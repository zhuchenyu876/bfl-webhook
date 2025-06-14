from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/image-callback', methods=['POST'])
def image_callback():
    data = request.get_json()
    print("✅ 收到回调数据：", data)

    task_id = data.get('id')
    image_url = data.get('image_url')

    print(f"任务完成：任务ID = {task_id}, 图片地址 = {image_url}")

    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run()
