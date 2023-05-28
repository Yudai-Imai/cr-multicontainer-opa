import json
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def hello():
    allowed = check_authorization(request)
    if allowed == True:
        return jsonify({"text": "hello world, alice!"})
    else:
        return jsonify({})

def get_requestdata(request):
    return json.loads(request.get_data())

def check_authorization(request):
    user = get_requestdata(request)
    input_data = json.dumps({"input": {"user": user['user']}})
    headers = {'content-type': 'application/json'}

    url = "http://localhost:5050/v1/data/example"  # OPAのURL（適宜変更）
    response = requests.post(url, data=input_data, headers=headers)

    response_json = response.json()
    allowed = response_json["result"]["allow"]
    print("-----")
    print(user)
    print("allowed:" + str(allowed))
    print("-----")
    return allowed

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)