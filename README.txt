I. STUDENT INFO
-------------------------
Deepa Borkar
dborkar@uchicago.edu

II. FILES INCLUDED
-------------------------
README.txt
movies.csv
Movies.db
drop_tables.sql 
create_db.sql
populate_db.sql
data_generator.py 
final.py

III. PROJECT DESCRIPTION
-------------------------
For this project, I created a web page that displays users that are able to review movies. The web page allows a person to see all the users that are on the website and also their reviews of the movies. The web page also allows users to add new reviews for movies. 

RelationX: users 
RelationY: user_reviewed_entertainment

IV. HOW TO RUN PROGRAM
-------------------------
Movies.db is already populated with data to run the website.

The following is how to run the website:
    python3 final.py

The following are how to populate the Movies.db file needed for the website (not necessary to run):
    cat create_db.sql | sqlite3 Movies.db 
    cat populate_db.sql | sqlite3 Movies.db

V. DESCRIPTION OF WEB PAGES
-------------------------

http://localhost:8080/
This is the landing page and just provides a link to go to the home page.

http://localhost:8080/home
This is where searches can be done in order to find users. The wildcard search attribute is the Name attribute, while the e-mail search must be exact.

http://localhost:8080/users/<user_id>
This is where a person can view or edit information about a specific user. If the update is successful, it will be displayed on the screen after hitting the 'Update' button. 

http://localhost:8080/delete/<user_id>
The delete button in a search will delete the user from the database. This link will also give an option to return to the home page.

http://localhost:8080/showreviews/<user_id>
The show users button in a search will allow you to see all the reviews that the specific user has posted.

http://localhost:8080/addreview/<user_id>
The add review button in a search will allow you to see all the reviews that the specific user has posted and also add a new review for that specific user. When the 'Add Review' button is hit, the new review will automatically show on the page.

http://localhost:8080/addusers
This link is shown under the Links header on the home page and allows you to add a new user to the database. This link brings you to a form to add the user. The Name attribute is required. All other attributes are optional and if the date joined is not specified, the date chosen will be today. 

VI. QUESTIONS
-------------------------
For any questions or issues, please e-mail dborkar@uchicago.edu.

