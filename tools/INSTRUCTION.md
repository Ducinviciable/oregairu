# Hướng Dẫn Dịch Tiếng Việt

Tài liệu này mô tả workflow chung để dịch bất kỳ route nào của game bằng bộ tool trong thư mục `tools/`.

## Mục Tiêu

- Trích xuất thoại từ một file route `.rpy` sang CSV.
- Dịch cột `vietnamese` trong CSV.
- Sinh lại file `translate ... strings:` của Ren'Py từ CSV.
- Kiểm tra coverage và parser trước khi chạy game.

## Bộ Tool Hiện Tại

- `tools/extract_text.py`: trích xuất thoại từ file `.rpy` sang CSV.
- `tools/generate_translation.py`: sinh file `.rpy` dịch từ CSV.
- `tools/report_cleanup_coverage.py`: báo cáo số dòng dịch, dòng placeholder và các mục bị gắn cờ.
- `tools/game_test.py`: kiểm tra cú pháp cơ bản của toàn bộ file `.rpy` trong `game/`.

## Quy Trình Dịch Một Route Mới

### 1. Trích xuất thoại

Ví dụ:

```bash
python tools/extract_text.py --input game/scripts/E4/E4_IRO.rpy --output tools/MY_ROUTE.csv
```

Kết quả là một file CSV với các cột:

- `line_number`
- `character`
- `original`
- `vietnamese`

### 2. Dịch CSV

Mở file CSV trong Excel, LibreOffice Calc, Google Sheets hoặc VS Code và điền cột `vietnamese`.

Lưu ý khi dịch:

- Giữ nguyên tên nhân vật.
- Giữ nguyên tag Ren'Py như `{size=35}`, `{/size}`, `{i}`, `{b}`.
- Không tự thêm backslash trước dấu ngoặc kép trong CSV; CSV sẽ xử lý chuẩn bằng dấu `""` ở mức file.

### 3. Sinh file `.rpy`

Ví dụ:

```bash
python tools/generate_translation.py --csv tools/MY_ROUTE.csv --output game/scripts/MY_ROUTE_vietnamese_AUTO.rpy
```

Nếu đã có file dịch thủ công `*_vietnamese.rpy` cùng route, tool sẽ tự bỏ qua các `old` string đã tồn tại để tránh lỗi trùng translation.

### 4. Kiểm tra coverage

Ví dụ:

```bash
python tools/report_cleanup_coverage.py --source game/scripts/E4/E4_IRO.rpy --translation game/scripts/E4/E4_IRO_vietnamese_AUTO.rpy
```

Tool này sẽ báo:

- Tổng số dòng thoại được nhận diện
- Số dòng translation đang active trong file `.rpy`
- Số placeholder/comment còn lại

### 5. Kiểm tra parser

Chạy:

```bash
python tools/game_test.py
```

Nếu có lỗi Ren'Py như thiếu dấu `"`, duplicate `old`, hoặc block translation chưa khép đúng, script sẽ báo ngay.

## Quy Tắc Dịch

- Giữ văn phong tự nhiên, nhất quán.
- Không đổi ý nghĩa của câu gốc khi gặp câu đùa hoặc câu ngắn.
- Tag Ren'Py phải giữ nguyên thứ tự và cấu trúc.
- Nếu gặp dòng lỗi hoặc fragment ngắn không thể khôi phục chắc chắn, hãy để lại comment và ghi chú thay vì đoán.

## Xử Lý Lỗi Thường Gặp

### 1. Lỗi parse vì dấu `"`

Nguyên nhân thường do CSV chứa chuỗi chưa được quote đúng cách hoặc file `.rpy` bị sinh ra với escape không chuẩn.

Khắc phục:

- Sửa CSV ở nguồn.
- Chạy lại `generate_translation.py`.
- Chạy lại `game_test.py`.

### 2. Duplicate translation

Nếu Ren'Py báo một `old` đã tồn tại, nghĩa là string đó đã có trong file `*_vietnamese.rpy` thủ công.

Khắc phục:

- Để generator tự skip file thủ công như hiện tại.
- Hoặc xoá/bỏ translation trùng ở một trong hai file.

### 3. Placeholder có tag Ren'Py

Nếu một dòng chứa `{size=...}` hoặc tag tương tự, tool báo cáo mới sẽ không coi đó là placeholder chỉ vì có formatting tag.

## Khuyến Nghị Cho Route Mới

Khi bắt đầu route mới, dùng thứ tự sau:

1. Chạy `extract_text.py` với `--input` và `--output` của route mới.
2. Dịch CSV.
3. Chạy `generate_translation.py` với `--csv` và `--output` của route mới.
4. Chạy `report_cleanup_coverage.py` với `--source` và `--translation` tương ứng.
5. Chạy `game_test.py`.

## Ghi Chú

- Bộ tool này không phụ thuộc vào Iroha. Chỉ cần đổi đường dẫn input/output là dùng được cho route khác.
- Nếu route mới có cấu trúc speaker đặc biệt hoặc script phức tạp hơn, nên rà lại phần trích xuất thoại trước khi dịch hàng loạt.
