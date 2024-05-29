import mysql.connector

database = mysql.connector.connect(
    host='pokedex-db.c4rkvijebh6q.us-east-1.rds.amazonaws.com',
    user='admin',
    password='12345678',
    database='pokedex'
)