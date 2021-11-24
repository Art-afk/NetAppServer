#from _typeshed import Self
import socketserver
import logging

PORT = 9090
HOST = 'localhost'
#IP = ''

class MyTCPServer(socketserver.BaseRequestHandler):
    def servershutdown(self):
        self.__shutdown_request = True
        self.__is_shut_down.wait()
    def handle(self):
            try:
                self.data = self.request.recv(1024).strip()
                if self.data == 'shutdown':
                    servershutdown()                   

                print("{} wrote:".format(self.client_address[0]))
                print(self.data)

                self.request.sendall(self.data.upper(), )
            except socketserver.error as e:
                logging.error("[ERROR] %s\n" % e[1])
            #HostIP = socket.gethostbyname(hostname)
            #        listener.bind(HostIP)
   

if __name__ == "__main__":
          with socketserver.TCPServer((HOST,PORT),MyTCPServer) as server:
            #socketserver.TCPServer.allow_reuse_address = True
            server.serve_forever()
  