import mysql.connector

database = mysql.connector.connect(
    host='pokedex.czaawgwka6gl.us-east-1.rds.amazonaws.com',
    user='admin',
    password='12345678',
    database='pokedex'
)