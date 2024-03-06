## SETUP: run the following command in the terminal to install dependencies (flask and matplotlib specifically):
## -m pip install -r requirements.txt
## run the web app by typing the following command in the terminal:
## python -m flask --app app run
## the terminal will output the localhost address it is running on

from flask import Flask, render_template
import generator

app = Flask(__name__)

@app.route("/")
def generate_dungeon():
    generator.main()
    return render_template("template.html")

if __name__ == "__main__":
    app.run(debug=True)
