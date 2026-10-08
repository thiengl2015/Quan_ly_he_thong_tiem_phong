# Kho dự án SE358

Kho mã của nhóm cho đồ án SE358 – Quản trị dự án phát triển phần mềm. Kho được tạo từ Kho mẫu SE358 khi nhóm nhận bài tập nhóm trên GitHub Classroom, nằm trong tổ chức GitHub của lớp. Giảng viên khoá nhánh chính và bảo vệ thẻ nộp bài sau hạn tạo kho (cuối tuần 2). Nhóm không tự đổi cấu hình kho.

Nhóm thay phần giới thiệu này bằng README của sản phẩm (cách cài đặt, cách chạy, cách chạy kiểm thử). Giữ lại các mục bên dưới hoặc chuyển sang `QUY-TRINH.md`.

## Cấu trúc kho

| Đường dẫn | Nội dung |
|---|---|
| `bao-cao/` | Sáu báo cáo bằng Markdown: `goi2-ke-hoach.md`, `goi3-sprint1.md`, `goi4-sprint2.md`, `goi5-sprint3.md`, `review-cheo.md`, `goi6-tong-ket.md`. Hình đặt trong `bao-cao/hinh/`. Bản PDF cùng tên là tuỳ chọn; bản Markdown là bản chấm. |
| `nhat-ky-quyet-dinh.md` | Sổ Nhật ký Quyết định (Sổ NKQĐ), có sẵn khuôn mục thường và khuôn mục xử lý phiếu sự cố. |
| `log-tac-tu/` | Log PR tác tử `PR-<số>.md` và log phiên tạo phiếu sự cố `phieu-dot<k>.md`. Khuôn trong `log-tac-tu/README.md`. |
| `phieu-su-co/` | Phiếu sự cố đã sinh, `dot<k>_N<xx>_SC-xx.md`. |
| `.se358/` | Bộ tác tử SE358. |
| `.github/`, `scripts/` | Mẫu hạng mục, mẫu PR, kiểm tra tự động. Không sửa. |
| Các thư mục khác | Mã nguồn sản phẩm. |

Bảng công việc là tab **Issues** của kho (kèm milestone `Sprint 1`, `Sprint 2`, `Sprint 3` và Project nếu nhóm muốn xem dạng bảng). Sổ Ước lượng sinh tự động từ hạng mục và PR, không lưu trong kho và không nhập tay.

Trong mọi tệp, PR và hạng mục, thành viên được gọi bằng mã (`N07-A`, `N07-B`…). Không ghi họ tên, MSSV hay email.

## Quy trình một hạng mục

1. **Tạo hạng mục** ở tab Issues bằng mẫu **Hạng mục**: câu chuyện người dùng, tiêu chí chấp nhận Cho trước – Khi – Thì, ước lượng giờ công ba số (thấp, khả năng nhất, cao), cách làm (`tác tử` hoặc `tay`), người phụ trách (mã, không bắt buộc). Gắn milestone của sprint. Ước lượng ghi khi tạo, không sửa về sau.
2. **Làm trên nhánh riêng**, mỗi hạng mục một nhánh. Tác tử chỉ làm việc trên nhánh này.
3. **Mở PR theo mẫu**: dòng ba thông tin, `Đóng #<số hạng mục>`, các dòng số liệu thực tế. PR tác tử thêm tệp `log-tac-tu/PR-<số PR>.md` trong chính PR đó. Kiểm tra `kiem-pr` chạy mỗi khi mở, sửa mô tả hoặc đẩy thêm commit; chưa đạt thì không merge được.
4. **Review**: một thành viên khác người điều khiển đọc diff, chạy thử và duyệt PR.
5. **Người merge** PR sau khi có duyệt và `kiem-pr` đạt.
6. **Nghiệm thu**: Chủ sản phẩm kiểm theo tiêu chí chấp nhận rồi đóng hạng mục. Thời điểm đóng hạng mục được dùng để tính velocity và cycle time.

Làm lại sau khi đã merge thì mở PR mới ghi `Đóng #` cùng hạng mục; số liệu các PR được cộng dồn.

**PR tài liệu.** PR chỉ sửa tệp trong `bao-cao/`, `phieu-su-co/`, `nhat-ky-quyet-dinh.md`, `log-tac-tu/phieu-dot<k>.md` hoặc tệp `.md` ở gốc kho chỉ cần dòng ba thông tin, không cần `Đóng #` và các dòng số liệu. `kiem-pr` tự nhận ra loại PR này theo danh sách tệp thay đổi và ghi "PR tài liệu" ở trang tóm tắt. Nếu PR tài liệu có dùng tác tử (ví dụ PR đưa phiếu sự cố vào kho), PR phải chứa log `log-tac-tu/phieu-dot<k>.md` hoặc `log-tac-tu/PR-<số>.md`. PR tài liệu không được tính vào Sổ Ước lượng và sáu con số.

## Ba quy tắc quản trị tác tử

1. **Tác tử không được merge.** Mọi thay đổi vào nhánh chính phải do người merge, sau khi đã được một thành viên khác (không phải người điều khiển phiên tác tử đó) review.
2. **Mỗi PR phải ghi rõ ba thông tin**: công cụ tác tử đã dùng, mã người điều khiển và mã người review (ví dụ `Tác tử: <tên công cụ> · Điều khiển: N07-B · Review: N07-A`). PR không dùng tác tử ghi `Tác tử: không`.
3. **Tác tử chỉ làm việc trên nhánh riêng và không được truy cập hạ tầng thật**: không giữ khoá triển khai, không có quyền ghi vào cơ sở dữ liệu thật; việc triển khai do người thực hiện.

**Chế tài**: vi phạm quy tắc 1 ⇒ **tiêu chí 1 của mốc sprint tương ứng = 0**. Vi phạm quy tắc 2 hoặc 3 ⇒ trừ ở tiêu chí 1 theo mức độ.

## Phiếu sự cố

Tác tử mô phỏng sự cố (tác tử 1 trong `.se358/`) là **bắt buộc ở cả ba đợt**. Đầu tuần 5, 7, 9, giảng viên công bố mã đợt; trong tuần đó nhóm chạy tác tử 1 với mã nhóm và mã đợt, lưu phiếu và log, rồi ghi phần xử lý thành một mục Sổ NKQĐ. Chi tiết trong `phieu-su-co/README.md`.

## Nộp bài

Nộp một gói là gắn thẻ trên nhánh chính và đẩy thẻ lên kho trước 23h59 ngày hạn. Tài liệu của gói phải được merge vào nhánh chính trước khi gắn thẻ.

```bash
git checkout main && git pull
git tag goi-3 && git push origin goi-3
```

Tên thẻ: `goi-2`, `goi-3`, `goi-4`, `goi-5`, `goi-6`; Báo cáo review chéo gắn thẻ `review-cheo`. Thẻ đã đẩy không xoá hay dời được, vì vậy chỉ gắn thẻ khi gói đã sẵn sàng. Giảng viên lấy bài theo mã commit mà thẻ trỏ tới lúc hạn.

## Kết quả kiểm gói và sáu con số

Khi đẩy thẻ, kiểm tra `kiem-goi` chạy tự động. Muốn kiểm trước khi gắn thẻ: tab **Actions** → **kiem-goi** → **Run workflow** → chọn gói.

Xem kết quả: tab **Actions** → chọn lần chạy → **Summary**. Trang tóm tắt có bảng đạt/chưa đạt (tệp báo cáo đúng tên và đã điền, số mục Sổ NKQĐ, phiếu sự cố và log ở Gói 3, 4, 5, không có email trong tệp, có ít nhất một hạng mục ở Gói 2–6) và sáu con số của sprint tương ứng (Gói 3: Sprint 1, Gói 4: Sprint 2, Gói 5: Sprint 3). Chép sáu con số vào báo cáo sprint và bình luận.

Mục **Cảnh báo** không làm gói bị đánh trượt nhưng cần xem lại: dãy tám chữ số giống MSSV (số tiền ghi kèm `đ`, `đồng`, `VND`, `triệu` hoặc có dấu phân cách thì không bị báo) và hạng mục chưa gắn milestone.

Sổ Ước lượng (`so-uoc-luong.csv`) tải ở mục **Artifacts** cuối trang tóm tắt.

Kết quả kiểm gói là kiểm thủ tục, không phải điểm. Lần chạy có mục chưa đạt hiện dấu đỏ; thẻ vẫn được ghi nhận là đã nộp.
