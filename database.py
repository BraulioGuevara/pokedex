import mysql.connector

database = mysql.connector.connect(
    host='pokedex.csibao6zjk83.us-east-1.rds.amazonaws.com',
    user='admin',
    password='12345678',
    database='pokedex'
)