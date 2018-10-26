import socket

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ss.bind(('', 4000))
ss.listen(1)
while True:
    print "waiting for connection"
    new,addr = ss.accept()
    new.settimeout(5)
    msg = 'init'
    while len(msg):
        try:
            hostName = ss.gethostname()
            hostIP = ss.gethostbyname(hostName)
            print("Host name: ", hostName)
            print("Host IP: ", hostIP)
            #msg = new.recv(30)
        except socket.timeout:
            print "got timeout"
            break
        print msg
    new.close()
ss.close()
