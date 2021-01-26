import requests
import json

URL = "http://localhost:8000/api/v1/absci-targets/target-registration/"
TOKEN = ""


class PTDBRequest():
  def __init__(self, new_target):
    self.target = json.dumps(new_target)

  def post_target(self):
    headers = self.get_headers()
    json_target_data = self.target
    login = {'username': USER, 'password': PASS}
    request = requests.post(URL, data=json_target_data, headers=headers)
    print(request.json())
    print(request.status_code)

  def get_headers(self):
    return {
      "Authorization": f"Token {TOKEN}",
      "Accept": "*/*",
      "Content-Type": "application/json"
    }