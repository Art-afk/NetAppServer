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
           # try:
            while True:
                self.data = self.request.recv(1024).strip()
                if self.data == 'shutdown':
                    self.servershutdown()
                #FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
                #logging.basicConfig(format=FORMAT)
                #d = {'clientip': self.client_address[0],'user': 'fbloggs'}
                FORMAT = '%(asctime)s %(clientip)-8s %(message)s'
                logging.basicConfig(format=FORMAT)
                d = {'clientip': self.client_address[0] }
                
               
                logger = logging.getLogger('socketserver')
                logger.warning('Protocol problem: %s', 'connection resettt', extra=d)

              #  print("{} wrote:".format(self.client_address[0]))
                dataS = self.data
                print(dataS)
                self.request.sendall(dataS + b'\n')
            # except socketserver.error as e:
                #    logging.error("[ERROR] %s\n" % e[1])
                #HostIP = socket.gethostbyname(hostname)
                #        listener.bind(HostIP)
    

if __name__ == "__main__":
          socketserver.TCPServer.allow_reuse_address = True
          with socketserver.TCPServer((HOST,PORT),MyTCPServer) as server:
            server.serve_forever()
  