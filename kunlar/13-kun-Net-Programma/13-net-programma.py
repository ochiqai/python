import socket


def retrieve_file():
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect(('data.pr4e.org', 80))

    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    print(cmd)
    mysocket.send(cmd)

    while True:
        data = mysocket.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')

    mysocket.close()

    # print("GET http://data.pr4e.org/romeo123123.txt HTTP/1.0\r\n\r\n")
    #
    #
    # example1 = b'Hello world'
    # example2 = 'Hello world'.encode()
    # print(example1, ' ', example2)


def retrieve_image():
    import time

    print("Rasmlarni HTTP orqali olish")
    HOST = "data.pr4e.org"
    PORT = 80
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((HOST, PORT))
    mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
    count = 0
    picture = b""

    while True:
        data = mysock.recv(5120)
        if len(data) < 1: break
        time.sleep(0.25)
        count += len(data)  #
        print(len(data), data)
        picture += data

    mysock.close()

    joy = picture.find(b"\r\n\r\n")
    print("header uzunligi", joy)
    print(picture[:joy].decode())

    rasm = picture[joy+4:]
    fayl = open("kitob.jpg", "wb")
    fayl.write(rasm)
    fayl.close()


def retrieve_web_page():
    import urllib.request
    fayl = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
    for qator in fayl:
        print(qator.decode().strip())

    img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
    fhand = open('cover3.jpg', 'wb')
    fhand.write(img)
    fhand.close()


def count_words():
    import urllib.request, urllib.parse, urllib.error
    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    counts = dict()
    for line in fhand:
        words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    print(counts)


def parse_html():
    import urllib.request, urllib.parse, urllib.error
    import re
    import ssl

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('URL addresni kiriting - ')
    html = urllib.request.urlopen(url, context=ctx).read()
    print(html)
    links = re.findall(b'href="(http[s]?://.*?)"', html)
    for link in links:
        print(link.decode())










