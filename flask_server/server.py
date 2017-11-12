from flask import Flask, render_template
import content

app = Flask(__name__)

@app.route('/')
def index():
    username = "pingu"
    filler = content.dummy_text()
    
    return render_template('index.html', filler=filler)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ == "__main__":
    app.run(debug=True)


# http://127.0.0.1:5000/
