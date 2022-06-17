import http.server
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('10.255.255.255', 1))

ip = s.getsockname()[0]

port=input("Which port?: ")

try:

    if not port:
        port=8080

    print("\n- Your local ip is:", ip)
    print("- And the port is:", port, "\n")
    http.server.test(HandlerClass=http.server.CGIHTTPRequestHandler, port=port)

except:
    print("\nAn error has occured. Please try again.")
