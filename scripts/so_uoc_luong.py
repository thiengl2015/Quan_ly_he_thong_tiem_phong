#!/usr/bin/env python3
"""Sinh Sổ Ước lượng (so-uoc-luong.csv) từ hạng mục (GitHub Issues) và PR đã merge.
PR không có dòng 'Đóng #<số>' (PR tài liệu) không được tính.

Nguồn dữ liệu, theo thứ tự ưu tiên:
  1. --issues TỆP --pulls TỆP   (JSON lấy bằng `gh api --paginate`, chấp nhận nhiều mảng nối nhau)
  2. biến môi trường SE358_DU_LIEU_THU = thư mục có issues.json, pulls.json (chạy thử cục bộ)
  3. GitHub REST API với GITHUB_TOKEN và GITHUB_REPOSITORY (trong GitHub Actions)

Chỉ dùng thư viện chuẩn của Python 3.10+.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import urllib.request
from datetime import datetime

# ---------------------------------------------------------------- tải dữ liệu

def doc_json_noi(van_ban: str) -> list:
    """Đọc một hoặc nhiều mảng JSON nối liền nhau (đầu ra của gh api --paginate)."""
    giai_ma = json.JSONDecoder()
    i, kq = 0, []
    van_ban = van_ban.strip()
    while i < len(van_ban):
        while i < len(van_ban) and van_ban[i].isspace():
            i += 1
        if i >= len(van_ban):
            break
        obj, i = giai_ma.raw_decode(van_ban, i)
        if isinstance(obj, list):
            for x in obj:
                kq.extend(x if isinstance(x, list) else [x])  # --slurp tạo mảng lồng
        else:
            kq.append(obj)
    return kq


def doc_tep_json(duong_dan: str) -> list:
    with open(duong_dan, encoding="utf-8") as f:
        return doc_json_noi(f.read())


def goi_api(duong: str) -> list:
    """GET có phân trang trên GitHub REST API; trả về danh sách gộp."""
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    goc = os.environ.get("GITHUB_API_URL", "https://api.github.com")
    url = duong if duong.startswith("http") else f"{goc}/{duong.lstrip('/')}"
    kq: list = []
    while url:
        req = urllib.request.Request(url, headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "se358-kiem",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        })
        with urllib.request.urlopen(req, timeout=60) as r:
            du_lieu = json.loads(r.read().decode("utf-8"))
            lien_ket = r.headers.get("Link", "")
        kq.extend(du_lieu if isinstance(du_lieu, list) else [du_lieu])
        m = re.search(r'<([^>]+)>;\s*rel="next"', lien_ket)
        url = m.group(1) if m else None
    return kq


def lay_du_lieu(tep_issues: str | None = None, tep_pulls: str | None = None):
    """Trả về (issues, pulls). issues đã loại PR."""
    thu = os.environ.get("SE358_DU_LIEU_THU")
    if tep_issues and tep_pulls:
        issues, pulls = doc_tep_json(tep_issues), doc_tep_json(tep_pulls)
    elif thu:
        issues = doc_tep_json(os.path.join(thu, "issues.json"))
        pulls = doc_tep_json(os.path.join(thu, "pulls.json"))
    else:
        repo = os.environ.get("GITHUB_REPOSITORY")
        if not repo:
            sys.exit("Thiếu nguồn dữ liệu: cần --issues/--pulls, SE358_DU_LIEU_THU hoặc GITHUB_REPOSITORY.")
        issues = goi_api(f"repos/{repo}/issues?state=all&per_page=100")
        pulls = goi_api(f"repos/{repo}/pulls?state=closed&per_page=100")
    issues = [i for i in issues if "pull_request" not in i]
    return issues, pulls

# ---------------------------------------------------------------- phân tích

SO = re.compile(r"^\s*(\d+(?:[.,]\d+)?)")
MA_NGUOI = re.compile(r"^N\d\d-[A-F]$")
DONG_BA_THONG_TIN = re.compile(
    r"T[áa]c\s*t[ửu]\s*:\s*(?P<tac_tu>.*?)\s*[·|]\s*[ĐđD]i[ềe]u\s*khi[ểe]n\s*:\s*(?P<dieu_khien>\S*)"
    r"\s*[·|]\s*Review\s*:\s*(?P<review>\S*)", re.IGNORECASE)
DONG_HANG_MUC = re.compile(r"[ĐđD][óo]ng\s*#\s*(\d+)", re.IGNORECASE)

# khoá trong thân PR -> tên cột
KHOA_PR = {
    "dac_ta": r"[ĐđD][ặa]c\s*t[ảa]\s*\(gi[ờo]\)",
    "tac_tu_phut": r"T[áa]c\s*t[ửu]\s*ch[ạa]y\s*\(ph[úu]t\)",
    "vong": r"S[ốo]\s*v[òo]ng",
    "token_dong": r"Token\s*\([đd][ồo]ng\)",
    "tham_dinh": r"Th[ẩa]m\s*[đd][ịi]nh\s*\(gi[ờo]\)",
    "lam_lai": r"L[àa]m\s*l[ạa]i\s*\(gi[ờo]\)",
    "viet_ma_tay": r"Vi[ếe]t\s*m[ãa]\s*tay\s*\(gi[ờo]\)",
}
TEN_KHOA_PR = {
    "dac_ta": "Đặc tả (giờ)", "tac_tu_phut": "Tác tử chạy (phút)", "vong": "Số vòng",
    "token_dong": "Token (đồng)", "tham_dinh": "Thẩm định (giờ)", "lam_lai": "Làm lại (giờ)",
    "viet_ma_tay": "Viết mã tay (giờ)",
}

# tiêu đề trong form hạng mục -> khoá
TIEU_DE_FORM = {
    "cau_chuyen": "Câu chuyện người dùng",
    "tieu_chi": "Tiêu chí chấp nhận",
    "uoc_thap": "Ước lượng thấp (giờ công)",
    "uoc_kha_nang": "Ước lượng khả năng nhất (giờ công)",
    "uoc_cao": "Ước lượng cao (giờ công)",
    "cach_lam": "Cách làm",
    "phu_trach": "Người phụ trách (mã, ví dụ N07-B)",
}


def bo_chu_thich(van_ban: str | None) -> str:
    return re.sub(r"<!--.*?-->", "", van_ban or "", flags=re.S)


def doc_so(chuoi: str | None) -> float | None:
    if chuoi is None:
        return None
    m = SO.match(chuoi)
    return float(m.group(1).replace(",", ".")) if m else None


def doc_so_nguyen_dong(chuoi: str | None) -> float | None:
    """Số tiền đồng: chấp nhận 9000, 9.000, 9 000, 9.000 đ."""
    if chuoi is None:
        return None
    m = re.match(r"^\s*(\d[\d.\s]*)", chuoi)
    if not m:
        return None
    so = re.sub(r"\D", "", m.group(1))
    return float(so) if so else None


def phan_tich_form(than: str | None) -> dict:
    """Issue form sinh thân dạng '### Tiêu đề\\n\\ngiá trị'."""
    khoi: dict[str, str] = {}
    hien_tai = None
    for dong in (than or "").splitlines():
        m = re.match(r"^###\s+(.*\S)\s*$", dong)
        if m:
            hien_tai = m.group(1)
            khoi[hien_tai] = ""
        elif hien_tai is not None:
            khoi[hien_tai] += dong + "\n"
    kq: dict = {}
    for khoa, tieu_de in TIEU_DE_FORM.items():
        gia_tri = khoi.get(tieu_de)
        if gia_tri is not None:
            gia_tri = gia_tri.strip()
            if gia_tri == "_No response_":
                gia_tri = ""
        kq[khoa] = gia_tri
    for khoa in ("uoc_thap", "uoc_kha_nang", "uoc_cao"):
        kq[khoa] = doc_so(kq[khoa])
    cach = (kq.get("cach_lam") or "").strip().lower()
    kq["cach_lam"] = "tay" if cach == "tay" else ("tác tử" if cach else "")
    kq["phu_trach"] = (kq.get("phu_trach") or "").strip().upper()
    kq["la_hang_muc"] = TIEU_DE_FORM["uoc_kha_nang"] in khoi
    return kq


def phan_tich_pr(than: str | None) -> dict:
    """Đọc ba thông tin, các 'Đóng #', và các ô số từ thân PR."""
    van_ban = bo_chu_thich(than)
    kq: dict = {"tac_tu": None, "dieu_khien": None, "review": None, "dong": [], "o": {}, "o_tho": {}}
    m = DONG_BA_THONG_TIN.search(van_ban)
    if m:
        kq["tac_tu"] = m.group("tac_tu").strip().strip('"').strip()
        kq["dieu_khien"] = m.group("dieu_khien").strip()
        kq["review"] = m.group("review").strip()
    kq["dong"] = [int(x) for x in DONG_HANG_MUC.findall(van_ban)]
    for khoa, mau in KHOA_PR.items():
        mm = re.search(r"^[ \t>*|-]*" + mau + r"[ \t]*\**[ \t]*[:：|][ \t]*(.*?)[ \t]*\|?[ \t]*$", van_ban,
                       re.IGNORECASE | re.MULTILINE)
        tho = mm.group(1).strip() if mm else None
        kq["o_tho"][khoa] = tho
        if khoa == "token_dong":
            kq["o"][khoa] = doc_so_nguyen_dong(tho)
        else:
            kq["o"][khoa] = doc_so(tho)
    return kq


def la_pr_tac_tu(pr_pt: dict) -> bool:
    t = (pr_pt.get("tac_tu") or "").strip().lower()
    return bool(t) and t not in ("không", "khong", "none", "no")

# ---------------------------------------------------------------- tổng hợp

COT = ["hang_muc", "tieu_de", "milestone", "cach_lam", "phu_trach", "uoc_thap", "uoc_kha_nang", "uoc_cao",
       "dac_ta", "tac_tu_phut", "vong", "token_dong", "tham_dinh", "lam_lai", "viet_ma_tay",
       "gio_cong", "sai_so_pct", "so_pr", "lan_dau_khong_lam_lai", "tao_luc", "dong_luc"]


def thoi_diem(chuoi: str | None) -> datetime | None:
    return datetime.fromisoformat(chuoi.replace("Z", "+00:00")) if chuoi else None


def tong_hop(issues: list, pulls: list) -> tuple[list[dict], list[dict], list[str]]:
    """Trả về (dòng Sổ Ước lượng, danh sách PR đã merge có 'Đóng #' đã phân tích, cảnh báo).

    PR không có 'Đóng #' (PR tài liệu) bị bỏ qua."""
    canh_bao: list[str] = []
    hang_muc: dict[int, dict] = {}
    for iss in issues:
        f = phan_tich_form(iss.get("body"))
        nhan = [l.get("name") for l in iss.get("labels", []) if isinstance(l, dict)]
        if not f["la_hang_muc"] and "hang-muc" not in nhan:
            continue
        hang_muc[iss["number"]] = {
            "hang_muc": iss["number"], "tieu_de": iss.get("title", ""),
            "milestone": (iss.get("milestone") or {}).get("title", ""),
            "cach_lam": f["cach_lam"], "phu_trach": f["phu_trach"], "uoc_thap": f["uoc_thap"],
            "uoc_kha_nang": f["uoc_kha_nang"], "uoc_cao": f["uoc_cao"],
            "dac_ta": 0.0, "tac_tu_phut": 0.0, "vong": 0.0, "token_dong": 0.0,
            "tham_dinh": 0.0, "lam_lai": 0.0, "viet_ma_tay": 0.0, "gio_cong": 0.0,
            "so_pr": 0, "tao_luc": iss.get("created_at") or "",
            "dong_luc": (iss.get("closed_at") or "") if iss.get("state") == "closed" else "",
            "_dong": iss.get("state") == "closed",
        }
        hm = hang_muc[iss["number"]]
        if hm["uoc_kha_nang"] is None or hm["uoc_thap"] is None or hm["uoc_cao"] is None:
            canh_bao.append(f"Hạng mục #{iss['number']} thiếu hoặc sai ô ước lượng.")
        elif not (hm["uoc_thap"] <= hm["uoc_kha_nang"] <= hm["uoc_cao"]):
            canh_bao.append(f"Hạng mục #{iss['number']}: ước lượng không theo thứ tự thấp ≤ khả năng nhất ≤ cao.")
        if not hm["milestone"]:
            canh_bao.append(f"Hạng mục #{iss['number']} chưa gắn milestone.")
        if hm["phu_trach"] and not MA_NGUOI.match(hm["phu_trach"]):
            canh_bao.append(f"Hạng mục #{iss['number']}: người phụ trách `{hm['phu_trach']}` không đúng dạng N07-B.")

    pr_da_merge: list[dict] = []
    for pr in sorted(pulls, key=lambda p: p.get("merged_at") or ""):
        if not pr.get("merged_at"):
            continue
        pt = phan_tich_pr(pr.get("body"))
        if not pt["dong"]:   # PR tài liệu hoặc PR không gắn hạng mục: không đưa vào số liệu
            continue
        pt.update(so=pr["number"], merged_at=pr["merged_at"], created_at=pr.get("created_at"),
                  la_tac_tu=la_pr_tac_tu(pt), hang_muc=None)
        so_hm = pt["dong"][0]
        if so_hm not in hang_muc:
            canh_bao.append(f"PR #{pr['number']} đóng #{so_hm}, nhưng #{so_hm} không phải hạng mục.")
        else:
            pt["hang_muc"] = so_hm
        pr_da_merge.append(pt)

    # PR tác tử có làm lại ở PR sau (cùng hạng mục) thì không tính là chấp nhận lần đầu
    for i, pt in enumerate(pr_da_merge):
        sau = [q for q in pr_da_merge[i + 1:] if q["hang_muc"] is not None and q["hang_muc"] == pt["hang_muc"]]
        lam_lai_sau = any((q["o"].get("lam_lai") or 0) > 0 for q in sau)
        pt["chap_nhan_lan_dau"] = (pt["o"].get("lam_lai") or 0) == 0 and not lam_lai_sau

    for pt in pr_da_merge:
        if pt["hang_muc"] is None:
            continue
        hm = hang_muc[pt["hang_muc"]]
        hm["so_pr"] += 1
        for k in ("dac_ta", "tac_tu_phut", "vong", "token_dong", "tham_dinh", "lam_lai", "viet_ma_tay"):
            hm[k] += pt["o"].get(k) or 0.0
        gio = (pt["o"].get("dac_ta") or 0) + (pt["o"].get("tham_dinh") or 0) + (pt["o"].get("lam_lai") or 0)
        if hm["cach_lam"] == "tay" or not pt["la_tac_tu"]:
            gio += pt["o"].get("viet_ma_tay") or 0
        pt["gio_cong"] = gio
        hm["gio_cong"] += gio

    dong: list[dict] = []
    for so in sorted(hang_muc):
        hm = hang_muc[so]
        if hm["_dong"] and hm["so_pr"] == 0:
            canh_bao.append(f"Hạng mục #{so} đã đóng nhưng không có PR nào đã merge ghi 'Đóng #{so}'.")
        if hm["_dong"] and hm["uoc_kha_nang"] and hm["so_pr"]:
            hm["sai_so_pct"] = round((hm["gio_cong"] - hm["uoc_kha_nang"]) / hm["uoc_kha_nang"] * 100, 1)
        else:
            hm["sai_so_pct"] = None
        if hm["cach_lam"] == "tay":   # hạng mục làm tay: để trống Đặc tả và Tác tử chạy nếu không ghi
            for k in ("dac_ta", "tac_tu_phut", "vong", "token_dong"):
                if not hm[k]:
                    hm[k] = None
        hm["lan_dau_khong_lam_lai"] = ("co" if hm["lam_lai"] == 0 else "khong") if hm["so_pr"] else ""
        dong.append(hm)
    return dong, pr_da_merge, canh_bao


def dinh_dang(v) -> str:
    if v is None:
        return ""
    if isinstance(v, float):
        return str(int(v)) if v.is_integer() else f"{v:.2f}".rstrip("0").rstrip(".")
    return str(v)


def ghi_csv(dong: list[dict], duong_dan: str) -> None:
    with open(duong_dan, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(COT)
        for hm in dong:
            w.writerow([dinh_dang(hm.get(c)) for c in COT])


def main() -> None:
    ap = argparse.ArgumentParser(description="Sinh Sổ Ước lượng từ hạng mục và PR.")
    ap.add_argument("--issues")
    ap.add_argument("--pulls")
    ap.add_argument("-o", "--ra", default="so-uoc-luong.csv")
    a = ap.parse_args()
    issues, pulls = lay_du_lieu(a.issues, a.pulls)
    dong, _, canh_bao = tong_hop(issues, pulls)
    ghi_csv(dong, a.ra)
    print(f"Đã ghi {a.ra}: {len(dong)} hạng mục.")
    for c in canh_bao:
        print("Cảnh báo:", c, file=sys.stderr)


if __name__ == "__main__":
    main()
