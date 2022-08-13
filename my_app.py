import flask
import socket


app=flask.Flask(__name__)
app.config["DEBUG"]=True

@app.route('/',methods=["GET"])
def display_fun():
    return f"This is a test webseite ! and served by host: {socket.gethostname()}"


#app.run(host="0.0.0.0")
