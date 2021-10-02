from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)

app.secret_key = "asdsadsd"

@app.route('/')
def index():
    # {"visits": 1} visits is stored in session as a key whose value is 1
    # which is stored in a cookie as a browser
    if 'visits' in session:
        session['visits'] += 1;
        print('key exists!')
    else:
        session['visits'] = 1;
        print("key does NOT exist")
    return render_template('index.html', count = session['visits'])

@app.route('/count')
def increase_count():
    session['visits'] += 1;
    return redirect("/")

@app.route('/destroy_session')
def destroy():
    session.clear();
    return redirect("/")






if __name__=="__main__":
    app.run(debug=True)