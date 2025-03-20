# Import các thư viện cần thiết
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib

# Tạo socket client và kết nối tới server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Tạo cặp khóa RSA cho client
client_key = RSA.generate(2048)

# Nhận khóa công khai của server
server_public_key = RSA.import_key(client_socket.recv(2048))

# Gửi khóa công khai của client tới server
client_socket.send(client_key.publickey().export_key(format='PEM'))

# Nhận khóa AES được mã hóa từ server
encrypted_aes_key = client_socket.recv(2048)

# Giải mã khóa AES bằng khóa riêng của client
cipher_rsa = PKCS1_OAEP.new(client_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)

# Lúc này, client có thể dùng aes_key để trao đổi dữ liệu bảo mật với server
# Hàm mã hóa tin nhắn
def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

# Hàm giải mã tin nhắn
def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

# Hàm nhận tin nhắn từ server
def receive_messages():
    while True:
        encrypted_message = client_socket.recv(1024)
        decrypted_message = decrypt_message(aes_key, encrypted_message)
        print("Received:", decrypted_message)

# Bắt đầu một luồng nhận tin nhắn
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Vòng lặp gửi tin nhắn liên tục
while True:
    message = input("Nhập tin nhắn (gõ 'exit' để thoát): ")
    encrypted_message = encrypt_message(aes_key, message)
    client_socket.send(encrypted_message)
    if message == "exit":
        break

# Đóng kết nối với server
client_socket.close()
