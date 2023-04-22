
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

#first query select all from table studio
mycursor.execute("SELECT * FROM studio")

firstQ = mycursor.fetchall()

print("-- DISPLAYING Studio RECORDS --")

#print screen each item  
for row in firstQ:
    #formatted to show each item in the tuple 
    print("Studio ID: {}\nStudio Name: {}\n".format(row[0], row[1]))

#Second query select all from table genre
mycursor.execute("SELECT * FROM genre")

secondQ = mycursor.fetchall()

print("-- DISPLAYING Genre RECORDS --")

#print screen ID and genre name 
for row in secondQ:
    #formatted to show ID then genre name
    print("Genre ID: {}\nGenre Name: {}\n".format(row[0], row[1]))


#third query to select film name, film runtime with less than two hours from film table
mycursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime <= 120")

thirdQ = mycursor.fetchall()

print("-- DISPLAYING Short Film RECORDS --")

#added a list too store the results of data pulled 
listThirdQ = []

#loop through the data then stored in a list
for row in thirdQ:
    listThirdQ.append(row)

def Sort_Tuple(tup):
    # method to sort the list in abc order by film name
    return(sorted(tup, key = lambda x: x[0]))

# save the data in a new list
newList = [Sort_Tuple(listThirdQ)]

#Final format of the data 
for row in newList:
    print("Film Name: {}\nRuntime: {}\n".format(row[0][0], row[0][1]))
    print("Film Name: {}\nRuntime: {}\n".format(row[1][0], row[1][1]))


#fourth query select film name, film director - then sort director name by abc order
mycursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")

fourthQ = mycursor.fetchall()

print("-- DISPLAYING Director RECORDS in Order --")

#final display 
for row in fourthQ:
    print("Film Name: {}\nDirector: {}\n".format(row[0], row[1]))


   

