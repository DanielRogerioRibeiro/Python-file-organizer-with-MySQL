import mysql.connector

meudb = mysql.connector.connect(
    host='localhost', #local de hospedagem
    user='root', #usuriario da pc
    password='admin', #senha dada inicialmente
    database='bancodedados' #dado cadastrado na tabela mysql
)

#Verificar banco de dados antes de criar 
cursor = meudb.cursor()
cursor.execute("SHOW DATABASES LIKE 'bancodedados'")

resultado = cursor.fetchall()

if resultado:
    print("O banco de dados já existe.")
else:
    print("O banco de dados ainda não existe.")
    cursor.execute("CREATE DATABASE bancodedados")