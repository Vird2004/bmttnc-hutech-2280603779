# Import thư viện cần thiết
import random
import tornado.ioloop
import tornado.web
import tornado.websocket

# Class WebSocketServer để quản lý các kết nối WebSocket
class WebSocketServer(tornado.websocket.WebSocketHandler):
    clients = set()  # Tập hợp các client đã kết nối
    
    def open(self):
        # Thêm client vào danh sách khi kết nối được mở
        WebSocketServer.clients.add(self)
    
    def on_close(self):
        # Loại client khỏi danh sách khi kết nối bị đóng
        WebSocketServer.clients.remove(self)
    
    @classmethod
    def send_message(cls, message: str):
        # Gửi tin nhắn đến tất cả các client đã kết nối
        print(f"Gửi tin nhắn: {message} đến {len(cls.clients)} client(s).")
        for client in cls.clients:
            client.write_message(message)

# Class RandomWordSelector để chọn ngẫu nhiên từ danh sách
class RandomWordSelector:
    def __init__(self, word_list):
        self.word_list = word_list
    
    def sample(self):
        # Chọn ngẫu nhiên một từ trong danh sách
        return random.choice(self.word_list)

# Hàm main để chạy ứng dụng Tornado
def main():
    # Thiết lập ứng dụng Tornado
    app = tornado.web.Application(
        [(r"/websocket/", WebSocketServer)],  # Định nghĩa route cho WebSocket
        websocket_ping_interval=10,
        websocket_ping_timeout=30,
    )
    app.listen(8888)  # Lắng nghe trên cổng 8888
    
    io_loop = tornado.ioloop.IOLoop.current()
    
    # Tạo đối tượng RandomWordSelector với danh sách từ
    word_selector = RandomWordSelector(['apple', 'banana', 'orange', 'grape', 'melon'])
    
    # Gửi tin nhắn ngẫu nhiên đến các client mỗi 3 giây
    periodic_callback = tornado.ioloop.PeriodicCallback(
        lambda: WebSocketServer.send_message(word_selector.sample()), 3000
    )
    periodic_callback.start()
    
    io_loop.start()  # Bắt đầu vòng lặp I/O

# Khởi động ứng dụng nếu chương trình được chạy trực tiếp
if __name__ == "__main__":
    main()
