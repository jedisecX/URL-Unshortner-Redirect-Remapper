#!/usr/bin/env python3
# JediSecX URL Unshortener and Redirect Mapper
# jedisec.com | jedisec.us | jedisec.cloud | jedisec.online | jedisec.me

import requests
import sys

def unshorten_url(url):
    try:
        session = requests.Session()
        session.max_redirects = 10
        resp = session.head(url, allow_redirects=True, timeout=5)
        history = resp.history

        if not history:
            print(f"[+] No redirects for: {url}")
            return

        print(f"[+] Redirect chain for {url}:")
        for r in history:
            print(f"    {r.status_code} -> {r.url}")
        print(f"    {resp.status_code} -> {resp.url}\n")

    except requests.exceptions.RequestException as e:
        print(f"[-] Failed to resolve {url}: {e}")

def main(file):
    print("[*] JediSecX URL Unshortener starting...\n")
    with open(file, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]

    for url in urls:
        unshorten_url(url)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} urls.txt")
        sys.exit(1)
    main(sys.argv[1])
