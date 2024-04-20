from fastapi import FastAPI, HTTPException
import mysql.connector
from core.conexion import connection
from models.user import User

app = FastAPI

@app.put('/actualizar')
async def put_user(user: User):
    cursor = connection.cursor()

    query = "UPDATE usuarios SET nombre, email, telefono VALUE(%S, %S, %S)"
    value = (usuarios.nombre, usuarios.email, usuarios.telefono)

    try:
        cursor.execute(query, value)
        connection.commit()
        return {'message': 'usuario actualizado exitosamente'}
    except ValueError as e:
        raise HTTPException(status_code=403, detail=f"Error de campos {err}")
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al actualizar usuario {err}")
    finally:
        cursor.close()