
            s.connect(("www.google.com", 443))
        ctx = ssl.create_default_context()
        http = urllib3.PoolManager()
        print("✅ requests HTTPS 연결 성공:", r.status_code)
        print("✅ urllib3 HTTPS 연결 성공:", r.status)
        print("✅ 소켓 기반 SSL 연결 성공")
        print("❌ requests 오류:", str(e))
        print("❌ SSL 모듈 오류:", str(e))
        print("❌ urllib3 오류:", str(e))
        print("❌ 소켓 SSL 오류:", str(e))
        print(f"✅ SSL 모듈 있음: {ssl.OPENSSL_VERSION}")
        r = http.request("GET", "https://www.google.com")
        r = requests.get("https://www.google.com", timeout=5)
        traceback.print_exc()
        with ctx.wrap_socket(socket.socket(), server_hostname="www.google.com") as s:
    except Exception as e:
    print("\n" + "="*60)
    print("="*60)
    print(f"🔍 {title}")
    print_header("1. ssl 모듈 상태")
    print_header("2. socket SSL 연결 테스트")
    print_header("3. requests HTTPS 연결 테스트")
    print_header("4. urllib3 HTTPS 연결 테스트")
    test_requests_https()
    test_socket_ssl()
    test_ssl_module()
    test_urllib3_https()
    try:
# -*- coding: utf-8 -*-
def print_header(title):
def test_requests_https():
def test_socket_ssl():
def test_ssl_module():
def test_urllib3_https():
if __name__ == "__main__":
import requests
import socket
import ssl
import traceback
import urllib3
