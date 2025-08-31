from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "change_this_secret_key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        # Here you would normally process/store the message.
        flash("Thank you, {0}! Your message has been received.".format(name or "visitor"))
        return redirect(url_for("contact"))
    return render_template("contact.html")

if __name__ == "__main__":
    app.run()

    