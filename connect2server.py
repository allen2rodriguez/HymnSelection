import os
import mysql.connector

hymndb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "All10202SQL",
    database = "hymns"
)

cursor = hymndb.cursor()