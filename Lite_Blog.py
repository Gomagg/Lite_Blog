from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'f831e89322b30d5f3303386954723dcf'

posts = [
    {
        'author': 'Emmanuel Adeyeye',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 15, 2022'
    },
    {
        'author': 'Christianah Adeyeye',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'November 16, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', tittle='Register', form=form)

@app.route("/login")
def login():
    form = RegistrationForm()
    return render_template('login.html', tittle='login', form=form)

# set FLASK_APP=Lite_Blog.py
# python -m flask run

if __name__ == '__main__':
  app.run(debug=True)