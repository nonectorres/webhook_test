from flask import Flask, request
# webhook test
app = Flask(__name__)

@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    payload = request.json
    print("Received GitHub webhook!")
    print(payload)  # Print the JSON data received
    return 'OK', 200

if __name__ == '__main__':
    app.run(port=5000)
