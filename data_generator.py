from faker import Faker
from faker.providers import internet
from random import sample, randint, choice

fake = Faker()
fake.add_provider(internet)

f = open('populate_db.sql', 'w')

# generate users data

users = []

for i in range(100):
    user_id = i
    name = fake.name()
    fname = name.split()[0]
    email = fname + "@fakeemail.com"
    phone = fake.phone_number()
    date_joined = "date('" + fake.date() + "')"
    users.append((user_id, name, email, phone, date_joined))
    users_insert = 'INSERT INTO users VALUES (%d, \'%s\', \'%s\', \'%s\', %s);\n' % (user_id, name, email, phone, date_joined)
    f.write(users_insert)

# generate friends data

for i in range(20):
    friend_id = i
    random_lst = sample(range(20), 2)
    friend_insert = 'INSERT INTO friend VALUES (%d, %d, %d);\n' % (friend_id, random_lst[0], random_lst[1])
    f.write(friend_insert)

# generate preferences data

genres = ['Action', 'Comedy', 'Drama', 'Animation', 'Romance', 'Fantasy']

for i in range(100):
    pref_id = i 
    genre = choice(genres)
    user_id = randint(0,99)
    pref_insert = 'INSERT INTO preferences VALUES (%d, \'%s\', %d);\n' % (pref_id, genre, user_id)
    f.write(pref_insert)

# generate entertainment data

f_movies = open('movies.csv', 'r')
movies = f_movies.readlines()
f_movies.close()
movie_id = 0

for line in movies:
    line = line.split(',')
    movie_name = line[0]
    movie_genre = line[1]
    movie_len = randint(20, 180) # random movie length
    movie_desc = fake.text() # random movie desc
    movie_insert = 'INSERT INTO entertainment VALUES (%d, \"%s\", \'%s\', %d, \'%s\');\n' % \
        (movie_id, movie_name, movie_genre, movie_len, movie_desc)
    f.write(movie_insert)
    movie_id += 1

# generate recommendations data

success_options = [True, False]

for i in range(100):
    rec_id = i
    user_id = randint(0,99)
    entertainment_id = randint(0, movie_id-1)
    successful = choice(success_options)
    rec_insert = 'INSERT INTO recommendations VALUES (%d, %d, %d, %s);\n' % \
        (rec_id, user_id, entertainment_id, successful)
    f.write(rec_insert)

# generate data for the following tables:
# user_watched_entertainment, user_favorites_entertainment, user_wants_to_watch_entertainment

for i in range(100):
    prim_id = i
    # user_watched_entertainment
    user_id = randint(0,19)
    entertainment_id = randint(0, movie_id-1)
    watch_insert = 'INSERT INTO user_watched_entertainment VALUES (%d, %d, %d);\n' % \
        (prim_id, user_id, entertainment_id)
    f.write(watch_insert)
    # user_favorites_entertainment
    user_id = randint(0,19)
    entertainment_id = randint(0, movie_id-1)
    fav_insert = 'INSERT INTO user_favorites_entertainment VALUES (%d, %d, %d);\n' % \
        (prim_id, user_id, entertainment_id)
    f.write(fav_insert)
    # user_wants_to_watch_entertainment
    user_id = randint(0,19)
    entertainment_id = randint(0, movie_id-1)
    wants_insert = 'INSERT INTO user_wants_to_watch_entertainment VALUES (%d, %d, %d);\n' % \
        (prim_id, user_id, entertainment_id)
    f.write(wants_insert)
    
# generate user_reviewed_entertainment data

for i in range(1000):
    review_id = i
    rating = randint(1, 5)
    review_text = fake.text()
    user_id = randint(0, 99)
    entertainment_id = randint(0, movie_id-1)
    date_reviewed = "date('" + fake.date() + "')"
    review_insert = 'INSERT INTO user_reviewed_entertainment VALUES (%d, %d, \"%s\", %d, %d, %s);\n' % \
        (review_id, rating, review_text, user_id, entertainment_id, date_reviewed)
    f.write(review_insert)

# generate crew data

for i in range(100):
    crew_id = i
    crew_name = fake.name()
    crew_insert = 'INSERT INTO crew VALUES (%d, \'%s\');\n' % \
        (crew_id, crew_name)
    f.write(crew_insert)

# generate crew_featured_in_entertainment data

for i in range(100):
    feature_id = i
    crew_id = randint(0, 99)
    entertainment_id = randint(0, movie_id-1)
    feature_insert = 'INSERT INTO crew_featured_in_entertainment VALUES (%d, %d, %d);\n' % \
        (feature_id, crew_id, entertainment_id)
    f.write(feature_insert)

# generate website data (might have less than 20 possible streaming sites)

websites = {
    'Hulu': 'https://www.hulu.com',
    'Netflix': 'https://www.netflix.com',
    'Disney Plus': 'https://www.disneyplus.com',
    'ESPN+': 'https://plus.espn.com',
    'Youtube': 'https://youtube.com'
} 
website_id = 0

for key, value in websites.items():
    site_insert = 'INSERT INTO website VALUES (%d, \"%s\", \"%s\");\n' % \
        (website_id, key, value)
    f.write(site_insert)
    website_id += 1

# generate entertainment_can_be_found_on_site data

for i in range(100):
    found_id = i
    site_id = randint(0, website_id-1)
    entertainment_id = randint(0, movie_id-1)
    found_insert = 'INSERT INTO entertainment_can_be_found_on_site VALUES (%d, %d, %d);\n' % \
        (found_id, site_id, entertainment_id)
    f.write(found_insert)