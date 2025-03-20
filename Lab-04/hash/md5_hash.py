# Thực hiện phép xoay vòng trái
def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

# Hàm chính thực hiện băm MD5
def md5(message):
    # Giá trị ban đầu cho MD5
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476
    
    # Tính toán và xử lý dữ liệu
    original_length = len(message)
    message = message + b'\x80' + b'\x00' * ((56 - (original_length + 1) % 64) % 64)
    message += (original_length * 8).to_bytes(8, byteorder='little')

    # Chia message thành từng khối
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]

        # Giá trị tạm thời để lưu trữ
        a0, b0, c0, d0 = a, b, c, d

        # Vòng lặp chính
        for j in range(64):
            if 0 <= j <= 15:
                f = (b & c) | (~b & d)
                g = j
            elif 16 <= j <= 31:
                f = (d & b) | (~d & c)
                g = (5 * j + 1) % 16
            elif 32 <= j <= 47:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            elif 48 <= j <= 63:
                f = c ^ (b | ~d)
                g = (7 * j) % 16

            temp = d
            d = c
            c = b
            b = (b + left_rotate((a + f + 0x5A827999 + words[g]) & 0xFFFFFFFF, 3)) & 0xFFFFFFFF
            a = temp

        # Cộng giá trị tạm thời vào giá trị ban đầu
        a = (a + a0) & 0xFFFFFFFF
        b = (b + b0) & 0xFFFFFFFF
        c = (c + c0) & 0xFFFFFFFF
        d = (d + d0) & 0xFFFFFFFF

    # Kết quả cuối cùng
    return '{:08x}{:08x}{:08x}{:08x}'.format(a, b, c, d)

# Yêu cầu người dùng nhập chuỗi để băm
input_string = input("Nhập chuỗi cần băm: ")
md5_hash = md5(input_string.encode('utf-8'))
print(f"Mã băm MD5 của chuỗi '{input_string}' là: {md5_hash}")
