# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 03:32:31 2019

@author: Ahmad
"""





"""1"""
from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the Index page'

@app.route('/hello')
def greeting():
    return 'Hello World!'

@app.route('/members')
def mymember():
    return 'Members Page'

if __name__ == '__main__':
    app.run()
    
    
















"""2""" 

# from flask import Flask , render_template
# app = Flask(__name__)

# @app.route('/<int:score>')
# def index(score):
#     return render_template('test1.html',marks=score)


# if __name__ == '__main__':
#     app.run()
   

@app.route('/marks')
@app.route('/marks/')
@app.route('/marks/<mark>')
def mark(mark = 0):
	mark = int(mark)
	if mark >= 90:
		score = 'got A'
	elif mark >= 80 and mark < 90:
		score = 'got B'
	elif mark >= 70 and mark < 80:
		score = 'got C'
	elif mark >= 60 and mark < 70:
		score = 'got D'
	else:
		score = 'failed'
	return render_template('marks.html', title='Marks', score = score)





"""3""" 
from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def index_name():
    return render_template('test2.html')

if __name__ == '__main__':
    app.run()




