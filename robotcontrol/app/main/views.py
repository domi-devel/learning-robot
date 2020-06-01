from flask import render_template, Blueprint, request

main = Blueprint("main", __name__, template_folder="templates/main", url_prefix="/")


@main.route("/", methods=["GET"])
def index():

    return render_template("main/index.html")


@main.route("/post", methods=["POST"])
def handlepost():
    try:
        cmd = request.data.decode()
        print(cmd)
        if(cmd == 'start'):
            return "OK"
        elif(cmd == 'stop'):
            return "OK"
        else:
            return('NOK')
    except Exception:
        return "Command Error"
