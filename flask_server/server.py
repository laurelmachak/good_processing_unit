from flask import Flask, render_template, request
#from flask_sqlalchemy import SQLAlchemy
from database import methods

app = Flask(__name__)
# TODO add app.config to connect to a db
#db = SQLAlchemy(app)

@app.route('/')
def index():
    posts = methods.get_all_posts()[0]
    
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contact')
def contact():
    return render_template('contact-us.html')

@app.route('/posts/new', methods = ['POST', 'GET'])
def new_blog_post():
    error = None
    
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        methods.create_post_file(title,body)
        return render_template('index.html')
    else:
        return render_template('new-post.html')

@app.route('/posts/<string:id>/')
def post(id):
    return render_template('show-post.html', id=id, post=methods.get_all_posts()[0][int(id)])
    
if __name__ == "__main__":
    app.run(debug=True)
    


# http://127.0.0.1:5000/
