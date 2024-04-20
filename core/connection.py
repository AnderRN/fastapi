import mysql.connector 

mysql_config = {
    'user':'root',
    'password':'',
    'host':'localhost',
    'database':'python'
}

connection = mysql.connector.connect(**mysql_config)

def get_connection():
    return connection
