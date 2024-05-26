import mysql.connector

database = mysql.connector.connect(
    host='pokedex.cnaeq4au0fly.us-east-1.rds.amazonaws.com',
    user='admin',
    password='123698745',
    database='pokedex'
)