import web

render = web.template.render('mvc/views/')

class Login:
    def GET(self):
        try:
            cookie = web.cookies()
            if cookie.get("username"):
                username = cookie.get("username")
                password = cookie.get("password")

                if username == "usuario" and password == "1234":
                    raise web.seeother('/login')

                else:
                    return render.index()
            else:
                return render.index()

        except Exception as e:
            return "Error" + str(e.args)

    def POST(self):
        input_data = web.input()

        username = input_data.username
        password = input_data.password

        web.setcookie("username", username, expires="", domain=None)
        web.setcookie("password", password, expires="", domain=None)

        return render.index()

        

