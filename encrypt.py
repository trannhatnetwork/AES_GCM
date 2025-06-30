from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64

# Nhập dữ liệu từ người dùng
plaintext = input("🔹 Nhập văn bản cần mã hóa: ").encode()
key_input = input("🔹 Nhập khóa bí mật (16, 24 hoặc 32 ký tự): ").encode()
aad_input = input("🔹 Nhập AAD (Authenticated Additional Data, tùy chọn): ").encode()

# Kiểm tra độ dài khóa hợp lệ
if len(key_input) not in [16, 24, 32]:
    print("❌ Độ dài khóa không hợp lệ! Phải là 16, 24 hoặc 32 byte.")
    exit(1)

# Tạo nonce ngẫu nhiên (12 byte)
nonce = os.urandom(12)
aesgcm = AESGCM(key_input)

# Mã hóa
ciphertext = aesgcm.encrypt(nonce, plaintext, aad_input)

# Mã hóa đầu ra dưới dạng base64 để dễ lưu trữ
print("\n✅ Mã hóa thành công!")
print(f"🔐 Nonce (base64): {base64.b64encode(nonce).decode()}")
print(f"📦 Ciphertext (base64): {base64.b64encode(ciphertext).decode()}")
print(f"📎 AAD (nếu có): {aad_input.decode(errors='ignore')}")
