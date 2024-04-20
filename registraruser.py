from fastapi import FastAPI, HTTPException
import mysql.connector
from core.conexion import connection
from models.user import User

app = FastAPI

@app.post('/registrar')
async def create_user(user: User):
    cursor = connection.cursor()

    query = "INSERT INTO usuarios (id, nombre, email, telefono, password) VALUE(%S, %S, %S, %S, %S)"
    value = (usuarios.id, usuarios.nombre, usuarios.email, usuarios.telefono, usuarios.password)

    try:
        cursor.execute(query, value)
        connection.commit()
        return {'message': 'usuario registrado exitosamente'}
    except ValueError as e:
        raise HTTPException(status_code=403, detail=f"Error de campos {err}")
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al registar usuario {err}")
    finally:
        cursor.close()
