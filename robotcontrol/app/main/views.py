from flask import render_template, Blueprint, request

main = Blueprint("main", __name__, template_folder="templates/main", url_prefix="/")


@main.route("/", methods=["GET"])
def index():
    return render_template("main/index.html")


@main.route("/load", methods=["GET"])
def load():
    return render_template("main/load.html")


@main.route("/save", methods=["GET"])
def save():
    return render_template("main/save.html")


@main.route("/post", methods=["POST"])
def handlepost():
    try:
        cmd = request.data.decode()
        print(cmd)
        if "load" in cmd:
            slot = cmd[-1:]
            # do load slot
            return "OK"
        elif "save" in cmd:
            slot = cmd[-1:]
            # do save
            return "OK"
        elif(cmd == 'idle'):
            return "OK"
        elif(cmd == 'work'):
            return "OK"
        elif(cmd == 'train'):
            return "OK"
        elif(cmd == 'shutdown'):
            return "OK"
        else:
            return('NOK')
    except Exception:
        return "Command Error"



