from flask import Flask, render_template

from forms.register_form import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
@app.route("/register")
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template("register_form.html", form=form, message="Passwords don`t match")
    return render_template("registration.html", form=form)


if __name__ == "__main__":
    app.run()
