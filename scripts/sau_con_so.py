#!/usr/bin/env python3
"""Tính sáu con số của một sprint (milestone) từ hạng mục và PR đã merge.

Dùng:  python3 sau_con_so.py --milestone "Sprint 1" [--issues TỆP --pulls TỆP] [-o tep.md] [--json]
Nguồn dữ liệu như so_uoc_luong.py (tệp JSON, SE358_DU_LIEU_THU, hoặc GitHub API).

Định nghĩa đã dùng (in kèm kết quả):
  1. Velocity: số hạng mục của milestone đã đóng, kèm tổng giờ khả năng nhất của các hạng mục đó.
  2. Cycle time trung bình: số ngày từ lúc tạo hạng mục tới lúc đóng hạng mục, trung bình trên các hạng mục đã đóng.
  3. Sai số ước lượng: (tổng giờ công thực tế − tổng giờ khả năng nhất) ÷ tổng giờ khả năng nhất, tính trên
     các hạng mục đã đóng có ước lượng và có ít nhất một PR đã merge.
  4. Tỷ lệ chấp nhận PR tác tử lần đầu: PR tác tử đã merge có Làm lại = 0 (và không có PR sau cùng hạng mục
     ghi Làm lại > 0) ÷ tổng PR tác tử đã merge của các hạng mục thuộc milestone.
  5. Tỷ trọng thẩm định: tổng giờ Thẩm định ÷ tổng giờ công, trên mọi PR đã merge của các hạng mục thuộc milestone.
  6. Chi phí token: tổng ô Token (đồng) trên cùng tập PR ở mục 5.
PR không có 'Đóng #<số>' (PR tài liệu) không được tính vào con số nào.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from so_uoc_luong import dinh_dang, lay_du_lieu, thoi_diem, tong_hop  # noqa: E402

DINH_NGHIA = [
    "Velocity: số hạng mục của milestone đã đóng (kèm tổng giờ khả năng nhất của các hạng mục đó).",
    "Cycle time: trung bình số ngày từ lúc tạo hạng mục tới lúc đóng hạng mục.",
    "Sai số ước lượng: (giờ công thực tế − giờ khả năng nhất) ÷ giờ khả năng nhất, cộng trên các hạng mục đã đóng có PR.",
    "Chấp nhận lần đầu: PR tác tử có Làm lại = 0 và không bị làm lại ở PR sau ÷ tổng PR tác tử.",
    "Tỷ trọng thẩm định: giờ Thẩm định ÷ tổng giờ công (Đặc tả + Thẩm định + Làm lại + Viết mã tay của PR làm tay).",
    "Chi phí token: tổng ô Token (đồng) của các PR thuộc milestone.",
]


def so_vn(x: float, chu_so: int = 1) -> str:
    return f"{x:.{chu_so}f}".replace(".", ",")


def co_dau(x: float) -> str:
    """Số có dấu, làm tròn hàng đơn vị: +14, −31, 0."""
    r = round(x)
    return ("+" if r > 0 else "−" if r < 0 else "") + str(abs(r))


def tien_vn(x: float) -> str:
    return f"{int(round(x)):,}".replace(",", ".") + " đ"


def cung_milestone(a: str, b: str) -> bool:
    return (a or "").strip().lower() == (b or "").strip().lower()


def tinh(dong: list[dict], prs: list[dict], milestone: str) -> dict:
    hm_ms = {hm["hang_muc"]: hm for hm in dong if cung_milestone(hm["milestone"], milestone)}
    da_dong = [hm for hm in hm_ms.values() if hm["dong_luc"]]
    kq: dict = {"milestone": milestone, "so_hang_muc": len(hm_ms)}

    kq["velocity"] = len(da_dong)
    kq["velocity_gio_kha_nang"] = sum(hm["uoc_kha_nang"] or 0 for hm in da_dong)

    ngay = [(thoi_diem(hm["dong_luc"]) - thoi_diem(hm["tao_luc"])).total_seconds() / 86400
            for hm in da_dong if hm["tao_luc"]]
    kq["cycle_time_ngay"] = sum(ngay) / len(ngay) if ngay else None
    kq["cycle_time_n"] = len(ngay)

    co_so = [hm for hm in da_dong if hm["uoc_kha_nang"] and hm["so_pr"]]
    tong_tt = sum(hm["gio_cong"] for hm in co_so)
    tong_knn = sum(hm["uoc_kha_nang"] for hm in co_so)
    kq["sai_so_pct"] = (tong_tt - tong_knn) / tong_knn * 100 if tong_knn else None
    kq["sai_so_n"] = len(co_so)
    kq["gio_cong_thuc_te"] = tong_tt
    kq["gio_kha_nang_nhat"] = tong_knn

    pr_ms = [p for p in prs if p.get("hang_muc") in hm_ms]
    pr_tt = [p for p in pr_ms if p["la_tac_tu"]]
    kq["pr_tac_tu"] = len(pr_tt)
    kq["pr_tac_tu_lan_dau"] = sum(1 for p in pr_tt if p["chap_nhan_lan_dau"])
    kq["chap_nhan_lan_dau_pct"] = kq["pr_tac_tu_lan_dau"] / len(pr_tt) * 100 if pr_tt else None

    tong_gio = sum(p.get("gio_cong", 0) for p in pr_ms)
    tham_dinh = sum(p["o"].get("tham_dinh") or 0 for p in pr_ms)
    kq["tham_dinh_gio"] = tham_dinh
    kq["tong_gio_cong"] = tong_gio
    kq["ty_trong_tham_dinh_pct"] = tham_dinh / tong_gio * 100 if tong_gio else None
    kq["so_pr"] = len(pr_ms)
    kq["token_dong"] = sum(p["o"].get("token_dong") or 0 for p in pr_ms)
    return kq


def bang_markdown(kq: dict) -> str:
    def hoac_n0(gia_tri, chuoi):
        return chuoi if gia_tri is not None else "n = 0"

    dong = [
        ("1. Velocity", f"{kq['velocity']} hạng mục ({so_vn(kq['velocity_gio_kha_nang'])} giờ khả năng nhất)",
         f"{kq['velocity']}/{kq['so_hang_muc']} hạng mục của milestone đã đóng"),
        ("2. Cycle time trung bình",
         hoac_n0(kq["cycle_time_ngay"], f"{so_vn(kq['cycle_time_ngay'] or 0)} ngày"),
         f"n = {kq['cycle_time_n']}; từ lúc tạo tới lúc đóng hạng mục"),
        ("3. Sai số ước lượng",
         hoac_n0(kq["sai_so_pct"], co_dau(kq["sai_so_pct"] or 0) + "%"),
         f"thực tế {so_vn(kq['gio_cong_thuc_te'])} giờ / khả năng nhất {so_vn(kq['gio_kha_nang_nhat'])} giờ; n = {kq['sai_so_n']}"),
        ("4. Chấp nhận PR tác tử lần đầu",
         hoac_n0(kq["chap_nhan_lan_dau_pct"], f"{kq['pr_tac_tu_lan_dau']}/{kq['pr_tac_tu']} ({so_vn(kq['chap_nhan_lan_dau_pct'] or 0, 0)}%)"),
         f"n = {kq['pr_tac_tu']} PR tác tử"),
        ("5. Tỷ trọng thẩm định",
         hoac_n0(kq["ty_trong_tham_dinh_pct"], f"{so_vn(kq['ty_trong_tham_dinh_pct'] or 0, 0)}%"),
         f"{so_vn(kq['tham_dinh_gio'])} / {so_vn(kq['tong_gio_cong'])} giờ công; n = {kq['so_pr']} PR"),
        ("6. Chi phí token", tien_vn(kq["token_dong"]), f"n = {kq['so_pr']} PR"),
    ]
    ra = [f"#### Sáu con số — {kq['milestone']}", "", "| Con số | Giá trị | Căn cứ |", "|---|---|---|"]
    ra += [f"| {a} | {b} | {c} |" for a, b, c in dong]
    return "\n".join(ra) + "\n"


def dinh_nghia_markdown() -> str:
    return "Định nghĩa đã dùng:\n\n" + "\n".join(f"- {d}" for d in DINH_NGHIA) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description="Tính sáu con số của một sprint.")
    ap.add_argument("--milestone", action="append", required=True, help='ví dụ "Sprint 1"; lặp lại được')
    ap.add_argument("--issues")
    ap.add_argument("--pulls")
    ap.add_argument("-o", "--ra")
    ap.add_argument("--json", action="store_true", help="in JSON thay cho Markdown")
    a = ap.parse_args()
    issues, pulls = lay_du_lieu(a.issues, a.pulls)
    dong, prs, _ = tong_hop(issues, pulls)
    ket_qua = [tinh(dong, prs, m) for m in a.milestone]
    if a.json:
        noi_dung = json.dumps(ket_qua, ensure_ascii=False, indent=2, default=dinh_dang) + "\n"
    else:
        noi_dung = "\n".join(bang_markdown(k) for k in ket_qua) + "\n" + dinh_nghia_markdown()
    if a.ra:
        with open(a.ra, "w", encoding="utf-8") as f:
            f.write(noi_dung)
    else:
        sys.stdout.write(noi_dung)


if __name__ == "__main__":
    main()
