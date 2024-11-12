import sys, argparse, socket, urllib.request
class url():
    def attempt_open_url(furl):
            try:
                with urllib.request.urlopen(furl) as response:
                    return response.read()
            except urllib.error.URLError as e:
                print(f"Error opening URL: {e.reason}")
                return None    
            content = attempt_open_url(furl)
            if content():
                print("URL opened successfully!")
            else:
                print("Failed to open URL.")
                sys.exit