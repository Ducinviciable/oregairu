# Template Workflow Dịch Route Mới

Tài liệu này là template chuẩn để dịch bất kỳ route nào của game bằng bộ tool trong `tools/`.

## 1. Chuẩn Bị

Xác định 4 đường dẫn trước khi làm việc:

- `INPUT_RPY`: file route gốc cần dịch, ví dụ `game/scripts/E4/E4_IRO.rpy`
- `OUTPUT_CSV`: file CSV sẽ chứa danh sách câu cần dịch (có được khi chạy `extract_text.py`), ví dụ `tools/E4_IRO.csv`
- `MANUAL_RPY`: file translation thủ công hiện có ( hoặc không có), nếu route đã có sẵn một phần dịch.
- `OUTPUT_AUTO_RPY`: file `.rpy` tự sinh từ CSV (không cần quan tâm vì generator sẽ tự sinh nhưng có thể đặt tên khác) .

? Ví dụ giả sử route mới tên là `NEW_ROUTE`:

- `INPUT_RPY = game/scripts/NEW_ROUTE/NEW_ROUTE.rpy`
- `OUTPUT_CSV = tools/NEW_ROUTE.csv`
- `MANUAL_RPY = game/scripts/NEW_ROUTE/NEW_ROUTE_vietnamese.rpy`
- `OUTPUT_AUTO_RPY = game/scripts/NEW_ROUTE/NEW_ROUTE_vietnamese_AUTO.rpy`

## 2. Trích Xuất Text Sang CSV

Chạy lệnh:

```bash
python tools/extract_text.py --input game/scripts/NEW_ROUTE/NEW_ROUTE.rpy --output tools/NEW_ROUTE.csv
```

Kết quả:

- File CSV được tạo ra tại `tools/NEW_ROUTE.csv`.
- CSV có 4 cột:
  - `line_number`
  - `character`
  - `original`
  - `vietnamese`

## 3. Dịch CSV

Mở `tools/NEW_ROUTE.csv` bằng Excel, LibreOffice Calc, Google Sheets hoặc VS Code.

Điền bản dịch vào cột `vietnamese`.

Quy tắc quan trọng:

- Giữ nguyên tên nhân vật trong cột `character`.
- Giữ nguyên tag Ren'Py như `{size=35}`, `{/size}`, `{i}`, `{b}`.
- Nếu câu có dấu ngoặc kép, hãy để CSV xử lý theo chuẩn; không tự chèn backslash vào file CSV.
- Nếu dòng nào là fragment lỗi hoặc sprite tag không thể khôi phục chắc chắn, để trống hoặc ghi chú riêng rồi xử lý sau.

## 4. Sinh File `.rpy`

Chạy:

```bash
python tools/generate_translation.py --csv tools/NEW_ROUTE.csv --output game/scripts/NEW_ROUTE/NEW_ROUTE_vietnamese_AUTO.rpy --manual-rpy game/scripts/NEW_ROUTE/NEW_ROUTE_vietnamese.rpy
```

Lưu ý:

- Nếu có file `MANUAL_RPY`, generator sẽ tự bỏ qua các `old` string đã tồn tại trong file này để tránh lỗi translation trùng.
- Nếu route chưa có file thủ công, có thể bỏ `--manual-rpy`.
- Nếu muốn giữ cả string trùng với file thủ công, thêm `--include-existing-manual`.

Ví dụ khi route chưa có file thủ công:

```bash
python tools/generate_translation.py --csv tools/NEW_ROUTE.csv --output game/scripts/NEW_ROUTE/NEW_ROUTE_vietnamese_AUTO.rpy
```

## 5. Kiểm Tra Coverage

Chạy:

```bash
python tools/report_cleanup_coverage.py --source game/scripts/NEW_ROUTE/NEW_ROUTE.rpy --translation game/scripts/NEW_ROUTE/NEW_ROUTE_vietnamese_AUTO.rpy
```

Báo cáo sẽ cho biết:

- Tổng số dòng thoại được nhận diện.
- Số dòng translation đang active trong file AUTO.
- Số placeholder/comment còn lại.

Nếu dòng nào chứa markup Ren'Py như `{size=...}` thì báo cáo hiện tại sẽ không coi đó là placeholder chỉ vì có tag định dạng.

## 6. Kiểm Tra Parser

Chạy:

```bash
python tools/game_test.py
```

Script này sẽ quét toàn bộ file `.rpy` trong thư mục `game/` và báo lỗi nếu:

- Thiếu `strings` trong block `translate`.
- Có `old` mà chưa có `new`.
- Có lỗi cú pháp quote cơ bản.

## 7. Chạy Game

Sau khi test xong:

1. Chạy game bằng file bootstrap của dự án.
2. Vào Settings.
3. Chọn Language -> Vietnamese.
4. Mở route vừa dịch và kiểm tra hiển thị thực tế.

## 8. Lệnh Từ Đầu Tới Cuối

Đây là chuỗi lệnh mẫu hoàn chỉnh cho một route mới:

```bash
python tools/extract_text.py --input game/scripts/NEW_ROUTE/NEW_ROUTE.rpy --output tools/NEW_ROUTE.csv
python tools/generate_translation.py --csv tools/NEW_ROUTE.csv --output game/scripts/NEW_ROUTE/NEW_ROUTE_vietnamese_AUTO.rpy --manual-rpy game/scripts/NEW_ROUTE/NEW_ROUTE_vietnamese.rpy
python tools/report_cleanup_coverage.py --source game/scripts/NEW_ROUTE/NEW_ROUTE.rpy --translation game/scripts/NEW_ROUTE/NEW_ROUTE_vietnamese_AUTO.rpy
python tools/game_test.py
```

## 9. Mẫu Đổi Input/Output Nhanh

Nếu route khác có tên `CHAPTER_02`, chỉ cần đổi các đường dẫn:

```bash
python tools/extract_text.py --input game/scripts/CHAPTER_02/CHAPTER_02.rpy --output tools/CHAPTER_02.csv
python tools/generate_translation.py --csv tools/CHAPTER_02.csv --output game/scripts/CHAPTER_02/CHAPTER_02_vietnamese_AUTO.rpy --manual-rpy game/scripts/CHAPTER_02/CHAPTER_02_vietnamese.rpy
python tools/report_cleanup_coverage.py --source game/scripts/CHAPTER_02/CHAPTER_02.rpy --translation game/scripts/CHAPTER_02/CHAPTER_02_vietnamese_AUTO.rpy
```

## 10. Ghi Nhớ Khi Dịch

- Không sửa logic game, chỉ xử lý nội dung dịch.
- Không đổi cấu trúc tag Ren'Py.
- Không tự đoán những fragment không rõ nghĩa.
- Nếu gặp dòng đã dịch trong file thủ công, để generator xử lý tránh trùng lặp.
- Kiểm tra file AUTO được sinh ra tránh lỗi dấu câu \" hoặc duplicate `old`.
- Luôn test kỹ sau khi sinh file dịch mới.
