# Danh mục 16 phiếu sự cố — dùng cho tác tử 1

Tệp dữ liệu của tác tử Mô phỏng sự cố (`01_mo_phong_su_co.md`). Hai tệp `01_mo_phong_su_co.md` (ma trận vị trí, quy tắc đổi, mẫu phiếu đã sinh) và tệp này cùng nội dung với bản in "SE358 — Bộ phiếu sự cố" (`SE358_Phieu_Su_Co_2026.docx`). Tình huống khung và "Điều nhóm phải chứng minh" lấy nguyên văn từ Hướng dẫn Thực hành và Đồ án SE358, mục Phiếu sự cố. Tham số cố định không được làm nhẹ. Chỗ ghi [cần GV xác nhận] là chỗ giảng viên cần chốt; tác tử giữ nguyên câu chữ gốc ở chỗ đó và không tự đặt số.

## Phân đợt

| Đợt | Mã đợt công bố | Phiếu của đợt | Mục Sổ NKQĐ nộp cùng |
|---|---|---|---|
| 1 | Đầu tuần 5 | SC-02 · SC-08 · SC-10 · SC-12 · SC-13 | Gói 3 (cuối tuần 6) |
| 2 | Đầu tuần 7 | SC-03 · SC-05 · SC-06 · SC-07 · SC-11 · SC-15 | Gói 4 (cuối tuần 8) |
| 3 | Đầu tuần 9 | SC-01 · SC-04 · SC-09 · SC-14 · SC-16 | Gói 5 (cuối tuần 10) |

## SC-01 · Cắt ngân sách · đợt 3

**Tình huống khung (nguyên văn):** Bên tài trợ thông báo cắt 20% ngân sách còn lại, có hiệu lực ngay. Lý do: công ty điều chỉnh kế hoạch chi tiêu giữa năm. Phạm vi cam kết không đổi.

**Tham số cố định:**
- Cắt đúng **20% ngân sách còn lại**, có hiệu lực ngay tại ngày chạy.
- Phạm vi cam kết không đổi.

**Số liệu:**
- Trần ngân sách: tra Bảng tra số liệu theo đề tài.
- AC đến ngày chạy: tính từ Sổ Ước lượng theo công thức AC = giờ công × 150.000 đ + chi phí token/API thật + hạ tầng thật.
- Ngân sách còn lại = trần ngân sách − AC. Khoản bị cắt = 20% × ngân sách còn lại. Khoản bị cắt không được lớn hơn cột "20% trần" của bảng tra; nếu lớn hơn thì AC đã tính sai, phải tính lại.

**Chỗ cần may đo:**
- Không có lựa chọn ngẫu nhiên.
- Liệt kê các hạng mục còn lại trong backlog cam kết kèm ước lượng khả năng nhất, để nhóm thấy khoản cắt tương ứng bao nhiêu giờ công.

**Điều nhóm phải chứng minh (nguyên văn):** Phân biệt chi phí cố định với chi phí điều chỉnh được; cắt tiền luôn kéo theo cắt một thứ khác.

## SC-02 · Yêu cầu nhỏ giữa sprint · đợt 1

**Tình huống khung (nguyên văn):** Khách hàng đề nghị bổ sung hai chức năng "rất nhỏ, chắc chỉ mất một buổi" ngay giữa sprint đang chạy. Người đề nghị là bên liên quan có quyền lực cao.

**Tham số cố định:**
- Đúng **hai** chức năng mới, người đề nghị cho rằng "chắc chỉ mất một buổi".
- Đề nghị đến giữa sprint đang chạy, từ bên liên quan có quyền lực cao.

**Số liệu:**
- Không có số liệu tra bảng.

**Chỗ cần may đo:**
- Người đề nghị: persona có quyền lực cao trong ma trận quyền lực – quan tâm của Kế hoạch dự án; nếu có nhiều người cùng mức, chọn bằng băm, ô 1, danh sách xếp theo thứ tự xuất hiện trong Kế hoạch.
- Hai chức năng: chọn một hạng mục neo bằng băm, ô 2, trong các hạng mục của sprint đang chạy (xếp theo mã hạng mục tăng dần). Tác tử viết hai chức năng gắn với hạng mục neo, chưa có trong backlog, nghe nhỏ theo cách người đề nghị mô tả.

**Điều nhóm phải chứng minh (nguyên văn):** Ước lượng công việc phát sinh trung thực; từ chối hoặc trì hoãn mà không làm hỏng quan hệ.

## SC-03 · Thành viên vắng mặt · đợt 2

**Tình huống khung (nguyên văn):** Một thành viên phải nghỉ hai tuần vì lý do cá nhân chính đáng. Người này đang giữ phần việc quan trọng nhất của sprint hiện tại.

**Tham số cố định:**
- Thành viên nghỉ đúng **hai tuần**, tính từ ngày chạy.
- Người nghỉ đang giữ phần việc quan trọng nhất của sprint hiện tại.
- Lý do: cá nhân, chính đáng; phiếu không nêu chi tiết lý do.

**Số liệu:**
- Không có số liệu tra bảng.

**Chỗ cần may đo:**
- Thành viên: người được giao hạng mục chưa xong có thứ tự ưu tiên cao nhất của Sprint 2 trên bảng công việc. Nếu bảng công việc không có thứ tự ưu tiên, lấy hạng mục chưa xong có ước lượng khả năng nhất lớn nhất. Hoà thì chọn bằng băm, ô 1, danh sách mã thành viên xếp A, B, C…
- Liệt kê mọi hạng mục người đó đang giữ và ngày kết thúc dự kiến của sprint.
- Phiếu chỉ là tình huống mô phỏng; việc thành viên có thật sự ngừng làm hai tuần hay không [cần GV xác nhận].

**Điều nhóm phải chứng minh (nguyên văn):** Kế hoạch phân bổ lại công việc; nhận ra rủi ro tập trung tri thức vào một người và có biện pháp giảm.

## SC-04 · Nhà cung cấp tăng giá · đợt 3

**Tình huống khung (nguyên văn):** Dịch vụ bên thứ ba mà dự án phụ thuộc (lưu trữ đám mây, dịch vụ gửi tin, API mô hình AI) thông báo tăng giá gấp đôi từ tháng sau.

**Tham số cố định:**
- Giá dịch vụ tăng đúng **gấp đôi** (×2) từ tháng sau.

**Số liệu:**
- Dịch vụ và khoản chi: cột "Khoản chi bên thứ ba" của bảng tra.
- Chi phí hiện tại của dịch vụ: lấy từ Kế hoạch dự án, Sổ NKQĐ hoặc cột `token_dong` của Sổ Ước lượng (khi dịch vụ là API mô hình AI); ghi rõ nguồn. Chi phí mới = 2 × chi phí hiện tại.

**Chỗ cần may đo:**
- Đề tài có ghi khoản chi bên thứ ba: dùng đúng dịch vụ đó.
- Đề tài ghi "—": chọn bằng băm, ô 1, trong các dịch vụ bên thứ ba mà kho mã đang gọi (tệp cấu hình, tệp khai báo phụ thuộc, biến môi trường mẫu), xếp theo bảng chữ cái. Nếu kho mã không gọi dịch vụ bên thứ ba nào, dừng ô này và ghi [cần GV xác nhận].
- ĐT-B4 không nhận phiếu này.

**Điều nhóm phải chứng minh (nguyên văn):** Tính lại tổng chi phí sở hữu; so chi phí chuyển nhà cung cấp với chi phí ở lại.

## SC-05 · Sức ép cạnh tranh · đợt 2

**Tình huống khung (nguyên văn):** Một sản phẩm cạnh tranh vừa ra mắt tính năng tương tự. Ban lãnh đạo yêu cầu rút ngắn thời gian ra mắt hai tuần, giữ nguyên phạm vi và ngân sách.

**Tham số cố định:**
- Rút ngắn thời gian ra mắt đúng **hai tuần** (14 ngày).
- Giữ nguyên phạm vi và ngân sách.

**Số liệu:**
- Mốc ra mắt hiện tại: Kế hoạch dự án. Mốc mới = mốc cũ − 14 ngày.

**Chỗ cần may đo:**
- Tính năng tương tự của sản phẩm cạnh tranh: chọn bằng băm, ô 1, trong các tính năng người dùng thấy được của sản phẩm (backlog, xếp theo mã hạng mục).
- Liệt kê hạng mục còn lại trong backlog cam kết kèm ước lượng, để nhóm tính phần phải nén.

**Điều nhóm phải chứng minh (nguyên văn):** Nén tiến độ luôn phát sinh chi phí; nhóm cần định lượng và trình bày rõ, không nhận lời khi chưa tính.

## SC-06 · Lỗi kiến trúc · đợt 2

**Tình huống khung (nguyên văn):** Kiểm thử tích hợp phát hiện một quyết định kiến trúc từ Sprint 1 khiến tính năng mới không thể triển khai đúng. Phải sửa lại phần đã được nghiệm thu là hoàn thành.

**Tham số cố định:**
- Quyết định kiến trúc lấy từ **Sprint 1**.
- Phần phải sửa đã được nghiệm thu là hoàn thành.
- Phát hiện qua kiểm thử tích hợp.
- Phiếu gốc không nêu khối lượng phải sửa; tác tử không tự đặt con số [cần GV xác nhận].

**Số liệu:**
- Không có số liệu tra bảng. Khối lượng phải sửa để nhóm tự ước lượng.

**Chỗ cần may đo:**
- Quyết định kiến trúc: chọn bằng băm, ô 1, trong các PR đã merge ở Sprint 1 có chạm mô hình dữ liệu, lược đồ cơ sở dữ liệu, cấu trúc thư mục hoặc giao diện giữa các thành phần, cùng các mục Sổ NKQĐ về kiến trúc (xếp theo ngày).
- Tính năng mới bị chặn: hạng mục Sprint 2 phụ thuộc vào phần đó; nhiều hạng mục thì chọn bằng băm, ô 2.
- Lý do không tương thích phải hợp lý về kỹ thuật với mã thật; ghi rõ đây là tình huống giả định.

**Điều nhóm phải chứng minh (nguyên văn):** Xử lý nợ kỹ thuật như một quyết định có định lượng; báo tin xấu về phần đã tuyên bố là xong.

## SC-07 · Yêu cầu tuân thủ · đợt 2

**Tình huống khung (nguyên văn):** Bộ phận pháp chế yêu cầu bổ sung cơ chế thu thập sự đồng ý, quyền rút lại đồng ý và quyền xoá dữ liệu theo Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 trước khi sản phẩm được đưa ra ngoài.

**Tham số cố định:**
- Bổ sung đủ ba cơ chế: thu thập sự đồng ý, quyền rút lại đồng ý, quyền xoá dữ liệu, theo Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15.
- Phải xong trước khi sản phẩm được đưa ra ngoài.
- Phiếu gốc không nêu hạn bằng ngày cụ thể [cần GV xác nhận].

**Số liệu:**
- Không có số liệu tra bảng.

**Chỗ cần may đo:**
- Liệt kê các trường dữ liệu cá nhân sản phẩm đang thu thập (mô hình dữ liệu, biểu mẫu, lược đồ) và các tính năng chạm tới chúng. Không có lựa chọn ngẫu nhiên.
- Đề tài loại C không nhận phiếu này.

**Điều nhóm phải chứng minh (nguyên văn):** Nghĩa vụ pháp lý phát sinh với dữ liệu cá nhân; yêu cầu tuân thủ không thương lượng được như yêu cầu chức năng.

## SC-08 · Người dùng bác bỏ · đợt 1

**Tình huống khung (nguyên văn):** Buổi thử nghiệm với năm người dùng thật cho thấy tính năng chính mà nhóm đã dồn công sức nhiều nhất bị hiểu sai và gần như không ai dùng được.

**Tham số cố định:**
- Buổi thử nghiệm với đúng **năm** người dùng thật.
- Tính năng bị bác bỏ là tính năng chính nhóm dồn công sức nhiều nhất.
- Kết quả ghi đúng như phiếu gốc: "bị hiểu sai và gần như không ai dùng được"; tác tử không tự đặt tỷ lệ [cần GV xác nhận].

**Số liệu:**
- Không có số liệu tra bảng.

**Chỗ cần may đo:**
- Tính năng: hạng mục (hoặc nhóm hạng mục cùng tính năng) có tổng giờ công đã ghi lớn nhất trong Sổ Ước lượng; nếu Sổ chưa có giờ thực tế, lấy hạng mục Sprint 1 có ước lượng khả năng nhất lớn nhất. Hoà thì chọn bằng băm, ô 1.
- Năm người dùng mô tả theo persona người dùng cuối trong gói ràng buộc. Chỗ hiểu sai mô tả dựa trên luồng giao diện có thật trong mã.

**Điều nhóm phải chứng minh (nguyên văn):** Phân biệt được output và outcome; dám thay đổi hướng đi thay vì bảo vệ công sức đã bỏ ra.

## SC-09 · Mất người chủ chốt · đợt 3

**Tình huống khung (nguyên văn):** Thành viên nắm nhiều hiểu biết nhất về hệ thống rời nhóm ngay lập tức. Phần lớn kiến thức của người này chưa được ghi lại ở đâu.

**Tham số cố định:**
- Thành viên rời nhóm **ngay lập tức** tại ngày chạy.
- Người rời là người nắm nhiều hiểu biết nhất về hệ thống; phần lớn kiến thức chưa được ghi lại.
- Phiếu chỉ là tình huống mô phỏng; việc thành viên có thật sự ngừng làm hay không [cần GV xác nhận].

**Số liệu:**
- Không có số liệu tra bảng.

**Chỗ cần may đo:**
- Thành viên: người đã sửa nhiều tệp khác nhau nhất trên nhánh chính (theo lịch sử commit). Hoà thì chọn bằng băm, ô 1, danh sách mã thành viên xếp A, B, C…
- Liệt kê các thư mục hoặc tệp chỉ người đó từng sửa, và các tài liệu (README, Sổ NKQĐ) có hay không có ghi về phần đó.

**Điều nhóm phải chứng minh (nguyên văn):** Đánh giá thiệt hại thật; kế hoạch phục hồi tri thức; bài học về hệ số xe buýt của nhóm.

## SC-10 · Deadline dời lên · đợt 1

**Tình huống khung (nguyên văn):** Thời gian còn lại bị cắt 30%. Lý do bất khả kháng từ phía khách hàng (sự kiện ra mắt bị dời lên sớm hơn).

**Tham số cố định:**
- Thời gian còn lại bị cắt đúng **30%**.
- Lý do: sự kiện ra mắt của khách hàng bị dời lên sớm hơn.

**Số liệu:**
- Số ngày còn lại = từ ngày chạy đến mốc kết thúc trong Kế hoạch dự án. Mốc mới = ngày chạy + 70% số ngày còn lại, làm tròn xuống ngày.

**Chỗ cần may đo:**
- Không có lựa chọn ngẫu nhiên.
- Liệt kê hạng mục còn lại kèm ước lượng để nhóm cắt phạm vi theo giá trị.

**Điều nhóm phải chứng minh (nguyên văn):** Cắt phạm vi theo giá trị thay vì cắt đều; đàm phán lại cam kết chuyên nghiệp.

## SC-11 · Lỗ hổng bảo mật · đợt 2

**Tình huống khung (nguyên văn):** Một thư viện mà dự án phụ thuộc bị công bố lỗ hổng nghiêm trọng. Bản vá làm thay đổi giao diện lập trình, buộc phải sửa nhiều nơi trong mã nguồn.

**Tham số cố định:**
- Thư viện dự án phụ thuộc trực tiếp bị công bố lỗ hổng nghiêm trọng.
- Bản vá thay đổi giao diện lập trình, buộc sửa nhiều nơi trong mã nguồn.
- Phiếu gốc không nêu thời hạn phải vá [cần GV xác nhận].

**Số liệu:**
- Số nơi phải sửa: đếm số tệp mã nguồn có nhập thư viện đó.

**Chỗ cần may đo:**
- Thư viện: chọn bằng băm, ô 1, trong các phụ thuộc trực tiếp (tệp khai báo phụ thuộc) được nhập ở ít nhất hai tệp mã nguồn, xếp theo bảng chữ cái; nếu không có thư viện nào như vậy, xét mọi phụ thuộc trực tiếp.
- Không gắn mã lỗ hổng có thật (CVE); ghi rõ đây là lỗ hổng giả định.

**Điều nhóm phải chứng minh (nguyên văn):** Rủi ro chuỗi cung ứng phần mềm; đánh giá mức khẩn cấp và lập kế hoạch ứng phó có thời hạn.

## SC-12 · Đảo ngược ưu tiên · đợt 1

**Tình huống khung (nguyên văn):** Khách hàng thay đổi chiến lược. Tính năng nhóm đang dồn sức làm bị hạ xuống mức thấp nhất, một tính năng chưa từng nằm trong backlog được đưa lên cao nhất.

**Tham số cố định:**
- Tính năng đang dồn sức bị hạ xuống mức ưu tiên thấp nhất.
- Một tính năng chưa từng nằm trong backlog được đưa lên cao nhất.
- Lý do: khách hàng thay đổi chiến lược.
- Phiếu gốc không có tham số định lượng [cần GV xác nhận].

**Số liệu:**
- Không có số liệu tra bảng.

**Chỗ cần may đo:**
- Tính năng bị hạ: hạng mục đang làm có giờ công đã ghi lớn nhất trong sprint hiện tại; hoà thì chọn bằng băm, ô 1.
- Tính năng mới: tác tử đề xuất một tính năng hợp với đề tài và mục tiêu của persona, không trùng hạng mục nào trên bảng công việc.

**Điều nhóm phải chứng minh (nguyên văn):** Xử lý thay đổi phạm vi ở mức chiến lược; bảo toàn giá trị đã tạo và đàm phán lại đường cơ sở.

## SC-13 · Tác tử làm hỏng nhánh chính · đợt 1

**Tình huống khung (nguyên văn):** Nhóm phát hiện từ ba ngày trước, tác tử đã commit thẳng năm thay đổi chưa ai đọc vào nhánh chính. Sản phẩm vẫn chạy nhưng không ai biết đã đổi gì.

**Tham số cố định:**
- Sự việc bắt đầu từ đúng **ba ngày** trước ngày chạy.
- Đúng **năm** thay đổi tác tử commit thẳng vào nhánh chính, chưa ai đọc.
- Sản phẩm vẫn chạy; không ai biết đã đổi gì.

**Số liệu:**
- Không có số liệu tra bảng.

**Chỗ cần may đo:**
- Năm tệp bị đổi: lập danh sách tệp mã nguồn trên nhánh chính (không tính tệp cấu hình, tài liệu, tệp dữ liệu), xếp theo bảng chữ cái của đường dẫn; vị trí bắt đầu chọn bằng băm, ô 1; lấy năm tệp liên tiếp, hết danh sách thì quay về đầu.
- Tình huống là giả định: tác tử mô phỏng sự cố **không được sửa, không được commit** vào kho mã.

**Điều nhóm phải chứng minh (nguyên văn):** Quy trình khôi phục và thẩm định lại; chi phí của việc đó; sửa quy tắc để không lặp lại.

## SC-14 · Hoá đơn token gấp bốn · đợt 3

**Tình huống khung (nguyên văn):** Chi phí token tháng này gấp bốn dự toán vì tác tử chạy vòng lặp sửa và thử hàng chục lần trên một hạng mục. Giám đốc tài chính yêu cầu giải trình và đặt trần mới bằng 60% dự toán cũ.

**Tham số cố định:**
- Chi phí token tháng này đúng **gấp bốn** dự toán.
- Trần mới bằng đúng **60%** dự toán cũ.
- Nguyên nhân: tác tử chạy vòng lặp sửa và thử hàng chục lần trên một hạng mục.

**Số liệu:**
- Dự toán token: Kế hoạch dự án hoặc Sổ Ước lượng của nhóm; nếu nhóm không có dự toán riêng, dùng cột "Trần token 5%" của bảng tra. Ghi rõ dùng nguồn nào.
- Hoá đơn = 4 × dự toán. Trần mới = 0,6 × dự toán. Cách quy dự toán cả dự án về một tháng [cần GV xác nhận].

**Chỗ cần may đo:**
- Hạng mục: hạng mục do tác tử thực hiện có số vòng lớn nhất trong cột `vong` của Sổ Ước lượng; hoà thì chọn bằng băm, ô 1.

**Điều nhóm phải chứng minh (nguyên văn):** Mô hình chi phí theo hạng mục; cơ chế kiểm soát (giới hạn vòng, giới hạn ngân sách mỗi phiên); tiêu chí quyết định hạng mục nào làm tay.

## SC-15 · Phân loại theo Luật Trí tuệ nhân tạo · đợt 2

**Tình huống khung (nguyên văn):** Pháp chế yêu cầu nhóm xác định sản phẩm thuộc mức rủi ro nào theo Luật Trí tuệ nhân tạo số 134/2025/QH15 và bổ sung nghĩa vụ tương ứng trước khi ra mắt.

**Tham số cố định:**
- Xác định mức rủi ro theo Luật Trí tuệ nhân tạo số 134/2025/QH15 và bổ sung nghĩa vụ tương ứng trước khi ra mắt.
- Phiếu gốc không có tham số định lượng [cần GV xác nhận].

**Số liệu:**
- Không có số liệu tra bảng.

**Chỗ cần may đo:**
- Liệt kê các tính năng có dùng mô hình AI khi sản phẩm chạy.
- Tác tử không kết luận sản phẩm thuộc mức rủi ro nào; nhóm tra văn bản và tự lập luận.

**Điều nhóm phải chứng minh (nguyên văn):** Phân loại có lập luận, dẫn điều khoản; tác động lên phạm vi, tiến độ, chi phí; nghĩa vụ nào không thương lượng được.

## SC-16 · Nhà cung cấp tác tử đổi điều khoản · đợt 3

**Tình huống khung (nguyên văn):** Công cụ tác tử nhóm đang dùng thông báo từ tháng sau: ngừng bậc miễn phí và bậc giáo dục, và dữ liệu gửi lên được dùng để huấn luyện trừ khi trả gói doanh nghiệp.

**Tham số cố định:**
- Có hiệu lực từ tháng sau.
- Ngừng bậc miễn phí và bậc giáo dục.
- Dữ liệu gửi lên được dùng để huấn luyện, trừ khi trả gói doanh nghiệp.
- Phiếu gốc không nêu giá gói doanh nghiệp [cần GV xác nhận].

**Số liệu:**
- Không có số liệu tra bảng.

**Chỗ cần may đo:**
- Công cụ: công cụ xuất hiện nhiều nhất ở dòng "Tác tử: …" của các PR; hoà thì chọn bằng băm, ô 1.
- Ghi rõ đây là thông báo giả định, không phải thông báo thật của nhà cung cấp.

**Điều nhóm phải chứng minh (nguyên văn):** Rủi ro rò rỉ mã và dữ liệu; chi phí chuyển đổi so với chi phí ở lại; phương án (đổi công cụ, trả tiền, làm tay một phần); tác động tiến độ và đường cơ sở.

## Bảng tra số liệu theo đề tài

Đơn vị: triệu đồng. Dùng cho SC-01, SC-04, SC-14. Cột "20% trần" là mức tối đa của khoản bị cắt ở SC-01; khoản cắt thật tính trên ngân sách còn lại nên nhỏ hơn. Cột "Trần token 5%" bằng 5% trần ngân sách; cột "Gấp bốn" bằng bốn lần trần token.

| Đề tài | Trần ngân sách | 20% trần (SC-01) | Trần token 5% (SC-14) | Gấp bốn (SC-14) | Khoản chi bên thứ ba (SC-04) |
|---|---|---|---|---|---|
| ĐT-A1 | 160 | 32 | 8 | 32 | Ba sàn thương mại điện tử (dịch vụ giả lập), mỗi sàn giới hạn 60 lệnh gọi mỗi phút. |
| ĐT-A2 | 190 | 38 | 9,5 | 38 | Dịch vụ tra cứu thẻ bảo hiểm y tế (giả lập), bên cung cấp không cam kết thời gian trả lời. |
| ĐT-A3 | 210 | 42 | 10,5 | 42 | Gói ký số 5.000 lượt một năm, vượt gói mua bổ sung đơn giá cao hơn 40%; thêm dịch vụ xác thực định danh. |
| ĐT-A4 | 150 | 30 | 7,5 | 30 | API bản đồ công khai có thật, bậc miễn phí 1.000 lệnh gọi mỗi ngày cho cả nhóm. |
| ĐT-B1 | 175 | 35 | 8,75 | 35 | Lưu trữ đám mây: 120 ca một ngày, 3 ảnh một ca, 8 MB một ảnh, giữ tối thiểu 5 năm. Trần vận hành 4 triệu một tháng. |
| ĐT-B2 | 140 | 28 | 7 | 28 | Token mô hình khi sản phẩm chạy thật, dưới 1.500 đồng một lượt hỏi, khoảng 4.000 lượt một tháng. Trần vận hành 6 triệu một tháng. |
| ĐT-B3 | 120 | 24 | 6 | 24 | Tin nhắn SMS khoảng 800 đồng một tin cho 4.200 trẻ. Trần vận hành 3 triệu một tháng. |
| ĐT-B4 | 165 | 33 | 8,25 | 33 | Lưu trữ và truyền dữ liệu video, khoảng 0,5 GB một giờ xem. Không nhận SC-04 vì trùng dữ kiện tuần 9. |
| ĐT-C1 | 260 | 52 | 13 | 52 | — |
| ĐT-C2 | 200 | 40 | 10 | 40 | — |
| ĐT-C3 | 180 | 36 | 9 | 36 | — |
| ĐT-C4 | 220 | 44 | 11 | 44 | — |
| ĐT-D1 | 200 | 40 | 10 | 40 | Chi phí gọi API mô hình, gói ràng buộc ghi là khoản chưa lường trước được. |
| ĐT-D2 | 170 | 34 | 8,5 | 34 | — |
| ĐT-D3 | 210 | 42 | 10,5 | 42 | — |
| ĐT-D4 | 190 | 38 | 9,5 | 38 | Chi phí gọi mô hình, dự kiến chiếm 25% ngân sách, tức 47,5 triệu đồng, và có thể vượt xa. |
| ĐT-E1 | 150 | 30 | 7,5 | 30 | — |
| ĐT-E2 | 230 | 46 | 11,5 | 46 | Đơn vị thanh toán là bên liên quan của đề tài; gói ràng buộc không nêu đơn giá. |
| ĐT-E3 | 110 | 22 | 5,5 | 22 | Đề tài buộc cân nhắc giữa tự làm và dùng dịch vụ có sẵn; gói ràng buộc không nêu đơn giá. |
| ĐT-E4 | 170 | 34 | 8,5 | 34 | — |

Dấu "—": gói ràng buộc không nêu khoản chi bên thứ ba. Ngân sách là con số giả định để thực hành; nhóm không chi tiền thật.
