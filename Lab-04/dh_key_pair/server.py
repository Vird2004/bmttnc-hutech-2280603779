from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

# Hàm tạo tham số DH
def generate_dh_parameters():
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    return parameters

# Hàm tạo khóa cho server
def generate_server_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

# Hàm chính
def main():
    # Tạo tham số DH
    parameters = generate_dh_parameters()
    # Tạo cặp khóa riêng và công khai
    private_key, public_key = generate_server_key_pair(parameters)
    # Lưu khóa công khai vào file
    with open("server_public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

if __name__ == "__main__":
    main()
