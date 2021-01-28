import requests
import json
import pprint

URL = "http://localhost:8000/api/v1/absci-targets/target-registration/"
TOKEN = "b94705a1e7169c061c8e550c8416f0c1cbfa0ed7"


class PTDBRequest():
  def __init__(self, new_target):
    self.target = json.dumps(new_target)

  def post_target(self):
    headers = self.get_headers()
    json_target_data = self.target
    # request = requests.post(URL, data=json_target_data, headers=headers)
    # pprint.pprint(json_target_data)

  def get_headers(self):
    return {
      "Authorization": f"Token {TOKEN}",
      "Accept": "*/*",
      "Content-Type": "application/json"
    }