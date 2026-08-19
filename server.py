from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/system-info', methods=['POST'])
def receive_info():
    data = request.get_json()
    if data:
        print("\nNHẬN DỮ LIỆU TỪ CLIENT")
        print(f"User: {data.get('username')}")
        print(f"Hệ điều hành: {data.get('os')} {data.get('os_release')}")
        print(f"CPU: {data.get('cpu')}")
        print(f"RAM: {data.get('ram')} GB")
        print("================================\n")
        
        return jsonify({"status": "success", "message": "Đã lưu dữ liệu máy khách!"}), 200
        
    return jsonify({"status": "error", "message": "Không nhận được payload dữ liệu"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)