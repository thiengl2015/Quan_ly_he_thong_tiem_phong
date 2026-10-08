# Log tác tử

Thư mục chứa hai loại log.

**Log PR tác tử.** Mỗi PR có dòng `Tác tử:` khác `không` phải thêm tệp `log-tac-tu/PR-<số PR>.md` ngay trong PR đó. Kiểm tra PR tự động báo chưa đạt nếu thiếu tệp. Số PR biết được sau khi mở PR; mở PR trước, rồi đẩy thêm commit chứa log. PR tài liệu (ví dụ PR đưa phiếu sự cố và `phieu-dot<k>.md` vào kho) ghi `Tác tử: <công cụ>` thì log phiên tạo phiếu trong PR đó được chấp nhận, không cần thêm `PR-<số>.md`.

**Log phiên tạo phiếu sự cố.** Mỗi đợt một tệp `log-tac-tu/phieu-dot<k>.md` (k = 1, 2, 3), lưu toàn bộ phiên chạy tác tử mô phỏng sự cố cùng khối "Tóm tắt phiên". Nộp cùng gói kế tiếp: đợt 1 với Gói 3, đợt 2 với Gói 4, đợt 3 với Gói 5.

## Khuôn log PR tác tử

Chép khuôn dưới đây vào `log-tac-tu/PR-<số>.md` và điền đủ sáu mục. Có thể dán thêm bản ghi phiên của công cụ tác tử ở cuối tệp.

```markdown
# Log PR #<số> · Hạng mục #<số>

- Người điều khiển: N07-B
- Thời điểm: <bắt đầu> → <kết thúc>
- Công cụ tác tử: 
- Số vòng: 

## Yêu cầu ban đầu

<câu lệnh hoặc đặc tả giao cho tác tử, chép nguyên văn>

## Kết quả chạy kiểm thử cuối

<lệnh kiểm thử và kết quả: số ca đạt, số ca lỗi>

## Tóm tắt diff

<các tệp thay đổi, số dòng thêm và xoá, thay đổi chính>
```

Log ghi bằng mã thành viên. Không dán khoá, mật khẩu, họ tên, MSSV hay email vào log.
