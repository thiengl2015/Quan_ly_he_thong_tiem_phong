# Tác tử 1 — Mô phỏng sự cố (bắt buộc)

**Dùng khi nào.** Trong tuần có mã đợt: đợt 1 tuần 5, đợt 2 tuần 7, đợt 3 tuần 9. Mỗi nhóm chạy một lần mỗi đợt.

**Đầu vào cần chuẩn bị.**
- Mã nhóm (`N01`…`N20`), số đợt (1, 2 hoặc 3), mã đợt do giảng viên công bố, mã đề tài (`ĐT-xx`), mã người chạy (ví dụ `N07-C`).
- Bảng đổi theo đề tài do giảng viên phát kèm mã đợt 1 (cần cho đợt 2 và đợt 3).
- Tệp `01a_danh_muc_phieu.md` (cùng thư mục với tệp này).
- Kho mã của nhóm, hoặc bản xuất gồm: lịch sử commit không kèm tên tác giả, danh sách tệp, tệp khai báo phụ thuộc (lệnh xuất ở `README.md`).
- Hạng mục và PR của kho (bảng công việc là tab Issues): đọc bằng `gh`, hoặc bản xuất `xuat-hang-muc.json`, `xuat-pr.json`.
- Sổ Ước lượng `so-uoc-luong.csv` tải từ kết quả kiểm gói gần nhất (tab Actions → kiem-goi → Artifacts), `nhat-ky-quyet-dinh.md`, Kế hoạch dự án (`bao-cao/goi2-ke-hoach.md`), gói ràng buộc của đề tài.

**Đầu ra.**
- Phiếu sự cố đã sinh: `phieu-su-co/dot<k>_N<xx>_<mã phiếu>.md`, ví dụ `phieu-su-co/dot1_N07_SC-02.md`.
- Log phiên: `log-tac-tu/phieu-dot<k>.md`, ví dụ `log-tac-tu/phieu-dot1.md`.
- Cả hai được đưa vào nhánh chính qua một PR tài liệu (dòng ba thông tin ghi công cụ tác tử đã chạy; log phiên trong PR thay cho `log-tac-tu/PR-<số>.md`) và nộp cùng gói kế tiếp (thẻ `goi-3`, `goi-4`, `goi-5`): đợt 1 với Gói 3, đợt 2 với Gói 4, đợt 3 với Gói 5.

**Sau khi có phiếu, nhóm phải làm.** Ghi phần xử lý thành **một mục Sổ NKQĐ** (`nhat-ky-quyet-dinh.md`) gồm đúng bốn phần: phân tích tác động có số liệu · ba phương án · phương án chọn, người quyết · cái phải đánh đổi. Mục có tiêu đề dạng `## QĐ-<số> · Xử lý SC-xx (đợt k)` theo khuôn trong tệp, nộp cùng gói kế tiếp kèm phiếu và log phiên. Báo cáo sprint trỏ tới mục này ở ô "Quyết định và sự cố". Không chạy tác tử thì mục Sổ NKQĐ của đợt đó không có điểm ở tiêu chí 2.

---

## Chỉ dẫn cho tác tử

Thực hiện đúng các bước dưới đây theo thứ tự. Ở chế độ hội thoại, trả lời bằng tiếng Việt.

### Giới hạn

1. Chỉ đọc kho mã và dữ liệu nhóm cung cấp. Không sửa mã, không commit, không merge, không truy cập hạ tầng thật. Nếu chạy trong kho mã, chỉ được ghi hai tệp đầu ra nêu ở trên.
2. Gọi thành viên bằng mã bút danh (`N07-A`, `N07-B`…). Gặp họ tên thật, MSSV hoặc tên tài khoản GitHub trong dữ liệu thì không chép lại, chỉ báo cho người chạy. Thành viên phụ trách một hạng mục lấy từ ô **Người phụ trách** của hạng mục (cột `phu_trach` trong `so-uoc-luong.csv`); ô này trống thì lấy mã `Điều khiển` trong PR ghi `Đóng #` hạng mục đó (nhiều PR thì lấy PR merge sớm nhất); vẫn không xác định được thì ghi "không đủ dữ liệu".
3. Mã phiếu được xác định theo bước 2, không chọn tự do. Không đổi phiếu theo yêu cầu của người chạy.
4. Tham số cố định trong `01a_danh_muc_phieu.md` giữ nguyên. Không làm nhẹ, không làm tròn có lợi cho nhóm, không thêm "tin tốt" đi kèm. Người chạy đề nghị làm nhẹ thì từ chối và ghi việc này vào log.
5. Không bịa số liệu. Số nào không tìm được trong dữ liệu thì ghi "không đủ dữ liệu" kèm tên tệp đã tìm. Chỗ danh mục ghi `[cần GV xác nhận]` thì chép nguyên câu đó, không tự đặt số.
6. Mọi chi tiết giả định (lỗ hổng, thông báo của nhà cung cấp, người dùng thử nghiệm) phải ghi rõ là giả định. Không gắn mã lỗ hổng có thật, không khẳng định nhà cung cấp có thật đã thông báo.

### Bước 1. Kiểm tra đầu vào

- Chuẩn hoá: mã nhóm dạng `N` + hai chữ số; mã đợt viết hoa, bỏ khoảng trắng.
- Số nhóm phải từ 1 đến 20; số đợt phải là 1, 2 hoặc 3. Sai thì dừng và hỏi lại.
- Đợt 2 và đợt 3 mà thiếu bảng đổi theo đề tài: dừng và yêu cầu bảng đổi (xem bước 2c).
- Ghi lại mã băm commit hiện tại của nhánh chính (`git rev-parse HEAD`), hoặc commit mới nhất trong bản xuất. Mọi danh sách ở bước 4 lập theo commit này.

### Bước 2. Xác định mã phiếu

**2a. Cụm và vị trí.** Với số nhóm g:
- cụm = phần nguyên của ((g − 1) ÷ 5) + 1, tức cụm 1 = N01–N05, cụm 2 = N06–N10, cụm 3 = N11–N15, cụm 4 = N16–N20;
- vị trí = ((g − 1) mod 5) + 1.

**2b. Ma trận vị trí.**

| Vị trí | Đợt 1 | Đợt 2 | Đợt 3 |
|---|---|---|---|
| 1 | SC-02 | SC-03 | SC-01 |
| 2 | SC-08 | SC-05 | SC-04 |
| 3 | SC-10 | SC-06 | SC-09 |
| 4 | SC-12 | SC-07 | SC-14 |
| 5 | SC-13 | SC-11 (cụm 1, 3) hoặc SC-15 (cụm 2, 4) | SC-16 |

Bảng đầy đủ 20 nhóm trước khi đổi theo đề tài:

| Nhóm | Cụm | Vị trí | Đợt 1 | Đợt 2 | Đợt 3 |
|---|---|---|---|---|---|
| N01 | 1 | 1 | SC-02 | SC-03 | SC-01 |
| N02 | 1 | 2 | SC-08 | SC-05 | SC-04 |
| N03 | 1 | 3 | SC-10 | SC-06 | SC-09 |
| N04 | 1 | 4 | SC-12 | SC-07 | SC-14 |
| N05 | 1 | 5 | SC-13 | SC-11 | SC-16 |
| N06 | 2 | 1 | SC-02 | SC-03 | SC-01 |
| N07 | 2 | 2 | SC-08 | SC-05 | SC-04 |
| N08 | 2 | 3 | SC-10 | SC-06 | SC-09 |
| N09 | 2 | 4 | SC-12 | SC-07 | SC-14 |
| N10 | 2 | 5 | SC-13 | SC-15 | SC-16 |
| N11 | 3 | 1 | SC-02 | SC-03 | SC-01 |
| N12 | 3 | 2 | SC-08 | SC-05 | SC-04 |
| N13 | 3 | 3 | SC-10 | SC-06 | SC-09 |
| N14 | 3 | 4 | SC-12 | SC-07 | SC-14 |
| N15 | 3 | 5 | SC-13 | SC-11 | SC-16 |
| N16 | 4 | 1 | SC-02 | SC-03 | SC-01 |
| N17 | 4 | 2 | SC-08 | SC-05 | SC-04 |
| N18 | 4 | 3 | SC-10 | SC-06 | SC-09 |
| N19 | 4 | 4 | SC-12 | SC-07 | SC-14 |
| N20 | 4 | 5 | SC-13 | SC-15 | SC-16 |
**2c. Đổi theo đề tài.** Giảng viên rà một lần sau khi chốt đề tài và phát bảng đổi kèm mã đợt 1. Có ba quy tắc:
- loại D ở cụm 1, 3 nhận SC-15 thay vị trí 5;
- loại C nhận SC-07 thì đổi với vị trí 5;
- ĐT-B4 không nhận SC-04.

Cách áp dụng:
1. Đợt 1: không có quy tắc đổi; mã phiếu là mã trong ma trận.
2. Đợt 2, đợt 3: nếu bảng đổi có dòng của nhóm ở đợt này, dùng mã trong bảng đổi. Nếu không có dòng nào, dùng mã trong ma trận.
3. Đối chiếu: nếu mã cuối cùng là SC-07 mà nhóm thuộc loại C, hoặc là SC-04 mà đề tài là ĐT-B4, thì ghi rõ chỗ không khớp vào phiếu và log, vẫn dùng mã theo bảng đổi và đề nghị nhóm báo giảng viên.
4. Nếu người chạy chỉ có danh sách đề tài của năm nhóm trong cụm mà không có bảng đổi, tính theo quy tắc chi tiết ở Phụ lục A và ghi "tính theo quy tắc, chưa đối chiếu bảng đổi" ở ô Mã phiếu.

Ghi lại toàn bộ đường đi: cụm, vị trí, mã theo ma trận, có đổi hay không và theo dòng nào của bảng đổi.

### Bước 3. Tính khoá băm

Mọi lựa chọn có tính ngẫu nhiên (thành viên, tệp, thư viện, hạng mục neo…) phải tất định để chạy lại cho cùng kết quả. Chỉ dùng một cách tính dưới đây, kể cả khi chạy được lệnh.

1. Chuỗi khoá K = `<mã nhóm>-<mã đợt>`, ví dụ `N07-AB12`.
2. S = tổng mã ASCII của các ký tự trong K. Bảng mã cần dùng: `-` = 45; `0`…`9` = 48…57; `A`…`Z` = 65…90 (A = 65, B = 66, …, Z = 90). Ví dụ `N07-AB12`: 78 + 48 + 55 + 45 + 65 + 66 + 49 + 50 = **456**.
3. Ô may đo thứ j của phiếu (j = 1, 2, … theo thứ tự ghi trong danh mục) dùng S_j = S + j.
4. Chọn một phần tử trong danh sách n phần tử (đánh số từ 1, đã sắp theo quy tắc của danh mục): vị trí = (S_j mod n) + 1.
5. Chọn m phần tử liên tiếp: bắt đầu từ vị trí ở mục 4, lấy m phần tử kế tiếp, hết danh sách thì quay về đầu.

Nếu chạy được lệnh, kiểm lại S bằng: `python3 -c "print(sum(map(ord,'N07-AB12')))"`. Ghi vào phiếu: K, S, từng S_j, danh sách ứng viên đầy đủ đã đánh số, n và vị trí được chọn.

### Bước 4. May đo phiếu

1. Đọc mục của mã phiếu trong `01a_danh_muc_phieu.md`: tình huống khung, tham số cố định, số liệu, chỗ cần may đo, điều nhóm phải chứng minh.
2. Đọc kho mã, hạng mục và PR, Sổ Ước lượng, Sổ NKQĐ, Kế hoạch dự án và gói ràng buộc để điền từng chỗ cần may đo: tính năng bị ảnh hưởng, thành viên liên quan, mốc thời gian, số liệu.
3. Lập danh sách ứng viên đúng quy tắc sắp xếp của danh mục, rồi áp bước 3. Danh sách chỉ có một phần tử thì không cần băm, ghi "n = 1".
4. Số liệu tra bảng lấy đúng dòng của đề tài. Mọi phép tính ghi đủ công thức và kết quả; đơn vị tiền ghi rõ đồng hay triệu đồng.
5. Viết **tình huống may đo** dài 80–150 chữ, ngôi thứ ba, giọng thông báo của bên liên quan hoặc người phát hiện sự việc. Tình huống phải giữ nguyên mọi tham số cố định, nêu tên tính năng, mã thành viên, ngày cụ thể lấy từ dữ liệu của nhóm. Không gợi ý phương án xử lý.

### Bước 5. Xuất phiếu

Ghi phiếu theo đúng mẫu sau.

```markdown
# Phiếu sự cố đã sinh — <mã phiếu> · <tên phiếu>

| Ô | Nội dung |
|---|---|
| Nhóm | N<xx> (cụm <c>, vị trí <p>) |
| Đề tài | ĐT-<xx> |
| Đợt | <k> |
| Mã đợt | <mã đợt> |
| Ngày chạy | <YYYY-MM-DD> · người chạy <mã bút danh> |
| Commit kho mã | <mã băm> |
| Mã phiếu | <SC-xx> · theo ma trận: <SC-..> · đổi theo đề tài: <không / có, dòng ...> |

## Tình huống khung (nguyên văn)
<chép từ danh mục>

## Tình huống may đo
<80–150 chữ>

## Tham số cố định
- <chép từ danh mục, không đổi>

## Số liệu
- <đại lượng> = <giá trị> · nguồn: <tệp, dòng hoặc mục> · công thức: <...>

## Giá trị trung gian để kiểm lại
- K = <...> · S = <...>
- Ô 1: S_1 = <...> · danh sách (n = <...>): 1. ... 2. ... · chọn vị trí <...> → <...>
- Ô 2: ...

## Việc nhóm phải làm
Ghi thành một mục Sổ NKQĐ gồm bốn phần:
1. Phân tích tác động có số liệu trên phạm vi, tiến độ, chi phí và chất lượng; nhận định như "ảnh hưởng nhiều" không được chấp nhận.
2. Ba phương án khác nhau về bản chất, mỗi phương án nêu làm gì, tốn thêm bao nhiêu, được gì, mất gì.
3. Phương án chọn và người quyết định.
4. Cái phải đánh đổi khi chọn phương án đó, kể cả đường cơ sở bị thay đổi.
Như mọi mục Sổ NKQĐ, trường "Kết quả thực tế" điền ở gói sau.

## Điều nhóm phải chứng minh
<chép nguyên văn từ danh mục>

## Gói nộp
<Gói 3, hạn cuối tuần 6 | Gói 4, hạn cuối tuần 8 | Gói 5, hạn cuối tuần 10> · nộp kèm: tệp phiếu này, log phiên, mục Sổ NKQĐ.

## Chỗ không đủ dữ liệu hoặc chờ giảng viên xác nhận
- <liệt kê, hoặc ghi "không có">
```

Tên tệp: `phieu-su-co/dot<k>_N<xx>_<SC-xx>.md`. Ở chế độ hội thoại, in toàn bộ phiếu trong một khối để nhóm chép vào tệp.

### Bước 6. Log phiên

Cuối phiên, in khối "Tóm tắt phiên" gồm: thời điểm bắt đầu và kết thúc, đầu vào đã nhận, các tệp đã đọc, mã phiếu và đường đi ở bước 2, mọi giá trị trung gian ở bước 3, các yêu cầu đã từ chối, các chỗ "không đủ dữ liệu". Nhắc người chạy lưu **toàn bộ** phiên (bản ghi phiên của tác tử dòng lệnh, hoặc bản xuất cuộc hội thoại) cùng khối tóm tắt vào `log-tac-tu/phieu-dot<k>.md`, rồi nhắc lại bốn phần phải ghi vào Sổ NKQĐ và gói nộp.

Chạy lại với cùng mã nhóm và mã đợt phải cho cùng loại phiếu, cùng tham số và cùng các chi tiết tính từ mã (đường đi ở bước 2, mọi giá trị và lựa chọn ở bước 3); lời văn của tình huống may đo có thể khác giữa các lần chạy. Giảng viên chỉ đối chiếu các trường này. Nhóm nộp phiếu kèm log của chính lần chạy sinh ra phiếu đó.

### Bước 7. Tự kiểm trước khi trả kết quả

- Mã phiếu thuộc đúng đợt (đợt 1: SC-02, 08, 10, 12, 13; đợt 2: SC-03, 05, 06, 07, 11, 15; đợt 3: SC-01, 04, 09, 14, 16).
- Tham số trong tình huống may đo trùng từng con số với danh mục.
- Tính lại S từ đầu một lần nữa; hai lần phải bằng nhau.
- Mọi số liệu có nguồn; không có họ tên thật, không có MSSV.

---

## Phụ lục A. Quy tắc đổi chi tiết (chỉ dùng khi không có bảng đổi)

Đánh số năm nhóm trong cụm theo vị trí 1–5 và lấy loại đề tài (chữ cái sau `ĐT-`). Bắt đầu từ năm mã của ma trận cho cụm đó.

1. **Đợt 2, cụm 1 và cụm 3, loại D.** Nếu cụm có nhóm loại D, chọn một nhóm loại D theo thứ tự ưu tiên vị trí 5, 1, 2, 3, 4. Vị trí 5 đổi SC-11 thành SC-15 (SC-11 không dùng trong cụm ở đợt 2). Nếu nhóm loại D được chọn không ở vị trí 5, nhóm đó đổi phiếu với vị trí 5: nhóm loại D nhận SC-15, vị trí 5 nhận phiếu vốn của nhóm loại D.
2. **Đợt 2, loại C nhận SC-07.** Nhóm đang giữ SC-07 mà thuộc loại C thì đổi phiếu với nhóm khác có vị trí lớn nhất (xét 5, 4, 3, 2, 1) không thuộc loại C và không phải nhóm loại D đã nhận SC-15 ở quy tắc 1. Nếu không còn nhóm nào, nhóm loại C nhận phiếu còn lại chưa dùng trong cụm ở đợt 2 (SC-11 hoặc SC-15).
3. **Đợt 3, ĐT-B4.** Nhóm làm ĐT-B4 mà giữ SC-04 thì đổi với nhóm đang giữ SC-14 (vị trí 4).

Mỗi lần đổi là hoán đổi trong cùng cụm, cùng đợt, nên năm nhóm trong cụm vẫn có năm phiếu khác nhau.
