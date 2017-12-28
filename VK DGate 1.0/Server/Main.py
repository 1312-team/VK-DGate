from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import urllib2, json
import urlparse
import logging

def get_vk_user_data_1_(s="https://api.vk.com/method/users.get?user_id=1&v=5.52&fields=photo_max"):
    r = urllib2.urlopen(s).read()
    return str(json.loads(r)["response"][0]["photo_max"])

class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        
        self.send_response(200)
        #data = self.send_response(200)
        #print(data)
        #print(self.path)
        #logging.info("added %s and to get" % self.log_request)
        logging.info("GET REQUEST\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        o = urlparse.urlparse(self.path)
        urlparse.parse_qs(o.query)
        print(o[4])
        if(o[4] == "Need-photo-durov"):
            self.send_header('content-type','text/html')
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(get_vk_user_data_1_())

def main(argv=None):
    serv = HTTPServer(("localhost",8080),HttpProcessor)
    logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'mylog.log')
    logging.debug( '\n\n')
    logging.debug( u'_______________________' )
    logging.debug( u'The Server was launched' )
    logging.debug( u'_______________________' )
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
    serv.server_close()
    logging.info('_______________________')
    logging.info('  Server was closed..  ')
    logging.info('_______________________')

if __name__ == "__main__":
    main()
