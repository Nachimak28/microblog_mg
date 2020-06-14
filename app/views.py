from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Nachiket'}  # fake user
    posts = [   # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'Avengers is a cool movie'
        },


    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
