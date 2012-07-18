import httplib
import socket
import ssl

class HTTPSConnection(httplib.HTTPSConnection):

    def connect(self):
        "Connect to a host on a given (SSL) port."

        sock = socket.create_connection((self.host, self.port),
                self.timeout, self.source_address)
        if self._tunnel_host:
            self.sock = sock
            self._tunnel()
        self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file,
                ssl_version=ssl.PROTOCOL_TLSv1)
