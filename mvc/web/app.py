import tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver
import sqlite3

def _execute(query):
    connection = sqlite3.connect('dbtask.db')
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    resultset = cursor.fetchall()
    connection.close()
    return resultset

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        query = 'select * from task'
        todos = _execute(query)
        self.render('index.html', todos = todos)

class NewHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('new.html')

    def post(self):
        name = self.get_argument('name', None)

        query = 'create table if not exists task \
            (id integer primary key, name text, status numeric) '
        _execute(query)

        query = "insert into task (name, status) values ('%s', %d)" %(name, 1)
        _execute(query)

        self.redirect('/')

class UpdateHandler(tornado.web.RequestHandler):
    def get(self, id, status):
        query = 'update task set status = %d where id = %d' %(int(status), int(id))
        _execute(query)

        self.redirect('/')

class DeleteHandler(tornado.web.RequestHandler):
    def get(self, id):
        query = 'delete from task where id = %d' %(int(id))
        _execute(query)

        self.redirect('/')

class RunApp(tornado.web.Application):
    def __init__(self):
        Handlers = [
            (r'/', IndexHandler),
            (r'/todo/new', NewHandler),
            (r'/todo/update/(\d+)/status/(\d+)', UpdateHandler),
            (r'/todo/delete/(\d+)', DeleteHandler)
        ]

        settings = dict(
            debug=True,
            template_path="",
            static_path="static"
        )

        tornado.web.Application.__init__(self, Handlers, **settings)

if (__name__ == '__main__'):
    http_server = tornado.web.HTTPServer(RunApp())
    http_server.listen(5000)
    tornado.ioloop.IOLoop.instance().start()
