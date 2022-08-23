import requests

BASE = "http://127.0.0.1:5000/"

# res = requests.get(BASE + "/todo")
# print(res.text)

# input()

# res = requests.post(BASE + "/todo", {"todo": "A", "status": "A"})
# print(res.text)

res = requests.put(BASE + "/todo/4", {"todo": "updated A","status": "updated A"})
print(res.text)