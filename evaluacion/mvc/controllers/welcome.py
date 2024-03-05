import web

render = web.template.render('mvc/views/')

class Bienvenida:
    def GET(self):
        try:
            cookie = web.cookies()
            username = cookie.get("username")
            if username:
                render.welcome(username)
            else:
                web.seeother('/')
        except Exception as e:
            return "Error" + str(e.args)

            
    

