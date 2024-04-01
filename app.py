from bottle import default_app, get, post, static_file, template, run
from icecream import ic

##############################
@get("/app.css")
def _():
    return static_file("app.css", ".") 

##############################
@get("/mixhtml.js")
def _():
    return static_file("mixhtml.js", ".") 

##############################
@get("/")
def _():
    return "test"
    return template("index")

##############################
@get("/login")
def _():
    return template("login")

##############################
@post("/login")
def _():
    try:
        return """
        <template mix-target="#toast_container">
            <div class="toast mix-fade-out" mix-ttl="2000">ok</div>
        </template>
        """
        # return """
        # <template mix-redirect="/profile"></template>
        # """
    except Exception as ex:
        ic(ex)
    finally:
        pass


##############################
# if __name__ == '__main__':
#     app = default_app()
run(host="0.0.0.0", port=80, debug=True, reloader=True)