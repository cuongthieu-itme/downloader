# YouTube Video Downloader

Ứng dụng Django đơn giản cho phép người dùng nhập URL YouTube và tải xuống video hoặc audio thông qua trình duyệt.

## Tính năng

- Tải xuống video YouTube với chất lượng tốt nhất
- Hỗ trợ cả định dạng video (MP4) và audio (MP3)
- Xem trước thông tin video trước khi tải xuống
- Giao diện người dùng thân thiện và dễ sử dụng
- Tải xuống trực tiếp từ trình duyệt

## Yêu cầu hệ thống

- Python 3.8 hoặc mới hơn
- Django 4.2.x
- yt-dlp
- ffmpeg (cần được cài đặt trên hệ thống)

## Cài đặt

1. Clone repository:
   ```
   git clone <repository-url>
   cd downloader
   ```

2. Tạo và kích hoạt môi trường ảo:
   ```
   python -m venv venv
   source venv/bin/activate  # Trên Linux/macOS
   venv\Scripts\activate     # Trên Windows
   ```

3. Cài đặt các thư viện phụ thuộc:
   ```
   pip install -r requirements.txt
   ```

4. Cài đặt ffmpeg (cần thiết để xử lý audio):
   - Trên Ubuntu/Debian:
     ```
     sudo apt update
     sudo apt install ffmpeg
     ```
   - Trên macOS (sử dụng Homebrew):
     ```
     brew install ffmpeg
     ```
   - Trên Windows: Tải xuống từ [ffmpeg.org](https://ffmpeg.org/download.html) và thêm vào PATH

5. Thiết lập cấu trúc thư mục:
   ```
   python manage.py collectstatic
   ```

## Chạy ứng dụng

1. Khởi động máy chủ phát triển:
   ```
   python manage.py runserver
   ```

2. Truy cập ứng dụng qua trình duyệt tại địa chỉ:
   ```
   http://127.0.0.1:8000/
   ```

## Cách sử dụng

1. Nhập URL video YouTube vào form
2. Chọn định dạng mong muốn (MP4 hoặc MP3)
3. Nhấn nút "Tải Video"
4. Đợi hệ thống xử lý video và hiển thị preview
5. Nhấn nút "Tải xuống MP4/MP3" để lưu file về máy

## Lưu ý

- Ứng dụng này chỉ dành cho mục đích học tập và nghiên cứu
- Chỉ sử dụng để tải xuống nội dung mà bạn có quyền sử dụng
- Tôn trọng quyền tác giả và điều khoản dịch vụ của YouTube
