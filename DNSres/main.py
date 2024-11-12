import sys
import socket
import urllib.request
k = 0
while k == 0:
    out = input("Enter URL: ")
    ip = socket.gethostbyname_ex(out)
    print(out, ip)
    out = "https://"+out
    def attempt_open_url(out):
        try:
            with urllib.request.urlopen(out) as response:
                return response.read()
        except urllib.error.URLError as e:
            print(f"Error opening URL: {e.reason}")
            return None

        content = attempt_open_url(out)

        if content():
            print("URL opened successfully!")
        else:
            print("Failed to open URL.")
    inp = input("Continue? Y/N: ")
    if inp == 'Y':
        k==0
    else:
        break



    