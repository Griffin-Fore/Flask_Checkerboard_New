from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user #importing the entire file, rather than class, to avoid ccircular imports
#There will be other imports need depending what you're trying to use in this file
#You will also need a bycrypt import (we will introduce this week 5)

# Create Users Controller

@app.route('/', defaults = {"rows":8, "columns": 8, "white_color": "white", "black_color": "black"})
@app.route('/<int:rows>', defaults = {"columns": 8, "white_color": "white", "black_color": "black"})
@app.route('/<int:rows>/<int:columns>', defaults = {"white_color": "white", "black_color": "black"})
@app.route('/<int:rows>/<int:columns>/<string:white_color>/<string:black_color>')
def default_checkerboard(rows,columns,white_color,black_color):
    return render_template('checkerboard.html', rows=rows, columns=columns, white_color=white_color, black_color=black_color)

@app.route('/math/<int:num1>/<int:num2>')
def add(num1,num2):
    new_num = num1 + num2
    return render_template('math.html',new_num=new_num)

# Read Users Controller
@app.route('/welcome/<string:name>')
def welcome(name):
    html_page = render_template('welcome.html', name=name)
    print(html_page)
    return html_page

# Update Users Controller

@app.route('/name of path/route goes here!', methods=['POST']) #Post request route
def rename1():
    return redirect('/route path goes here!')

@app.route('/dashboard')
def rename2():
    return render_template('Dashboard html page here!')