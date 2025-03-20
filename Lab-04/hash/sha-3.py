from Crypto.Hash import SHA3_256

# Hàm băm sử dụng SHA-3
def sha3(message):
    sha3_hash = SHA3_256.new()   # Tạo một đối tượng SHA3-256
    sha3_hash.update(message)    # Cập nhật dữ liệu cần băm
    return sha3_hash.digest()    # Trả về kết quả băm (dạng bytes)

# Hàm chính
def main():
    # Yêu cầu người dùng nhập chuỗi văn bản và chuyển thành bytes
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    
    # Tính toán hàm băm SHA-3
    hashed_text = sha3(text)
    
    # Hiển thị kết quả
    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))
    print("SHA-3 Hash:", hashed_text.hex())  # Chuyển kết quả băm sang dạng hex

# Nếu chương trình chạy trực tiếp, thực hiện hàm main
if __name__ == "__main__":
    main()
