from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp
 
app = Flask(__name__)
 
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
 

def isWinner(bo):
    le = "X"
    le2 = "O"
    if ((bo[0][0] == le and bo[0][1] == le and bo[0][2] == le) or (bo[1][0] == le and bo[1][1] == le and bo[1][2] == le) or (bo[2][0] == le and bo[2][1] == le and bo[2][2] == le) or (bo[0][0] == le and bo[1][0] == le and bo[2][0] == le) or (bo[0][1] == le and bo[1][1] == le and bo[2][1] == le) or (bo[0][2] == le and bo[1][2] == le and bo[2][2] == le) or (bo[0][0] == le and bo[1][1] == le and bo[2][2] == le) or (bo[0][2] == le and bo[1][1] == le and bo[2][0] == le)):
        return "X wins"
    elif ((bo[0][0] == le2 and bo[0][1] == le2 and bo[0][2] == le2) or (bo[1][0] == le2 and bo[1][1] == le2 and bo[1][2] == le2) or (bo[2][0] == le2 and bo[2][1] == le2 and bo[2][2] == le2) or (bo[0][0] == le2 and bo[1][0] == le2 and bo[2][0] == le2) or (bo[0][1] == le2 and bo[1][1] == le2 and bo[2][1] == le2) or (bo[0][2] == le2 and bo[1][2] == le2 and bo[2][2] == le2) or (bo[0][0] == le2 and bo[1][1] == le2 and bo[2][2] == le2) or (bo[0][2] == le2 and bo[1][1] == le2 and bo[2][0] == le2)):
        return "O wins"
    else:
        return "Your move"

@app.route("/<int:row>/<int:col>")
@app.route("/")
def index(row=None, col=None):
    if "board" not in session:
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"
    else:
        session["board"][row][col] = session["turn"]
        if session["turn"] == "X":
            session["turn"] = "O"
        elif session["turn"] == "O":
            session["turn"] = "X"
        
    # Check if game is won
    a = isWinner(session["board"])
    
    return render_template("game.html", game=session["board"], turn=session["turn"], result=a)
 
@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    return redirect(url_for("index", row=row, col=col))

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("index"))