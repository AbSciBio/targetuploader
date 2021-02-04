import json
import requests

URL = "http://localhost:8000/api/v1/absci-targets/target-registration/"
class PTDBRequest():
  def __init__(self, new_target):
    self.target = json.dumps(new_target)

  def post_target(self):
    headers = self.get_headers()
    # request = requests.post(URL, data=self.target, headers=headers)
    
  def get_headers(self):
    return {
      "Authorization": f"Token {TOKEN}",
      "Accept": "*/*",
      "Content-Type": "application/json"
    }