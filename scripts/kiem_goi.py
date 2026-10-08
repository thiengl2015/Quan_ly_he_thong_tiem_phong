#!/usr/bin/env python3
"""Kiểm gói nộp SE358 (không chấm điểm).

Dùng:  python3 scripts/kiem_goi.py --goi 3 [--kho .] [--ra-thu-muc ket-qua]
       --goi nhận 2, 3, 4, 5, 6, review-cheo hoặc tên thẻ (goi-3, review-cheo).
       Không có --goi thì lấy từ GITHUB_REF_NAME.
Ghi: <ra-thu-muc>/so-uoc-luong.csv, <ra-thu-muc>/ket-qua.md; nội dung kết quả thêm vào GITHUB_STEP_SUMMARY.
Thoát mã 1 khi có mục chưa đạt. Mục "Cảnh báo" (dãy số giống MSSV, hạng mục chưa gắn milestone)
không làm gói bị đánh trượt.
"""
from __future__ import annotations

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sau_con_so import bang_markdown, dinh_nghia_markdown, tinh  # noqa: E402
from so_uoc_luong import bo_chu_thich, ghi_csv, lay_du_lieu, tong_hop  # noqa: E402

BAO_CAO = {
    "2": "bao-cao/goi2-ke-hoach.md",
    "3": "bao-cao/goi3-sprint1.md",
    "4": "bao-cao/goi4-sprint2.md",
    "5": "bao-cao/goi5-sprint3.md",
    "review-cheo": "bao-cao/review-cheo.md",
    "6": "bao-cao/goi6-tong-ket.md",
}
SPRINT = {"3": ["Sprint 1"], "4": ["Sprint 2"], "5": ["Sprint 3"], "6": ["Sprint 1", "Sprint 2", "Sprint 3"]}
GIU_CHO = re.compile(r"<!--\s*điền\s*:", re.IGNORECASE)
MUC_NKQD = re.compile(r"^##\s+QĐ-\d+", re.MULTILINE)
MUC_PHIEU = re.compile(r"^##\s+QĐ-\d+.*\bSC-\d\d\b", re.MULTILINE)
MSSV = re.compile(r"(?<![\d.,])2\d{7}(?![\d.,])")
DON_VI_TIEN = r"(?:đ|đồng|vnd|vnđ|triệu|tr)\b"
TIEN_SAU = re.compile(r"^\s*" + DON_VI_TIEN, re.IGNORECASE)
TIEN_TRUOC = re.compile(r"(?:vnd|vnđ)\s*$", re.IGNORECASE)
NGAY_8_SO = re.compile(r"^20[2-3]\d(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])$")
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
EMAIL_BO_QUA = re.compile(r"(^noreply@github\.com$|noreply\.github\.com|users\.noreply|@example\.(com|org|net)$|^git@github\.com$)",
                          re.IGNORECASE)
BO_QUA_THU_MUC = {".git", ".se358", ".github", "scripts", "node_modules", ".venv", "venv", "__pycache__",
                  "dist", "build", ".next", "target", "vendor"}


def chuan_goi(g: str) -> str:
    g = (g or "").strip().lower()
    if g.startswith("refs/tags/"):
        g = g[len("refs/tags/"):]
    if g in ("review-cheo", "review"):
        return "review-cheo"
    m = re.fullmatch(r"(?:goi-?)?([2-6])", g)
    if not m:
        sys.exit(f"Không nhận ra gói: {g!r}")
    return m.group(1)


def doc(duong: str) -> str | None:
    try:
        with open(duong, encoding="utf-8") as f:
            return f.read()
    except (FileNotFoundError, UnicodeDecodeError):
        return None


def kiem_bao_cao(kho: str, tep: str) -> tuple[bool, str]:
    nd = doc(os.path.join(kho, tep))
    if nd is None:
        return False, f"Không có `{tep}`."
    so_giu_cho = len(GIU_CHO.findall(nd))
    if so_giu_cho:
        return False, f"`{tep}` còn {so_giu_cho} dòng giữ chỗ `<!-- điền: … -->`."
    if len(bo_chu_thich(nd).split()) < 50:
        return False, f"`{tep}` gần như trống."
    return True, f"`{tep}` đã điền."


def la_so_tien(dong: str, m: re.Match) -> bool:
    return bool(TIEN_SAU.match(dong[m.end():]) or TIEN_TRUOC.search(dong[:m.start()]))


def quet_rieng_tu(kho: str) -> tuple[list[str], list[str]]:
    """Trả về (chỗ có email, chỗ có dãy giống MSSV)."""
    gap_email: list[str] = []
    gap_mssv: list[str] = []
    for goc, thu_muc, tep in os.walk(kho):
        thu_muc[:] = [d for d in thu_muc if d not in BO_QUA_THU_MUC]
        for ten in tep:
            duong = os.path.join(goc, ten)
            try:
                if os.path.getsize(duong) > 2_000_000:
                    continue
                with open(duong, "rb") as f:
                    du = f.read()
                if b"\x00" in du[:4096]:
                    continue
                nd = du.decode("utf-8", errors="ignore")
            except OSError:
                continue
            tuong_doi = os.path.relpath(duong, kho)
            for so_dong, dong in enumerate(nd.splitlines(), 1):
                for m in MSSV.finditer(dong):
                    if not NGAY_8_SO.match(m.group(0)) and not la_so_tien(dong, m):
                        gap_mssv.append(f"`{tuong_doi}:{so_dong}` có dãy 8 chữ số giống MSSV ({m.group(0)[:2]}…)")
                for m in EMAIL.finditer(dong):
                    if not EMAIL_BO_QUA.search(m.group(0)):
                        gap_email.append(f"`{tuong_doi}:{so_dong}` có địa chỉ email")
    return gap_email, gap_mssv


def gop(ds: list[str], toi_da: int = 20) -> str:
    return "<br>".join(ds[:toi_da]) + (f"<br>… và {len(ds) - toi_da} chỗ khác" if len(ds) > toi_da else "")


def ma_nhom_tu_repo() -> str | None:
    m = re.search(r"se358-(N\d\d)", os.environ.get("GITHUB_REPOSITORY", ""), re.IGNORECASE)
    return m.group(1).upper() if m else None


def kiem_goi(kho: str, goi: str, ma_nhom: str | None) -> tuple[list[tuple[str, bool, str]], dict]:
    kq: list[tuple[str, bool, str]] = []
    tt: dict = {}

    ok, gc = kiem_bao_cao(kho, BAO_CAO[goi])
    kq.append(("Báo cáo của gói", ok, gc))
    if goi == "5":
        ok_rc = True
        nd = doc(os.path.join(kho, BAO_CAO["5"])) or ""
        if not re.search(r"trả lời.*review chéo", nd, re.IGNORECASE):
            ok_rc = False
        kq.append(("Đoạn trả lời review chéo trong Báo cáo Sprint 3", ok_rc,
                   "" if ok_rc else "Không thấy mục trả lời Báo cáo review chéo."))
    if goi == "6":
        for g in ("2", "3", "4", "5"):
            ok, gc = kiem_bao_cao(kho, BAO_CAO[g])
            kq.append((f"Báo cáo Gói {g} vẫn còn trong kho", ok, gc))
        kq.append(("README.md ở gốc kho", os.path.exists(os.path.join(kho, "README.md")), ""))

    # Sổ NKQĐ
    nkqd = doc(os.path.join(kho, "nhat-ky-quyet-dinh.md"))
    if nkqd is None:
        kq.append(("Sổ NKQĐ", False, "Không có `nhat-ky-quyet-dinh.md` ở gốc kho."))
    else:
        nd = bo_chu_thich(nkqd)
        so_muc, so_phieu = len(MUC_NKQD.findall(nd)), len(MUC_PHIEU.findall(nd))
        tt["nkqd"] = (so_muc, so_phieu)
        if goi in ("3", "4", "5"):
            can = int(goi) - 2
            kq.append(("Sổ NKQĐ: mục xử lý phiếu sự cố", so_phieu >= can,
                       f"{so_muc} mục, trong đó {so_phieu} mục xử lý phiếu (cần ≥ {can} tới gói này)"))
        elif goi == "6":
            kq.append(("Sổ NKQĐ: tối thiểu 6 mục, 3 mục xử lý phiếu", so_muc >= 6 and so_phieu >= 3,
                       f"{so_muc} mục, trong đó {so_phieu} mục xử lý phiếu"))
        else:
            kq.append(("Sổ NKQĐ", True, f"{so_muc} mục, trong đó {so_phieu} mục xử lý phiếu"))

    # phiếu sự cố và log phiên
    if goi in ("3", "4", "5"):
        dot = int(goi) - 2
        nhom = ma_nhom or r"N\d\d"
        mau = re.compile(rf"^dot{dot}_{nhom}_SC-\d\d\.md$")
        thu_muc = os.path.join(kho, "phieu-su-co")
        phieu = sorted(t for t in (os.listdir(thu_muc) if os.path.isdir(thu_muc) else []) if mau.match(t))
        kq.append((f"Phiếu sự cố đợt {dot}", bool(phieu),
                   ", ".join(f"`phieu-su-co/{p}`" for p in phieu) or
                   f"Không có `phieu-su-co/dot{dot}_{ma_nhom or 'Nxx'}_SC-xx.md`."))
        thu_muc = os.path.join(kho, "log-tac-tu")
        log = sorted(t for t in (os.listdir(thu_muc) if os.path.isdir(thu_muc) else [])
                     if re.match(rf"^phieu-dot{dot}([_.-].*)?\.md$", t))
        kq.append((f"Log phiên tạo phiếu đợt {dot}", bool(log),
                   ", ".join(f"`log-tac-tu/{t}`" for t in log) or f"Không có `log-tac-tu/phieu-dot{dot}.md`."))

    # dữ liệu cá nhân: email làm trượt; dãy giống MSSV chỉ cảnh báo (có thể là số khác)
    gap_email, gap_mssv = quet_rieng_tu(kho)
    kq.append(("Không có email trong tệp", not gap_email, gop(gap_email) if gap_email else "Không thấy."))
    kq.append(("Không có MSSV trong tệp", None if gap_mssv else True,
               (gop(gap_mssv) + "<br>Nếu là MSSV thì thay bằng mã bút danh; nếu là số khác thì bỏ qua.")
               if gap_mssv else "Không thấy."))
    return kq, tt


def main() -> None:
    ap = argparse.ArgumentParser(description="Kiểm gói nộp SE358.")
    ap.add_argument("--goi", default=os.environ.get("SE358_GOI") or os.environ.get("GITHUB_REF_NAME"))
    ap.add_argument("--kho", default=".")
    ap.add_argument("--ma-nhom", default=None)
    ap.add_argument("--ra-thu-muc", default="ket-qua-kiem-goi")
    ap.add_argument("--issues")
    ap.add_argument("--pulls")
    a = ap.parse_args()
    goi = chuan_goi(a.goi)
    ma_nhom = (a.ma_nhom or ma_nhom_tu_repo() or "").upper() or None
    os.makedirs(a.ra_thu_muc, exist_ok=True)

    kq, _ = kiem_goi(a.kho, goi, ma_nhom)

    # Sổ Ước lượng và sáu con số
    phan_so = ""
    canh_bao: list[str] = []
    try:
        issues, pulls = lay_du_lieu(a.issues, a.pulls)
        dong, prs, canh_bao = tong_hop(issues, pulls)
        ghi_csv(dong, os.path.join(a.ra_thu_muc, "so-uoc-luong.csv"))
        if goi == "review-cheo":   # review chéo không đòi hạng mục
            kq.append(("Sổ Ước lượng sinh từ hạng mục và PR", True,
                       f"{len(dong)} hạng mục, {len(prs)} PR đã merge có `Đóng #`; không bắt buộc ở gói này"))
        else:
            kq.append(("Sổ Ước lượng sinh từ hạng mục và PR", bool(dong),
                       f"{len(dong)} hạng mục, {len(prs)} PR đã merge có `Đóng #`; tải tệp ở mục Artifacts"
                       if dong else "Chưa có hạng mục nào tạo bằng mẫu Hạng mục (cần ít nhất một)."))
        khong_ms = [f"#{hm['hang_muc']}" for hm in dong if not hm["milestone"]]
        if dong:
            kq.append(("Hạng mục có milestone", None if khong_ms else True,
                       ("Chưa gắn milestone: " + ", ".join(khong_ms[:30])
                        + (" …" if len(khong_ms) > 30 else "")) if khong_ms else "Mọi hạng mục đã gắn milestone."))
        for m in SPRINT.get(goi, []):
            phan_so += bang_markdown(tinh(dong, prs, m)) + "\n"
        if phan_so:
            phan_so += dinh_nghia_markdown()
    except SystemExit:
        raise
    except Exception as loi:
        kq.append(("Sổ Ước lượng sinh từ hạng mục và PR", False, f"Không lấy được dữ liệu: {loi}"))

    ten_goi = "Báo cáo review chéo" if goi == "review-cheo" else f"Gói {goi}"
    dat = all(x[1] is not False for x in kq)
    ra = [f"## Kiểm {ten_goi}{' · ' + ma_nhom if ma_nhom else ''}: {'ĐẠT' if dat else 'CÒN MỤC CHƯA ĐẠT'}", "",
          "Kết quả kiểm thủ tục, không phải điểm.", "",
          "| Kiểm tra | Kết quả | Ghi chú |", "|---|---|---|"]
    nhan = {True: "Đạt", False: "Chưa đạt", None: "Cảnh báo"}
    ra += [f"| {t} | {nhan[ok]} | {g.replace('|', '/')} |" for t, ok, g in kq]
    if phan_so:
        ra += ["", "### Sáu con số", "", phan_so]
    if canh_bao:
        ra += ["", "### Cảnh báo dữ liệu hạng mục và PR", ""] + [f"- {c}" for c in canh_bao[:40]]
        if len(canh_bao) > 40:
            ra.append(f"- … và {len(canh_bao) - 40} cảnh báo khác")
    noi_dung = "\n".join(ra) + "\n"

    with open(os.path.join(a.ra_thu_muc, "ket-qua.md"), "w", encoding="utf-8") as f:
        f.write(noi_dung)
    tom_tat = os.environ.get("GITHUB_STEP_SUMMARY")
    if tom_tat:
        with open(tom_tat, "a", encoding="utf-8") as f:
            f.write(noi_dung)
    print(noi_dung)
    sys.exit(0 if dat else 1)


if __name__ == "__main__":
    main()
