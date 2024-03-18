from flask import Flask, render_template
import generator

app = Flask(__name__)

@app.route("/")
def generate_dungeon():
    generator.main()
    return render_template("generator.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
