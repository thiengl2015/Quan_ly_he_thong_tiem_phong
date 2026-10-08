# Bộ tác tử SE358 — Hướng dẫn sử dụng

SE358 – Quản trị dự án phát triển phần mềm · Năm học 2026–2027

> *Mỗi nhóm quản trị một dự án phần mềm nhỏ, trong đó phần lớn mã nguồn do tác tử AI viết; nhóm chịu trách nhiệm về đặc tả, thẩm định, chi phí và mọi quyết định của dự án. Trong cùng học kỳ, nhóm còn review chéo dự án của một nhóm khác.*

Bộ gồm bốn tác tử viết dưới dạng tệp chỉ dẫn Markdown. Nhóm dùng các tệp này với công cụ tác tử sẵn có, không phải tự xây tác tử. Kho mã của mỗi nhóm (tạo từ Kho mẫu SE358 qua GitHub Classroom) có sẵn bản sao của bộ trong thư mục `.se358/`.

## Bốn tác tử

| # | Tệp | Dùng để | Bắt buộc |
|---|---|---|---|
| 1 | `01_mo_phong_su_co.md` (kèm `01a_danh_muc_phieu.md`) | Sinh phiếu sự cố may đo theo dự án, từ mã nhóm và mã đợt | **Có**, mỗi đợt một lần |
| 2 | `02_tu_kiem_goi.md` | Đọc báo cáo của gói so với yêu cầu và tiêu chí chấm, chỉ ra chỗ thiếu trước khi gắn thẻ; không chấm điểm. Phần kiểm thủ tục do kiểm gói tự động (`kiem-goi`) làm | Không |
| 3 | `03_luyen_van_dap.md` | Luyện trả lời câu hỏi về chính phần việc của mình trước TH3 | Không |
| 4 | `04_gia_su.md` | Năm câu hỏi áp dụng sau mỗi buổi học; đóng vai persona của đề tài | Không |

**Mã đợt** do giảng viên công bố đầu tuần 5 (đợt 1), đầu tuần 7 (đợt 2) và đầu tuần 9 (đợt 3). Kèm mã đợt 1, giảng viên phát **bảng đổi theo đề tài**; nhóm giữ bảng này để chạy đợt 2 và đợt 3. Phiếu đợt 1 nộp cùng Gói 3, đợt 2 cùng Gói 4, đợt 3 cùng Gói 5, mỗi lần kèm log phiên và một mục Sổ NKQĐ xử lý phiếu.

**Nộp bài.** Kết quả của tác tử 1 được đưa vào kho mã: phiếu tại `phieu-su-co/dot<k>_N<xx>_SC-xx.md`, log phiên tại `log-tac-tu/phieu-dot<k>.md`, mục xử lý trong `nhat-ky-quyet-dinh.md`. Nhóm nộp gói bằng cách gắn và đẩy thẻ (`goi-2`…`goi-6`, `review-cheo`). Cấu trúc kho, quy trình một hạng mục và cách chạy kiểm gói xem Hướng dẫn Thực hành và Đồ án SE358, Mục 3.2 và 3.5.

## Dữ liệu tác tử cần đọc

- **Tệp trong kho**: `bao-cao/`, `nhat-ky-quyet-dinh.md`, `log-tac-tu/`, `phieu-su-co/`, mã nguồn.
- **Hạng mục và PR** (bảng công việc là tab Issues của kho): tác tử dòng lệnh đọc bằng `gh` nếu đã đăng nhập, ví dụ `gh issue list --state all --limit 300` và `gh pr list --state all --limit 300`.
- **Sổ Ước lượng** (`so-uoc-luong.csv`) và **sáu con số**: không nằm trong kho. Tải ở kết quả kiểm gói: tab **Actions** → **kiem-goi** → chọn lần chạy → mục **Artifacts** (Sổ Ước lượng và `ket-qua.md` có sáu con số). Chưa có lần chạy nào thì bấm **Run workflow** và chọn gói.

## Cách chạy

### (a) Tác tử dòng lệnh trong kho mã

1. Tạo một nhánh riêng cho phiên, ví dụ `se358/phieu-dot1`.
2. Đặt các tệp chưa nằm trong kho (gói ràng buộc, bảng đổi theo đề tài, `so-uoc-luong.csv` đã tải) vào `.se358/dau-vao/` và nói cho tác tử biết.
3. Mở tác tử dòng lệnh tại gốc kho mã và ra lệnh, ví dụ:
   `Đọc .se358/01_mo_phong_su_co.md và làm theo. Mã nhóm N07, đợt 1, mã đợt <mã đợt>, đề tài ĐT-C2, người chạy N07-C.`
4. Đọc lại tệp tác tử ghi ra, rồi đưa vào nhánh chính bằng PR theo mẫu PR của kho và ba quy tắc dưới đây; PR phải qua kiểm tra `kiem-pr`. PR chỉ chứa tệp tác tử ghi ra (phiếu, log phiên, báo cáo) là PR tài liệu: chỉ cần dòng ba thông tin, không cần `Đóng #` và số liệu thực tế. Kết quả có mặt trên nhánh chính trước khi gắn thẻ gói thì mới được nộp.

### (b) Trợ lý hội thoại bậc miễn phí

1. Mở một cuộc hội thoại mới bằng tài khoản của một thành viên trong nhóm.
2. Tải lên tệp chỉ dẫn của tác tử cần dùng (tác tử 1 thì tải cả `01a_danh_muc_phieu.md`) và các bản xuất cần thiết.
3. Gõ: `Làm theo tệp chỉ dẫn đã tải lên.` kèm các thông tin đầu vào mà tệp yêu cầu.
4. Chép kết quả vào tệp tương ứng trong kho mã (phiếu vào `phieu-su-co/`, log vào `log-tac-tu/`) rồi đưa vào nhánh chính qua PR.

Bản xuất gọn cho chế độ (b), chạy tại gốc kho. Các lệnh không xuất tên tác giả hay tài khoản GitHub:

```
git log --date=iso --pretty=format:'%h|%ad|%s' --stat > xuat-git-log.txt
git ls-files > xuat-danh-sach-tep.txt
gh issue list --state all --limit 300 --json number,title,body,milestone,state,createdAt,closedAt > xuat-hang-muc.json
gh pr list --state all --limit 300 --json number,title,body,state,mergedAt > xuat-pr.json
```

Kèm theo: tệp khai báo phụ thuộc (`package.json`, `requirements.txt`…), README, `so-uoc-luong.csv`, `nhat-ky-quyet-dinh.md`. Tệp quá lớn thì tải phần liên quan tới sprint đang làm.

## Quy tắc khi dùng

- **Không đưa dữ liệu ra ngoài tài khoản của nhóm.** Không dán dữ liệu dự án vào cuộc hội thoại dùng chung với người ngoài nhóm, không bật liên kết chia sẻ công khai.
- **Giữ bút danh.** Mọi tệp đưa vào tác tử gọi thành viên bằng mã `N07-A`, `N07-B`… theo thứ tự chữ cái tên; không họ tên, không MSSV, không tên tài khoản GitHub. Không cần đổi cấu hình git; chỉ cần dùng lệnh xuất ở trên. Bảng đối chiếu tên–mã không bao giờ đưa vào tác tử. Gói hồ sơ sẽ được tác tử đọc, và theo Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15, môn học hạn chế tối đa dữ liệu cá nhân đưa vào công cụ.
- **Lưu log phiên.** Với tác tử 1, log là bắt buộc, lưu tại `log-tac-tu/phieu-dot<k>.md` và nộp cùng phiếu. Log của PR tác tử thông thường lưu tại `log-tac-tu/PR-<số PR>.md`.
- **Không làm nhẹ phiếu sự cố.** Mã phiếu xác định theo ma trận và bảng đổi; tham số mức độ cố định. Giảng viên chạy lại tác tử với cùng mã để đối chiếu loại phiếu, tham số và các chi tiết tính từ mã của phiếu nộp.
- Ba quy tắc quản trị tác tử áp dụng cho mọi phiên, kể cả phiên dùng Bộ tác tử:
  1. **Tác tử không được merge.** Mọi thay đổi vào nhánh chính phải do người merge, sau khi đã được một thành viên khác (không phải người điều khiển phiên tác tử đó) review.
  2. **Mỗi PR phải ghi rõ ba thông tin**: công cụ tác tử đã dùng, mã người điều khiển và mã người review (ví dụ `Tác tử: <tên công cụ> · Điều khiển: N07-B · Review: N07-A`). PR không dùng tác tử ghi `Tác tử: không`.
  3. **Tác tử chỉ làm việc trên nhánh riêng và không được truy cập hạ tầng thật**: không giữ khoá triển khai, không có quyền ghi vào cơ sở dữ liệu thật; việc triển khai do người thực hiện.

## Ví dụ

Kết quả tác tử 1 với mã đợt giả (chỉ minh hoạ cách tra, không phải mã đợt thật):

| Nhóm | Mã đợt giả | Mã phiếu |
|---|---|---|
| N03 (đợt 2) | `K7Q2` | SC-06 |
| N12, đề tài loại D (đợt 2) | `K7Q2` | SC-15 |
| N19 (đợt 3) | `M4R8` | SC-14 |

Ví dụ giả sử N03 và N19 không có dòng trong bảng đổi, và trong cụm 3 chỉ N12 thuộc loại D.
