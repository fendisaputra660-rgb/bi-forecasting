import requests

BASE = "http://127.0.0.1:5000"

def run():
    s = requests.Session()
    # login
    resp = s.post(f"{BASE}/login", data={"username": "admin", "password": "admin123"})
    print("POST /login ->", resp.status_code)

    d = s.get(f"{BASE}/dashboard")
    print("GET /dashboard ->", d.status_code, "len", len(d.text))

    b = s.get(f"{BASE}/bi")
    print("GET /bi ->", b.status_code, "len", len(b.text))

if __name__ == '__main__':
    run()
