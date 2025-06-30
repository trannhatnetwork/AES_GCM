from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import base64

# Nhập dữ liệu cần giải mã
ciphertext_b64 = input("📦 Nhập ciphertext (base64): ")
nonce_b64 = input("🔐 Nhập nonce (base64): ")
key_input = input("🔑 Nhập khóa bí mật (16, 24 hoặc 32 ký tự): ").encode()
aad_input = input("📎 Nhập AAD (Authenticated Additional Data, nếu có): ").encode()

# Giải mã base64 thành bytes
try:
    ciphertext = base64.b64decode(ciphertext_b64)
    nonce = base64.b64decode(nonce_b64)
except Exception:
    print("❌ Không thể decode base64. Vui lòng kiểm tra đầu vào.")
    exit(1)

# Kiểm tra khóa
if len(key_input) not in [16, 24, 32]:
    print("❌ Độ dài khóa không hợp lệ! Phải là 16, 24 hoặc 32 byte.")
    exit(1)

aesgcm = AESGCM(key_input)

# Giải mã và xác thực
try:
    plaintext = aesgcm.decrypt(nonce, ciphertext, aad_input)
    print("\n✅ Giải mã thành công!")
    print(f"📝 Văn bản gốc: {plaintext.decode()}")
except Exception:
    print("❌ Giải mã thất bại hoặc authentication tag không khớp!")
