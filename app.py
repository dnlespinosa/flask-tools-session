from flask import Flask, request, render_template, redirect, flash,  jsonify, session
from surveys import Question, Survey

app = Flask(__name__)
app.secret_key = 'its a secret'

responses = []

@app.route('/')
def home_page():
    session['responses']=[]
    return render_template('home.html')

@app.route('/answer', methods=['POST'])
def answered():
    answer = request.form['answer']
    responses.append(answer)
    if (len(responses) == 4):
        return redirect('/question/4')
    else:
        return redirect(f'/question/{len(responses)}')

@app.route('/question/0')
def question_0():
    return render_template('questions-0.html')

@app.route('/question/1')
def question_1():
    if (len(responses) != 1):
        return redirect('/question/0')
    return render_template('questions-1.html')
    

@app.route('/question/2')
def question_2():
    if (len(responses) != 2):
        return redirect(f'/question/{len(responses)}')
    return render_template('questions-2.html', responses=responses)

@app.route('/question/3')
def question_3():
    if (len(responses) != 3):
        return redirect(f'/question/{len(responses)}')
    return render_template('quesitons-3.html', responses=responses)

@app.route('/question/4')
def question_4():
    if (len(responses) != 4):
        return redirect(f'/question/{len(responses)}')
    session['responses'] = responses
    return render_template('questions-4.html', responses=responses)

@app.route('/reset')
def reset():
    responses = []
    return redirect('/')

