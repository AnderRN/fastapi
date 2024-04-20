from fastapi import FastAPI, HTTPException
import mysql.connector
from core.conexion import connection
from models.user import User

app = FastAPI

@app.get('/listar')
async def listar_user(user: User):
    cursor = connection.cursor()

    query = "SELECT nombre,email,telefono FROM usuarios"
    value = (user.nombre, user.email, user.telefono)

    try:
        cursor.execute(query, value)
        connection.commit()
        return {'message': 'usuario listado'}
    except ValueError as e:
        raise HTTPException(status_code=403, detail=f"Error de campos {err}")
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al listar usuario {err}")
    finally:
        cursor.close()