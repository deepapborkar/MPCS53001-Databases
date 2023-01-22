from bottle import route, run, request
import sqlite3

# Start Connection with SQL DB
con = sqlite3.connect('Movies.db')
cur = con.cursor()

# FUNCTIONS

def display_links_homepage():
    html = ''
    # display links to click in a table
    html += "<h3>Links</h3>"
    html += "<table>"
    html += "<tr>"
    html += "<td> New Users: </td>"
    html += "<td> <a href=/addusers>Link for Adding Users</a> </td>"
    html += "</tr>"
    html += "<tr>"
    html += "<td> Current Users: </td>"
    html += "<td> <a href=/users>Link for All Users</a> </td>"
    html += "</tr>"
    html += "<tr>"
    html += "<td> Current Movies: </td>"
    html += "<td> <a href=/movies>Link for All Movies</a> </td>"
    html += "</tr>"
    html += "</table>"
    return html

def display_search_results(query):
    html = ''
    html += "<table>"
    html += "  <tr> <th>User Name</th> <th>User Email</th> <th>View / Edit</th> <th>Delete</th> <th>Show Reviews</th> <th>Add Review</th> </tr>"
    for row in cur.execute(query):
        html += "<tr>"
        html += "<td>" + row[1] + "</td>"
        html += "<td>" + row[2] + "</td>"
        html += "<td>" + "<a href=/users/" + str(row[0]) + ">View / Edit</a>" + "</td>"
        html += "<td>" + "<a href=/delete/" + str(row[0]) + ">Delete</a>" + "</td>"
        html += "<td>" + "<a href=/showreviews/" + str(row[0]) + ">Show Reviews</a>" + "</td>"
        html += "<td>" + "<a href=/addreview/" + str(row[0]) + ">Add Review</a>" + "</td>"
        html += "</tr>"
    html += "</table>"
    return html

def display_user_info(id):
    html = ""
    user = cur.execute('select * from users where user_id =' + id + ";")
    # display the user's info
    for u in user:
        html += "<h1>" + str(u[1]) + "</h1>"
        html += "<table>"
        html += "<tr>"
        html += "<td> Email: </td>"
        html += "<td>" + str(u[2]) + "</td>"
        html += "</tr>"
        html += "<tr>"
        html += "<td> Phone Number: </td>"
        html += "<td>" + str(u[3]) + "</td>"
        html += "</tr>"
        html += "<tr>"
        html += "<td> Date Joined: </td>"
        html += "<td>" + str(u[4]) + "</td>"
        html += "</tr>"
        html += "</table>"
    return html

def display_user_reviews(id):
    html = ''
    # display user's reviews
    html += "<h1> User Reviews </h1>"
    query = '''select review_id, rating, review_text, user_id, name, date_reviewed 
    from user_reviewed_entertainment join entertainment using (entertainment_id)
    where user_id =''' + id + ''' order by date_reviewed desc;'''
    for review in cur.execute(query):
        html += "<table>"
        html += "<tr>"
        html += "<td> <b> Review ID: </b> </td>"
        html += "<td> <b>" + str(review[0]) + "</b> </td>"
        html += "</tr>"
        html += "<tr>"
        html += "<td> Movie: </td>"
        html += "<td>" + str(review[4]) + "</td>"
        html += "</tr>"
        html += "<tr>"
        html += "<td> Date Reviewed: </td>"
        html += "<td>" + str(review[5]) + "</td>"
        html += "</tr>"
        html += "<tr>"
        html += "<td> Rating: </td>"
        html += "<td>" + str(review[1]) + "</td>"
        html += "</tr>"
        html += "<tr>"
        html += "<td> Review Text: </td>"
        html += "<td>" + str(review[2]) + "</td>"
        html += "</tr>"
        html += "</table>"
    return html

def display_form_search_users():
    html = ''
    # search functionality
    html += "<h3>Search Users</h3>"
    html += '''
    <form action="/home" method="post">
    <label for="name">Name(*):</label><br>
    <input type="text" id="name" name="name" value=""><br>
    <label for="email">Email:</label><br>
    <input type="text" id="email" name="email" value=""><br><br>
    <input type="submit" value="Search">
    </form> 
    '''
    return html

def display_form_edit_user(id):
    html = ''
    # form for editing user
    html += "<h2>Input User Info Changes</h2>"
    html += '''
    <form action="/users/''' + id + '''" method="post">
    <label for="name">Name:</label><br>
    <input type="text" id="name" name="name" value=""><br><br>
    <label for="email">Email:</label><br>
    <input type="text" id="email" name="email" value=""><br><br>
    <label for="number">Phone Number:</label><br>
    <input type="text" id="number" name="number" value=""><br><br>
    <label for="date">Date Joined:</label><br>
    <input type="date" id="date" name="date" value=""><br><br>
    <input type="submit" value="Update">
    </form> 
    '''
    return html

def display_form_add_user():
    html = ''
    # form for editing user
    html += "<h2>Input New User Info</h2>"
    html += '''
    <form action="/addusers" method="post">
    <label for="name">Name (Required):</label><br>
    <input type="text" id="name" name="name" value=""><br><br>
    <label for="email">Email:</label><br>
    <input type="text" id="email" name="email" value=""><br><br>
    <label for="number">Phone Number:</label><br>
    <input type="text" id="number" name="number" value=""><br><br>
    <label for="date">Date Joined:</label><br>
    <input type="date" id="date" name="date" value=""><br><br>
    <input type="submit" value="Add User">
    </form> 
    '''
    return html

def display_form_movie_review(id):
    html = ''
    # display entertainment review form
    query = 'select name from entertainment order by name asc;'
    html += "<h2>Input Movie Review</h2>"
    html += '''
    <form action="/addreview/''' + id + '''" method="post">
    <label for="name">Movie Name:</label><br>
    <select id="name" name="name" value=""><br>
    '''
    for movie in cur.execute(query):
        html += '''<option value="''' + movie[0] + '''">''' + movie[0] + '''</option>'''
    html += '''
    </select> <br><br>
    <label for="rating">Rating:</label><br>
    <select id="rating" name="rating" value=""><br>
    <option value="1">1</option>
    <option value="2">2</option>
    <option value="3">3</option>
    <option value="4">4</option>
    <option value="5">5</option>
    </select><br><br>
    <label for="review">Review:</label><br>
    <input style="width:400px;" type="text" id="review" name="review" value=""><br><br>
    <input type="submit" value="Add Review">
    </form> 
    '''
    return html

# ROUTING FUNCTIONS

@route('/')
def landing_page():
    # go to home
    html = "<h1> <a href=/home>Go to Home Page</a> </h1>"
    return html

@route('/home')
# HOME PAGE (0)
def home_page():
    # header
    html = "<h1> Home Page </h1>"

    # search functionality
    html += display_form_search_users()

    # display links to click in a table
    html += display_links_homepage()
    return html

@route('/home', method = 'POST')
# HOME PAGE (0)
def search():
    # header
    html = "<h1> Home Page </h1>"

    # search functionality
    html += display_form_search_users()

    # get the form inputs
    name = request.forms.get('name')
    email = request.forms.get('email')
    html += 'Results for Name: '
    html += name 
    html += ' and Email: '
    html += email

    # RETURN SEARCH RESULTS (1)
    html += "<h3>Results</h3>"
    # return all results for empty search
    if len(name) == 0 and len(email) == 0:
        query = 'select user_id, name, email from users order by name asc limit 20;'
        html += display_search_results(query)
    # case where only name is searched
    elif len(name) != 0 and len(email) == 0:
        query = 'select user_id, name, email from users where name like \'%' + name + '%\' order by name asc limit 20;'
        html += display_search_results(query)
    # case where only email is searched
    elif len(name) == 0 and len(email) != 0:
        query = 'select user_id, name, email from users where email = \'' + email + '\' order by name asc limit 20;'
        html += display_search_results(query)
    else:
        query = 'select user_id, name, email from'
        query += '(select user_id, name, email from users where name like \'%' + name + '%\''
        query += 'INTERSECT select user_id, name, email from users where email = \'' + email + '\')'
        query += 'order by name asc limit 20;'
        html += display_search_results(query)
        

    # display links to click in a table
    html += display_links_homepage()
    return html 

@route('/users/<id>')
# VIEW EDIT USER INFO (2)
def specific_user_information(id):
    html = ""

    # display the users info at the top of page
    html += display_user_info(id)
    
    # form for editing user
    html += display_form_edit_user(id)

    # return home
    html += "<br><br><a href=/home>Return Home</a>"
    return html

@route('/users/<id>', method = 'POST')
# VIEW EDIT USER INFO (2)
def edit_specific_user_information(id):
    # edit user info
    name = request.forms.get('name')
    email = request.forms.get('email')
    number = request.forms.get('number')
    date = request.forms.get('date')
    # update name
    if (len(name) > 0) and (len(name.replace(' ', '')) > 0):
        query = '''update users set name = \"''' + name + '''\" where user_id =''' + id + ''';'''
        cur.execute(query)
        con.commit()
    # update email
    if len(email) > 0:
        query = '''update users set email = \"''' + email + '''\" where user_id =''' + id + ''';'''
        cur.execute(query)
        con.commit()
    # update phone number
    if len(number) > 0:
        query = '''update users set phone_number = \'''' + number + '''\' where user_id =''' + id + ''';'''
        cur.execute(query)
        con.commit()
    # update date joined
    if len(date) > 0:
        query = '''update users set date_joined = date(\'''' + date + '''\') where user_id =''' + id + ''';'''
        cur.execute(query)
        con.commit()
    
    html = ""

    # display the user's info
    html += display_user_info(id)
    
    # form for editing user
    html += display_form_edit_user(id)

    # return home
    html += "<br><br><a href=/home>Return Home</a>"
    return html

@route('/delete/<id>')
# DELETE USER (3)
def delete_user(id):
    html = ""

    # display the user that will be deleted
    user = cur.execute('select * from users where user_id =' + id + ";")
    for u in user:
        html += str(u[1]) + " has been deleted."
    
    # delete the user
    query = 'delete from users where user_id = ' + id + ';'
    cur.execute(query)
    con.commit()
    
    # return home
    html += "<br><br><a href=/home>Return Home</a>"
    return html

@route('/showreviews/<id>')
# SHOW USERS REVIEWS (4)
def show_user_reviews(id):
    html = ""

    # display the user's info
    html += display_user_info(id)

    # display user's reviews
    html += display_user_reviews(id)
    
    # return home
    html += "<br><br><a href=/home>Return Home</a>"
    return html

@route('/addreview/<id>')
# ADD MOVIE REVIEW (5)
def add_review(id):
    html = ""
    
    # display the user's info
    html += display_user_info(id)
    
    # display entertainment review form
    html += display_form_movie_review(id)
    
    # display user's reviews
    html += display_user_reviews(id)

    # return home
    html += "<br><br><a href=/home>Return Home</a>"
    return html

@route('/addreview/<id>', method = 'POST')
# ADD REVIEW (5)
def add_new_review(id):
    html = ""
    
    # display the user's info
    html += display_user_info(id)
    
    # add the new review for the user to the database
    user_id = int(id)
    date_reviewed = "date('now')"
    movie_name = request.forms.get('name')
    movie_rating = int(request.forms.get('rating'))
    movie_review = request.forms.get('review')
    movie_id_query = 'select entertainment_id from entertainment where name = \'' + movie_name + '\';'
    movie_id = int(cur.execute(movie_id_query).fetchall()[0][0])
    query_insert = 'insert into user_reviewed_entertainment (rating, review_text, user_id, entertainment_id, date_reviewed) values(%d, \"%s\", %d, %d, %s);' % \
        (movie_rating, movie_review, user_id, movie_id, date_reviewed)
    cur.execute(query_insert)
    con.commit()

    # display entertainment review form
    html += display_form_movie_review(id)

    # display user's reviews
    html += display_user_reviews(id)

    # return home
    html += "<br><br><a href=/home>Return Home</a>"
    return html

@route('/addusers')
# ADD A NEW USER (6)
def add_user():
    html = ''

    # display the form the add a user
    html += display_form_add_user()

    # return home
    html += "<br><br><a href=/home>Return Home</a>"
    return html

@route('/addusers', method = 'POST')
# ADD A NEW USER (6)
def add_user():
    html = ''

    # display the form to add a user
    html += display_form_add_user()

    # add the user
    name = request.forms.get('name')
    email = request.forms.get('email')
    number = request.forms.get('number')
    date = request.forms.get('date')
    if len(date) == 0:
        # put in current date if the date is empty
        date = "date('now')"
    else:
        # convert date to sql language
        date = '''date(\'''' + date + '''\')'''

    # query to add the user
    if (len(name) == 0) or (len(name.replace(' ', '')) == 0):
        # return error message
        html += '<p style = "color:red;"> User Name is Required. </p>'
    else: 
        # insert the user to the database
        query_insert = 'insert into users (name, email, phone_number, date_joined) values(\"%s\", \"%s\", \"%s\", %s);' % \
        (name, email, number, date)
        cur.execute(query_insert)
        con.commit()
        html += '<p>' + name + ' was added to the database.</p>'

    # return home
    html += "<br><br><a href=/home>Return Home</a>"
    return html

# FUNCTIONS FROM P7 ASSIGNMENT

@route('/users')
def user_information():
    # user header
    html = "<h1> User Information </h1>"
    # display a table of user information
    html += "<table>"
    html += "  <tr> <th>User Name</th> <th>Link</th> </tr>"
    for row in cur.execute('select user_id, name from users order by name asc;'):
        html += "<tr>"
        html += "<td>" + row[1] + "</td>"
        html += "<td>" + "<a href=/users/" + str(row[0]) + ">More Info</a>" + "</td>"
        html += "</tr>"
    html += "</table>"
    # return home
    html += "<br><br><a href=/home>Return Home</a>"
    return html

@route('/movies')
def movie_information():
    # user header
    html = "<h1> Movie Information </h1>"
    # display a table of movie information
    html += "<table>"
    html += "  <tr> <th>Movie Name</th> <th>Link</th> </tr>"
    for row in cur.execute('select entertainment_id, name from entertainment order by name asc;'):
        html += "<tr>"
        html += "<td>" + row[1] + "</td>"
        html += "<td>" + "<a href=/movies/" + str(row[0]) + ">More Info</a>" + "</td>"
        html += "</tr>"
    html += "</table>"
    # return home
    html += "<br><br><a href=/home>Return Home</a>"
    return html

@route('/movies/<id>')
def specific_movie_information(id):
    html = ""
    movie = cur.execute('select * from entertainment where entertainment_id =' + id + ";")
    # display the movie info
    for m in movie:
        html += "<h1>" + m[1] + "</h1>"
        html += "<table>"
        html += "<tr>"
        html += "<td> Genre: </td>"
        html += "<td>" + m[2] + "</td>"
        html += "</tr>"
        html += "<tr>"
        html += "<td> Length: </td>"
        html += "<td>" + str(m[3]) + "</td>"
        html += "</tr>"
        html += "<tr>"
        html += "<td> Description: </td>"
        html += "<td>" + m[4] + "</td>"
        html += "</tr>"
        html += "</table>"
    # return to movies
    html += "<br><br><a href=/movies>Return to Movies</a>"
    # return home
    html += "<br><br><a href=/home>Return Home</a>"
    return html

# MAIN PROGRAM

run(host = 'localhost', port=8080, debug = True)