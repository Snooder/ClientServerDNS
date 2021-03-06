import socket
import sys

def dnslookup(data, dnstable):
    print("Data: " + str(data))
    found = 0
    for i in dnstable:
        if(str(data)==i[0]):
            print("Match found")
            print(i)
            found=1
            databack = str(i[0]) + " " + str(i[1])+ " " + str(i[2][0])
            connection.sendall(databack)
            print(databack)
    if(found==0):
		hostname = socket.gethostname()
        databack = str(hostname) + " - Error:HOST NOT FOUND"
        connection.sendall(databack)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostnames = open("PROJI-DNSTS.txt","r")
dnstable = []
for dns in hostnames:
    name = dns.split(" ")
    dnstable.append([name[0],name[1],name[2].rsplit()])

port = int(sys.argv[1])
hostname = socket.gethostname()
# Bind the socket to the port
server_address = (hostname, port)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address)
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(50)
            print('received {!r}'.format(data))
            if data:
                dnslookup(data, dnstable)
                print('sending data back to the client')
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        print("Closing current connection")
        connection.close()
