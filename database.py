import mysql.connector

database = mysql.connector.connect(
    host='pokedex.c4rkvijebh6q.us-east-1.rds.amazonaws.com',
    user='admin',
    password='123698745',
    database='pokedex'
)