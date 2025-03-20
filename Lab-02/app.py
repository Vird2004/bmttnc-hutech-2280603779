from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# Route cho trang chủ
@app.route('/')
def home():
    return render_template('index.html')

# Route cho Caesar Cipher
@app.route('/caesar')
def caesar():
    return render_template('caesar.html')

# Route mã hóa Caesar Cipher
@app.route('/encrypt', methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt(text, key)
    return f'{text}<br>Key: {key}<br>Encrypted Text: {encrypted_text}'

# Route giải mã Caesar Cipher
@app.route('/decrypt', methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt(text, key)
    return f'{text}<br>Key: {key}<br>Decrypted Text: {decrypted_text}'

# Chạy ứng dụng
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
