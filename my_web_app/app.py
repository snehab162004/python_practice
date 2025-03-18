from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def game():
    if request.method == "POST":
        action = request.form["action"]
        if action == "run":
            return render_template("result.html", message="You escaped safely!")
        elif action == "fight":
            return render_template("result.html", message="The monster defeated you!")
        else:
            return render_template("result.html", message="Invalid choice.")
    return render_template("game.html")

if __name__ == "__main__":
    app.run(debug=True)
