# Import thư viện hashlib để sử dụng thuật toán băm BLAKE2
import hashlib

# Hàm băm BLAKE2 sử dụng digest_size 64 byte
def blake2(message):
    # Tạo một đối tượng băm BLAKE2
    blake2_hash = hashlib.blake2b(digest_size=64)
    # Cập nhật nội dung dữ liệu cần băm
    blake2_hash.update(message)
    # Trả về kết quả băm (dạng bytes)
    return blake2_hash.digest()

# Hàm chính thực hiện lấy chuỗi từ người dùng, băm và in ra kết quả
def main():
    # Nhập chuỗi văn bản từ người dùng và chuyển thành bytes
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    # Sử dụng hàm băm BLAKE2 để băm chuỗi văn bản
    hashed_text = blake2(text)
    # Hiển thị chuỗi đã nhập và giá trị băm
    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))
    print("BLAKE2 Hash:", hashed_text.hex())  # Chuyển bytes sang chuỗi hexa

# Gọi hàm chính nếu chương trình chạy trực tiếp
if __name__ == "__main__":
    main()
