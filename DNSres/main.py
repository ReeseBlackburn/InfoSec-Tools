import sys, argparse, socket, urllib.request, mods
# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-u", "--url", help = "enter url")
parser.add_argument("-w", "--wordlist", help = "enter file path to wordlist")

# Read arguments from command line
args = parser.parse_args()

if args.url:
    out = args.url
    wl = args.wordlist
    k = 0
    while k == 0:
        furl = "https://"+out
        ip = socket.gethostbyname_ex(out)
        print(ip)
        break    