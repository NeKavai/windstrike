import tornado.ioloop
import tornado.web
import tornado.httpserver

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Init commit")

def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
    ])

if __name__ == '__main__':
    server = tornado.httpserver.HTTPServer(make_app())
    server.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    
