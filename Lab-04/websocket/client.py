import tornado.ioloop
import tornado.websocket

class WebSocketClient:
    def __init__(self, io_loop):
        self.connection = None
        self.io_loop = io_loop

    def start(self):
        # Bắt đầu kết nối và lắng nghe
        self.connect_and_read()

    def stop(self):
        # Dừng vòng lặp I/O
        self.io_loop.stop()

    def connect_and_read(self):
        # Kết nối đến WebSocket server
        print("Đang kết nối và lắng nghe...")
        tornado.websocket.websocket_connect(
            url="ws://localhost:8888/websocket/",
            callback=self.maybe_retry_connection,
            on_message_callback=self.on_message,
            ping_interval=10,  # Gửi tín hiệu ping mỗi 10 giây
            ping_timeout=30    # Timeout sau 30 giây nếu không có phản hồi
        )

    def maybe_retry_connection(self, future) -> None:
        try:
            self.connection = future.result()
        except Exception:
            # Xử lý khi không thể kết nối
            print("Không kết nối được, thử lại sau 3 giây...")
            self.io_loop.call_later(3, self.connect_and_read)

    def on_message(self, message):
        if message is None:
            # Xử lý khi mất kết nối
            print("Mất kết nối, đang kết nối lại...")
            self.connect_and_read()
            return
        # In tin nhắn nhận được từ server
        print(f"Từ server: {message}")
        # Lắng nghe tin nhắn tiếp theo
        self.connection.read_message(callback=self.on_message)

# Hàm chính khởi tạo vòng lặp và chạy client
def main():
    io_loop = tornado.ioloop.IOLoop.current()
    client = WebSocketClient(io_loop)
    io_loop.add_callback(client.start)
    io_loop.start()

# Khởi động nếu script được chạy trực tiếp
if __name__ == "__main__":
    main()
