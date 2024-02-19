from flask import Flask, render_template
import generator

app = Flask(__name__)

@app.route("/")
def generate_dungeon():
    generator.main()
    return render_template("template.html")

if __name__ == "__main__":
    app.run(debug=True)
