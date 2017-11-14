from flask import Flask, render_template
from database import methods

app = Flask(__name__)

@app.route('/')
def index():
    post_content = methods.get_blog_post('./database/post_01.txt')
    title = post_content[0]
    post = post_content[1]
    filler = methods.dummy_text()
    
    return render_template('index.html', title=title, post=post)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ == "__main__":
    app.run(debug=True)
    


# http://127.0.0.1:5000/
