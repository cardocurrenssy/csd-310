"""
 Ricardo Orlando
 Bellevue University
 Module 7 04/22/23
 
 A program that connects to a database and use queries to access the data
 """
import mysql.connector

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

#database connection 
db = mysql.connector.connect(**config)

mycursor = db.cursor()

def show_films(cursor,title):
    # method to execute an inner join all tables,
    #  iterate over the dataset and output the results to the terminal window.

    # inner join query
    cursor.execute("""SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name' FROM film INNER JOIN genre ON
                   film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id""")
    
    # get the results from the cursor object
    films = cursor.fetchall()

    print("\n == {} ==".format(title))

    # iterate over the film data set and display the result
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

# first output
show_films(mycursor,"DISPLAYING FILMS")

# adding a film to the database
mycursor.execute("""INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) 
    VALUES('Renfield', '2023', '155', 'Chris McKay', (SELECT studio_id FROM studio WHERE studio_name = 'Universal Pictures'),(SELECT genre_id FROM genre WHERE genre_name = 'Horror') )""")

# committing the changes 
db.commit()

# second output 
show_films(mycursor, "DISPLAYING FILMS AFTER INSERT")

# updating the genre on Alien
mycursor.execute("UPDATE genre, film SET genre_name = 'Horror' WHERE film_name = 'Alien'")
db.commit()

# displaying the change to the genre 
show_films(mycursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")

#  deleting the gladiator from the table
mycursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")
db.commit()

# third output
show_films(mycursor, "DISPLAYING FILMS AFTER DELETE")




