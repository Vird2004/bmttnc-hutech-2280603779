
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

# Hàm tạo cặp khóa riêng và công khai cho client
def generate_client_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

# Hàm tạo shared secret (khóa chung) từ khóa riêng của client và khóa công khai của server
def derive_shared_secret(private_key, server_public_key):
    shared_key = private_key.exchange(server_public_key)
    return shared_key

def main():
    # Nạp khóa công khai của server từ file PEM
    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(f.read())

    # Sử dụng tham số từ khóa công khai của server để tạo cặp khóa client
    parameters = server_public_key.parameters()
    private_key, public_key = generate_client_key_pair(parameters)

    # Tạo shared secret sử dụng khóa riêng của client và khóa công khai của server
    shared_secret = derive_shared_secret(private_key, server_public_key)

    print("Shared Secret:", shared_secret.hex())

if __name__ == "__main__":
    main()

from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

# Hàm tạo cặp khóa riêng và công khai cho client
def generate_client_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

# Hàm tạo shared secret (khóa chung) từ khóa riêng của client và khóa công khai của server
def derive_shared_secret(private_key, server_public_key):
    shared_key = private_key.exchange(server_public_key)
    return shared_key

def main():
    # Nạp khóa công khai của server từ file PEM
    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(f.read())

    # Sử dụng tham số từ khóa công khai của server để tạo cặp khóa client
    parameters = server_public_key.parameters()
    private_key, public_key = generate_client_key_pair(parameters)

    # Tạo shared secret sử dụng khóa riêng của client và khóa công khai của server
    shared_secret = derive_shared_secret(private_key, server_public_key)

    print("Shared Secret:", shared_secret.hex())

if __name__ == "__main__":
    main()

