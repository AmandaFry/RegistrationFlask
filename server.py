#registration 
from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key= 'it is dinner time'

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

NAME_REGEX = re.compile(r'^[a-zA-Z]*$')

						#is there upper case, number, at least 8 charater
PW_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?\d)[A-Za-z\d]{8,}$')

CALENDAR_REGEX = re.compile(r'^(0[1-9]|1[0-2])[- \/\.](0[1-9]|[1-2][0-9]|3[0-1])[- \/\.](19|20)\d\d$')
# (0[1-9]|1[0-2]) 
#
# (0[1-9]
# 	If the first number is 0 then the second number can be 1-9 - takes care of 01- 09
#    |
#    OR
#   	1[0-2])
#   	the first number is 1 then the second number can be 0-2 - takes care of 10-12


# (0[1-9]|[1-2][0-9]|3[0-1])
# (0[1-9]
#  If the first number is 0 then the second number can be 1-9 - take care of 01 - 09
#    |
#    OR
#       [1-2][0-9]
#       If the first number is one or two then the number can be 0-9 - takes care of 10-29
#		   |
# 		   OR
# 			  3[0-1])
# 			  If the first character start with 3 then the second number can be 0-1 - takes care of 30-31

# 
# [- \/\.] 
# this character can be - or / or .
# I need an escape charcter for / and . that ia why it shows as \/ and \. 

# (19|20)\d\d')
# after the first two character is 19 OR 20 the next two charcter can be any number
# need tewo \d \d for number of digit follows but no need to limted to a spacific space



@app.route('/')
def index():
	return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
	is_error = False

	if len(request.form['email']) < 1:
		flash('Email cannot be empty')
		is_error = True
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('email is not valid')
		is_error = True
	elif len(request.form['first_name']) < 2:
		flash('first name cannot be empty')
		is_error = True
	elif not NAME_REGEX.match(request.form['first_name']):
		flash('in valid first name')
		is_error = True
	elif len(request.form['last_name']) < 2:
		flash('last name cannot be empty')
		is_error = True
	elif not NAME_REGEX.match(request.form['last_name']):
		flash('in valid last name')
		is_error = True
	elif len(request.form['password']) < 1:
		flash('password cannot be empty')
		is_error = True
	elif len(request.form['confirm_password']) < 1:
		flash('confirm password cannot be empty')
		is_error = True
	elif not PW_REGEX.match(request.form['password']):
		flash('invalid password')
		is_error = True
	elif not request.form['password'] == request.form['confirm_password']:
		flash('passwords don not match')
		is_error = True
	elif len(request.form['birthday']) < 1:
		flash('bithrday cannot be empty')
		is_error = True
	elif not CALENDAR_REGEX.match(request.form['birthday']):
		flash('not valid birthday')
		is_error = True

	if is_error:
		return redirect('/')
	else:
		flash('Congratulation you are registered')
		return redirect ('/')

app.run(debug=True)