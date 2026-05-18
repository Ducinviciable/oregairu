# 📖 Hướng Dẫn Dịch Route Iroha Sang Tiếng Việt

## 🎯 Trạng Thái Hiện Tại

- ✅ File script Iroha Route đã giải nén: `game/scripts/E4/E4_IRO.rpy`
- ✅ File translation tạo sẵn: `game/scripts/E4/E4_IRO_vietnamese.rpy`
- 🔄 Cần hoàn thành việc dịch phần còn lại

---

## 📋 Cách Sử Dụng File Dịch

### **Phương Pháp 1: Sử Dụng File Translation Overlay (Khuyến Nghị)**

1. **Mở file dịch**:

   ```
   game/scripts/E4/E4_IRO_vietnamese.rpy
   ```

2. **Cấu trúc file dịch**:

   ```renpy
   translate vietnamese strings:
       old "English text"
       new "Tiếng Việt"
   ```

3. **Thêm vào `game/script.rpy`**:

   ```renpy
   init python:
       renpy.languages["Vietnamese"] = "Tiếng Việt"
   ```

4. **Chọn ngôn ngữ trong game settings**

---

## 🔧 Cách Dịch Phần Còn Lại

### **Bước 1: Mở File E4_IRO.rpy**

- Tìm tất cả các dialogue (hội thoại)
- Mỗi dòng hội thoại có format:
  ```
  character "English text"
  ```

### **Bước 2: Dịch và Thêm Vào File Translation**

```renpy
translate vietnamese strings:
    old "Original English"
    new "Bản dịch Tiếng Việt"
```

### **Bước 3: Để Ý Các Element Đặc Biệt**

- **Tên nhân vật**: `iroha`, `hachiman`, `yukino` → giữ nguyên
- **Thẻ text**: `{size=35}`, `{/size}` → giữ nguyên
- **Dấu ngoặc**: `[...]`, `(...)` → dịch text trong ngoặc

---

## 💡 Ví Dụ Dịch

**Input (tiếng Anh):**

```
iroha "Now then, senpai. Let's go shopping!"
```

**Output (Tiếng Việt):**

```renpy
translate vietnamese strings:
    old "Now then, senpai. Let's go shopping!"
    new "Thế thì, tiền bối ơi. Chúng ta đi mua sắm nào!"
```

---

## 📊 Tổng Quát Route Iroha

| Label       | Nội Dung                    | Trạng Thái   |
| ----------- | --------------------------- | ------------ |
| `E4_IRO_01` | Đi mua sắm - Chọn lựa       | ✅ 30%       |
| `E4_IRO_02` | Làm socola - Tasting        | ⏳ Chưa dịch |
| `E4_IRO_03` | Kết thúc tốt (Socola Iroha) | ⏳ Chưa dịch |
| `E4_IRO_04` | Kết thúc Orimoto            | ⏳ Chưa dịch |
| `E4_IRO_05` | Cảnh Đại học                | ⏳ Chưa dịch |
| `E4_IRO_06` | Hậu trường                  | ⏳ Chưa dịch |

---

## 🚀 Phương Pháp B: Dịch Bằng Python Script (✨ Khuyến Nghị)

### **Bước 1: Trích xuất text từ file .rpy**

```bash
python3 extract_text.py
```

**Kết quả**: File `DICH_IROHA_ROUTE.csv` sẽ được tạo ra chứa tất cả text cần dịch

### **Bước 2: Mở CSV file và dịch**

1. Mở file: `DICH_IROHA_ROUTE.csv`
2. Mỗi dòng có cấu trúc:
   - `line_number`: Số dòng trong file gốc
   - `character`: Tên nhân vật
   - `original`: Text tiếng Anh
   - `vietnamese`: **← Điền bản dịch ở đây**

3. **Cách mở CSV**:
   - **Excel/LibreOffice Calc** (dễ nhất)
   - **VSCode** với extension: Rainbow CSV
   - **Google Sheets** (online)

### **Bước 3: Generate file dịch .rpy tự động**

Khi đã dịch xong CSV, chạy:

```bash
python3 generate_translation.py
```

**Kết quả**: File `game/scripts/E4/E4_IRO_vietnamese_AUTO.rpy` sẽ được tạo ra tự động

### **Bước 4: Test Game**

1. Chạy game
2. Vào Settings → Language → Vietnamese
3. Chọn route Iroha
4. Kiểm tra dịch

---

## 📋 Template CSV Mẫu

File `DICH_IROHA_ROUTE_TEMPLATE.csv` chứa 20 dòng mẫu để bạn tham khảo cách dịch.

| line_number | character | original                            | vietnamese                                    |
| ----------- | --------- | ----------------------------------- | --------------------------------------------- |
| 8           | iroha     | Now then senpai. Let's go shopping! | Thế thì tiền bối ơi. Chúng ta đi mua sắm nào! |
| 9           | hachiman  | Eh? Right now?                      | Hả? Bây giờ à?                                |
| ...         | ...       | ...                                 | ...                                           |

---

## 🎯 Quy Trình Dịch (Tóm Tắt)

```
1️⃣ Chạy extract_text.py
         ↓
2️⃣ Mở DICH_IROHA_ROUTE.csv
         ↓
3️⃣ Dịch tất cả cột 'vietnamese'
         ↓
4️⃣ Chạy generate_translation.py
         ↓
5️⃣ Copy file .rpy vào game/scripts/E4/
         ↓
6️⃣ Test game với Tiếng Việt ✅
```

---

## 💻 Yêu Cầu Hệ Thống

- Python 3.6+ (đã có sẵn trong Ren'Py)
- Không cần cài thêm library nào

---

## 🎓 Ví Dụ Dịch CSV

**Original (tiếng Anh)**:

```
iroha,Now then senpai. Let's go shopping!
hachiman,Eh? Right now?
iroha,We have to pick a budget and a place.
```

**Vietnamese (tiếng Việt)**:

```
iroha,Thế thì tiền bối ơi. Chúng ta đi mua sắm nào!
hachiman,Hả? Bây giờ à?
iroha,Chúng ta phải chọn ngân sách và địa điểm.
```

---

## 📝 Checklist Hoàn Thành

- [ ] Dịch `E4_IRO_01` (Shopping)
- [ ] Dịch `E4_IRO_02` (Chocolate tasting)
- [ ] Dịch `E4_IRO_03` (Iroha ending)
- [ ] Dịch `E4_IRO_04` (Orimoto ending)
- [ ] Dịch `E4_IRO_05` (College scenes)
- [ ] Dịch `E4_IRO_06` (Epilogue)
- [ ] Test game với ngôn ngữ Tiếng Việt
- [ ] Kiểm tra lỗi spelling/grammar

---

## 🎮 Cách Test Trong Game

1. Chạy game: `oregairuzokupc.py`
2. Vào **Settings → Language → Vietnamese**
3. Chọn route Iroha
4. Kiểm tra dịch có hiển thị chưa

---

## 💬 Thủ Thuật Dịch Tốt

✨ **Tips:**

- Giữ tone thoại tự nhiên
- Dùng "tiền bối" cho "senpai"
- Dùng "cô ấy" hay "cô nàng" cho Iroha tùy ngữ cảnh
- Dịch joke nếu có thể, nếu không thì note lại

---

## 📞 Nếu Cần Giúp Đỡ

- Dùng **Google Translate** làm công cụ hỗ trợ
- **Deepl.com** cho dịch tự nhiên hơn
- Xem **anime Oregairu** để hiểu nhân vật tốt hơn

---

**Chúc bạn dịch vui! 🎉**
