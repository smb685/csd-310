import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",  # or your MySQL username
    password="March.03031994",  # your MySQL password
    database="movies"
)


cursor = db.cursor()

# Query 1: Select all fields from the studio table
print("STUDIO RECORDS")
cursor.execute("SELECT * FROM studio")
studios = cursor.fetchall()
for studio in studios:
    print(f"Studio ID: {studio[0]}, Name: {studio[1]}")
print()

# Query 2: Select all fields from the genre table
print("GENRE RECORDS")
cursor.execute("SELECT * FROM genre")
genres = cursor.fetchall()
for genre in genres:
    print(f"Genre ID: {genre[0]}, Name: {genre[1]}")
print()

# Query 3: Movies under 2 hours
print("MOVIES WITH RUNTIME UNDER 2 HOURS")
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
short_films = cursor.fetchall()
for film in short_films:
    print(f"Film: {film[0]}, Runtime: {film[1]} minutes")
print()

# Query 4: Films grouped by director
print("FILMS GROUPED BY DIRECTOR")
cursor.execute("SELECT film_director, GROUP_CONCAT(film_name SEPARATOR ', ') FROM film GROUP BY film_director")
directors = cursor.fetchall()
for director in directors:
    print(f"Director: {director[0]}, Films: {director[1]}")

# Close connection
db.close()
