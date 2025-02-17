import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 8080))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        # работа с файлом
        html_page = open('index.html')
        html_content = html_page.read()
        html_page.close()

        html_response = 'HTTP/1.0 200 OK\nContent-Type: text/html\n\n' + html_content

        conn.sendall(html_response.encode('utf-8'))
        conn.close()


if __name__ == '__main__':
    main()
