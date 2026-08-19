# 🖥️ System Information Gatherer (Client-Server)

Dự án mô phỏng mô hình mạng Client-Server, trong đó Máy khách (Client) tự động thu thập các thông số phần cứng, hệ điều hành và gửi về Máy chủ (Server) thông qua giao thức HTTP POST.

## 📋 Kiến trúc hệ thống
- **Server:** Xây dựng bằng Python Flask, cung cấp một RESTful API endpoint để lắng nghe và tiếp nhận dữ liệu.
- **Client:** Viết bằng Python, chạy trên máy ảo (VMware - Windows 10), sử dụng các thư viện hệ thống để trích xuất thông tin phần cứng.

## 🚀 Chức năng chính
Client sẽ thu thập và gửi các thông tin sau:
- Tên người dùng (Username)
- Hệ điều hành và phiên bản (OS & Release)
- Thông số Vi xử lý (CPU)
- Dung lượng Bộ nhớ trong (RAM)

## 🛠️ Yêu cầu môi trường (Prerequisites)
- Python 3.x cài đặt trên cả Server và Client.
- Cấu hình mạng: Client và Server phải thông mạng LAN với nhau (Khuyến nghị dùng chế độ NAT hoặc Bridged trên VMware).

## ⚙️ Hướng dẫn Cài đặt & Sử dụng

### 1. Khởi chạy Server (Máy chủ lắng nghe)
Cài đặt thư viện:pip install flask
Khởi động Server:python server.py
*Lưu ý: Đảm bảo tường lửa (Firewall) cho phép kết nối qua cổng 5000.*

### 2. Cấu hình và chạy Client (Máy ảo Windows 10)
Cài đặt các gói phụ thuộc:pip install requests psutil
Mở file `client.py` và cập nhật biến `SERVER_URL` thành địa chỉ IP thực tế của máy Server:SERVER_URL = 'http://
