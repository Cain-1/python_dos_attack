import requests 
import threading


def main():
    while True:
        res = requests.get(url)
        print("site: ",url,"status code: ",res.status_code)
url = input("url: ")
threads = int(input("threads: "))
for _ in range(threads):
    thr = threading.Thread(target=main)
    thr.start()


main()