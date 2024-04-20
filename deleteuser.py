from fastapi import FastAPI, HTTPException
import mysql.connector
from core.conexion import connection
from models.user import User

app = FastAPI

@app.delete('/eliminar')
async def delete_user(user: User):
    cursor = connection.cursor()

    query = "DELETE FROM usuarios WHERE id"
    value = (user.id)

    try:
        cursor.execute(query, value)
        connection.commit()
        return {'message': 'usuario eliminado exitosamente'}
    except ValueError as e:
        raise HTTPException(status_code=403, detail=f"Error de campos {err}")
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al eliminar usuario {err}")
    finally:
        cursor.close()