
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import urllib2, json

service_api_key = "5fb9b4fe5fb9b4fe5fb9b4fe2f5fe85f3255fb95fb9b4fe0588d75f57dfd6c5d4c3dd4c"
def get_vk_user_data():
    r = urllib2.urlopen("https://api.vk.com/method/users.get?user_id=1&v=5.52&fields=photo_max").read()
    return str(json.loads(r)["response"][0]["photo_max"])

class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        
        
        self.wfile.write(get_vk_user_data())

serv = HTTPServer(("localhost",8080),HttpProcessor)
serv.serve_forever()
