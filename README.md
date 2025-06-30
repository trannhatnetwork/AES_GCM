# 🔐 AES-GCM Demo – Mã hóa và xác thực dữ liệu với Python

## 🧠 Giới thiệu

**AES (Advanced Encryption Standard)** là một thuật toán mã hóa đối xứng, nghĩa là cùng một **khóa bí mật** được dùng cho cả mã hóa và giải mã.

Trong dự án này, chúng ta sử dụng **chế độ GCM (Galois/Counter Mode)** của AES, cho phép:
- ✅ Mã hóa dữ liệu
- ✅ Xác thực dữ liệu thông qua `authentication tag`
- ✅ Bảo vệ tính **toàn vẹn** và **bảo mật**

---

## ❓ Câu hỏi & Giải thích

### 🔹 AES là gì?

> **AES** là một thuật toán mã hóa khối đối xứng, chuẩn hóa bởi NIST, dùng để bảo vệ dữ liệu số.

- Mã hóa/giải mã sử dụng cùng một khóa bí mật
- Kích thước khóa: 128, 192, hoặc 256 bit
- Kích thước khối dữ liệu: 128 bit

---

### 🔹 AES hoạt động như thế nào?

AES hoạt động theo nhiều vòng lặp biến đổi dữ liệu, bao gồm:
1. **SubBytes** – thay thế byte bằng S-box
2. **ShiftRows** – dịch hàng theo pattern
3. **MixColumns** – trộn các cột
4. **AddRoundKey** – XOR với khóa con

Số vòng lặp:
- 10 vòng với khóa 128-bit
- 12 vòng với khóa 192-bit
- 14 vòng với khóa 256-bit

---

### 🔹 AES-GCM là gì?

> **AES-GCM (Galois/Counter Mode)** là một chế độ hoạt động hiện đại của AES giúp **mã hóa và xác thực** dữ liệu cùng lúc.

GCM sử dụng:
- **Nonce** (một giá trị duy nhất cho mỗi lần mã hóa)
- **AAD** (Authenticated Additional Data)
- **Authentication Tag** để kiểm tra tính toàn vẹn

---

### 🔹 Nonce là gì và dùng để làm gì?

- **Nonce** là số ngẫu nhiên hoặc giả ngẫu nhiên được dùng **một lần duy nhất** trong mỗi lần mã hóa.
- Giúp đảm bảo rằng mã hóa cùng một dữ liệu nhiều lần vẫn ra ciphertext khác nhau.

---

### 🔹 Authentication Tag là gì?

> Authentication Tag là đoạn mã được sinh ra khi mã hóa bằng AES-GCM để xác minh dữ liệu không bị sửa đổi.

- Nếu tag không khớp khi giải mã → báo lỗi
- Giúp bảo vệ chống lại tấn công sửa đổi nội dung

---

### 🔹 AAD là gì?

> AAD (Authenticated Additional Data) là dữ liệu **không mã hóa**, nhưng **vẫn được xác thực** cùng với ciphertext.

Ví dụ: tiêu đề gói tin, địa chỉ IP, metadata...

---

## 💡 Ý tưởng chương trình: AES-GCM Demo

Chương trình minh họa 2 chức năng:

### 🟢 Mã hóa:
- Nhập:
  - Văn bản gốc
  - Khóa bí mật (16/24/32 byte)
  - Nonce (12 byte)
  - AAD (tùy chọn)
- Thực hiện mã hóa bằng AES-GCM
- Xuất:
  - Ciphertext
  - Authentication Tag

### 🔄 Giải mã:
- Nhập:
  - Ciphertext
  - Khóa bí mật
  - Nonce
  - Authentication Tag
- Giải mã và xác minh tag
- Nếu hợp lệ → in ra văn bản gốc
- Nếu sai tag → thông báo lỗi

---

## 🛠️ Yêu cầu

- Python 3.x
- Thư viện [`cryptography`](https://cryptography.io)

### Cài đặt:
```bash
pip install cryptography
