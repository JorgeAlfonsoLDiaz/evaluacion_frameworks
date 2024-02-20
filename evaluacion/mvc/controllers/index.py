import web

render = web.template.render('mvc/views/')
session = web.session.Session(app, web.session.DiskStore('sessions'))

session.username = ""
session.password = ""

class Login:
    def GET(self):
        if session.username == "usuario" and session.password == "1234":
            render.welcome(session.username, session.password)
        else:
            return render.index()

    def POST(self):
        input_data = web.input()

        username = input_data.username
        password = input_data.password

        session.username = username
        session.password = password

        if session.username == "usuario" and session.password == "1234":
            return render.welcome(session.username, session.password)
        else:
            return render.index()

        

