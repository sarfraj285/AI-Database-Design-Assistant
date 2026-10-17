
from flask import Flask, render_template, request
from schema_generator import generate_schema

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    resulta = None
    requirement = ""

    if request.method == "POST":
        requirement = request.form.get("requirement", "").strip()

        if requirement:
            resulta= generate_schema(requirement)

    return render_template(
        "index.html",
        requirement=requirement,
        result=resulta
    )

if __name__ == "__main__":
    app.run(debug=True, port=5001)
