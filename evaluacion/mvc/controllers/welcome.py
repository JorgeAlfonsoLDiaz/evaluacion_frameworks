import web

render = web.template.render('mvc/views/')
session = web.session.Session(app, web.session.DiskStore('sessions'))

class Bienvenida:
    def GET(self):
        if session.username == "usuario" and session.password == "1234":
            render.welcome(session.username, session.password)
        else:
            return render.index()

    

