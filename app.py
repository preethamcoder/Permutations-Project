import math
from flask import Flask, render_template, request, request, redirect, send_file, send_from_directory, safe_join, abort
app = Flask(__name__)
def permutationsofword(a):
    uniquelet = set(a.lower())
    perm = math.factorial(len(a))
    for i in uniquelet:
        x = a.count(i)
        perm /= math.factorial(x)
    perms = int(perm)
    return str(perms)
@app.route("/")
def hello():
    return render_template('homepage.php')
@app.route("/?")
def render():
    return render_template('homepage.php')
@app.route("/page1", methods=['GET', 'POST'])
def hi():
    if request.method == 'POST':
        a = request.form['theword']
        fsend = permutationsofword(a)
    return render_template('page1.php', oword = a, permu = fsend)
