#!/usr/bin/env python3
"""Kiểm thân PR theo mẫu SE358. Chạy trong GitHub Actions (sự kiện pull_request).

PR tài liệu (mọi tệp thay đổi thuộc bao-cao/, phieu-su-co/, nhat-ky-quyet-dinh.md, log-tac-tu/phieu-dot*.md
hoặc tệp .md ở gốc kho; được kèm log-tac-tu/PR-<số>.md) chỉ kiểm dòng ba thông tin và, nếu dùng tác tử,
log phiên; không đòi `Đóng #` và bốn cột.

Đọc PR từ tệp sự kiện GITHUB_EVENT_PATH. Danh sách tệp PR thay đổi lấy qua GitHub API;
khi chạy thử, đặt SE358_DU_LIEU_THU = thư mục có pr_files.json (mảng {"filename","status"}).
Ghi kết quả vào GITHUB_STEP_SUMMARY (nếu có) và thoát mã 1 khi có mục chưa đạt.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from so_uoc_luong import (KHOA_PR, MA_NGUOI, TEN_KHOA_PR, doc_tep_json, goi_api,  # noqa: E402
                          la_pr_tac_tu, phan_tich_pr)

O_TAC_TU = ["dac_ta", "tac_tu_phut", "vong", "token_dong", "tham_dinh", "lam_lai"]
O_TAY = ["tham_dinh", "lam_lai", "viet_ma_tay"]
LOG_PHIEU = re.compile(r"^log-tac-tu/phieu-dot\d+([_.-][^/]*)?\.md$")


def la_tep_tai_lieu(ten: str) -> bool:
    return (ten.startswith("bao-cao/") or ten.startswith("phieu-su-co/")
            or ten == "nhat-ky-quyet-dinh.md" or bool(LOG_PHIEU.match(ten))
            or ("/" not in ten and ten.lower().endswith(".md")))


def la_pr_tai_lieu(tep: list[str] | None, so_pr: int | None = None) -> bool:
    """Mọi tệp là tài liệu (log PR-<số PR này>.md được kèm), và có ít nhất một tệp tài liệu."""
    if not tep:
        return False
    log_pr = f"log-tac-tu/PR-{so_pr}.md"
    con_lai = [t for t in tep if t != log_pr]
    return bool(con_lai) and all(la_tep_tai_lieu(t) for t in con_lai)


def tep_thay_doi(so_pr: int, su_kien: dict) -> list[str] | None:
    thu = os.environ.get("SE358_DU_LIEU_THU")
    if thu:
        duong = os.path.join(thu, "pr_files.json")
        return [f["filename"] for f in doc_tep_json(duong) if f.get("status") != "removed"] \
            if os.path.exists(duong) else []
    repo = os.environ.get("GITHUB_REPOSITORY")
    try:
        ds = goi_api(f"repos/{repo}/pulls/{so_pr}/files?per_page=100")
        return [f["filename"] for f in ds if f.get("status") != "removed"]
    except Exception as loi:  # dự phòng: git diff với nhánh gốc
        print(f"Không gọi được API ({loi}); thử git diff.", file=sys.stderr)
        pr = su_kien.get("pull_request", {})
        goc, dau = pr.get("base", {}).get("sha"), pr.get("head", {}).get("sha")
        try:
            ra = subprocess.run(["git", "diff", "--name-only", "--diff-filter=d", f"{goc}...{dau}"],
                                capture_output=True, text=True, check=True).stdout
            return [x for x in ra.splitlines() if x]
        except Exception:
            return None


def kiem(than: str, so_pr: int, tep: list[str] | None, repo: str = "") -> list[tuple[str, bool, str]]:
    pt = phan_tich_pr(than)
    kq: list[tuple[str, bool, str]] = []

    tai_lieu = la_pr_tai_lieu(tep, so_pr)
    m_nhom = re.search(r"se358-(N\d\d)", repo or "", re.IGNORECASE)
    ma_nhom = m_nhom.group(1).upper() if m_nhom else None

    # 1. dòng ba thông tin
    if pt["tac_tu"] is None:
        kq.append(("Dòng ba thông tin", False,
                   "Không tìm thấy dòng `Tác tử: … · Điều khiển: Nxx-X · Review: Nxx-Y`."))
    else:
        loi = []
        if not pt["tac_tu"] or "<" in pt["tac_tu"]:
            loi.append("chưa ghi công cụ tác tử (hoặc `không`)")
        for ten, ma in (("Điều khiển", pt["dieu_khien"]), ("Review", pt["review"])):
            if not MA_NGUOI.match(ma or ""):
                loi.append(f"mã {ten} `{ma}` không đúng dạng N07-A")
            elif ma_nhom and not ma.startswith(ma_nhom + "-"):
                loi.append(f"mã {ten} `{ma}` không thuộc nhóm {ma_nhom}")
        kq.append(("Dòng ba thông tin", not loi, "; ".join(loi) or
                   f"Tác tử: {pt['tac_tu']} · Điều khiển: {pt['dieu_khien']} · Review: {pt['review']}"))
        dung_ma = MA_NGUOI.match(pt["dieu_khien"] or "") and MA_NGUOI.match(pt["review"] or "")
        if dung_ma:
            kq.append(("Người review khác người điều khiển", pt["dieu_khien"] != pt["review"],
                       "" if pt["dieu_khien"] != pt["review"] else "Review trùng Điều khiển."))

    tac_tu = la_pr_tac_tu(pt)
    if tai_lieu:
        kq.append(("Loại PR", True, "PR tài liệu: chỉ kiểm dòng ba thông tin"
                   + (" và log phiên" if tac_tu else "")))
        if tac_tu:
            ten_log = f"log-tac-tu/PR-{so_pr}.md"
            log = [t for t in tep if t == ten_log or LOG_PHIEU.match(t)]
            kq.append(("Log tác tử", bool(log),
                       "Có " + ", ".join(f"`{t}`" for t in log) if log else
                       f"PR có dùng tác tử nhưng chưa thêm `{ten_log}` hoặc `log-tac-tu/phieu-dot<k>.md`."))
        return kq

    # 2. Đóng #
    if len(pt["dong"]) == 1:
        kq.append(("Hạng mục đóng", True, f"Đóng #{pt['dong'][0]}"))
    elif not pt["dong"]:
        kq.append(("Hạng mục đóng", False, "Thiếu dòng `Đóng #<số hạng mục>`."))
    else:
        kq.append(("Hạng mục đóng", False,
                   "Mỗi PR ghi đúng một `Đóng #<số>`; đang có: " + ", ".join(f"#{x}" for x in pt["dong"])))

    # 3. ô số
    can = O_TAC_TU if tac_tu else O_TAY
    thieu = [TEN_KHOA_PR[k] for k in can
             if pt["o"].get(k) is None and pt["o_tho"].get(k) in (None, "", "-", "–")]
    sai = [f"{TEN_KHOA_PR[k]} = `{pt['o_tho'][k]}`" for k in KHOA_PR
           if pt["o_tho"].get(k) not in (None, "", "-", "–") and pt["o"].get(k) is None]
    ghi_chu = []
    if thieu:
        ghi_chu.append("thiếu: " + ", ".join(thieu))
    if sai:
        ghi_chu.append("không đọc được số: " + ", ".join(sai))
    kq.append(("Ô số liệu thực tế" + (" (PR tác tử)" if tac_tu else " (PR làm tay)"), not thieu and not sai,
               "; ".join(ghi_chu) or "Đủ ô"))

    # 4. log tác tử
    if tac_tu:
        ten_log = f"log-tac-tu/PR-{so_pr}.md"
        if tep is None:
            kq.append(("Log tác tử", False, f"Không lấy được danh sách tệp của PR để tìm `{ten_log}`."))
        else:
            kq.append(("Log tác tử", ten_log in tep,
                       f"Có `{ten_log}`" if ten_log in tep else f"PR chưa thêm hoặc sửa `{ten_log}`."))
    return kq


def in_ket_qua(so_pr: int, kq: list[tuple[str, bool, str]]) -> str:
    dat = all(x[1] for x in kq)
    loai = " (PR tài liệu)" if any(t == "Loại PR" for t, _, _ in kq) else ""
    ra = [f"### Kiểm PR #{so_pr}{loai}: {'ĐẠT' if dat else 'CHƯA ĐẠT'}", "",
          "| Kiểm tra | Kết quả | Ghi chú |", "|---|---|---|"]
    ra += [f"| {ten} | {'Đạt' if ok else 'Chưa đạt'} | {gc.replace('|', '/')} |" for ten, ok, gc in kq]
    if not dat:
        ra += ["", "Sửa thân PR (Edit ở mô tả PR) hoặc thêm tệp log rồi đẩy lại; kiểm tra tự chạy lại."]
    return "\n".join(ra) + "\n"


def main() -> None:
    duong = os.environ.get("GITHUB_EVENT_PATH")
    if not duong:
        sys.exit("Thiếu GITHUB_EVENT_PATH.")
    with open(duong, encoding="utf-8") as f:
        su_kien = json.load(f)
    pr = su_kien.get("pull_request") or {}
    so_pr = pr.get("number") or su_kien.get("number")
    than = pr.get("body") or ""
    tep = tep_thay_doi(so_pr, su_kien)
    kq = kiem(than, so_pr, tep, os.environ.get("GITHUB_REPOSITORY", ""))
    noi_dung = in_ket_qua(so_pr, kq)
    tom_tat = os.environ.get("GITHUB_STEP_SUMMARY")
    if tom_tat:
        with open(tom_tat, "a", encoding="utf-8") as f:
            f.write(noi_dung)
    print(noi_dung)
    sys.exit(0 if all(x[1] for x in kq) else 1)


if __name__ == "__main__":
    main()
