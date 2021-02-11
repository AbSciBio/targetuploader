import json
import requests
from pprint import pprint
class PTDBRequest():
  def __init__(self, new_target, user_input):
    self.target = json.dumps(new_target)
    self.url = user_input['API_URL']
    self.token = user_input['token']
    pprint(self.target, indent=2)
    print(" ")

  def post_target(self):
    headers = self.get_headers()
    request = requests.post(self.url, data=self.target, headers=headers)
    pprint(request.content)
    
  def get_headers(self):
    return {
      "Authorization": f"Token {self.token}",
      "Accept": "*/*",
      "Content-Type": "application/json"
    }
