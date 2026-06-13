from flask import Flask, render_template, request
from summarizer import summarize_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    text = ""
    summary = ""

    if request.method == "POST":
        text = request.form["text"]

        if text.strip():
            summary = summarize_text(text)

    return render_template(
        "index.html",
        text=text,
        summary=summary
    )

if __name__ == "__main__":
    app.run(debug=True)