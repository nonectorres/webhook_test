from flask import Flask, request
# webhook test server update
app = Flask(__name__)

# test commit again, now, now

@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    payload = request.json
    print("Received GitHub webhook!")
    print(payload)  # Print the JSON data received
    return 'OK', 200

if __name__ == '__main__':
    app.run(port=5000)
