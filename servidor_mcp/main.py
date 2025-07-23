from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import os

app = FastAPI()

# Modelo para entrada de usuario
class Usuario(BaseModel):
    nombre: str
    edad: int
    ciudad: str

# ✅ Endpoint para leer desde CSV
@app.get("/usuario_csv/{nombre}")
def obtener_usuario_csv(nombre: str):
    try:
        df = pd.read_csv("usuarios.csv")
        usuario = df[df["nombre"].str.lower() == nombre.lower()]
        if not usuario.empty:
            return usuario.to_dict(orient="records")[0]
        else:
            return {"error": "Usuario no encontrado en CSV"}
    except Exception as e:
        return {"error": str(e)}

# Nuevo endpoint para agregar al CSV
@app.post("/agregar_usuario")
def agregar_usuario(usuario: Usuario):
    try:
        archivo = "usuarios.csv"
        existe = os.path.exists(archivo)

        nuevo_df = pd.DataFrame([usuario.dict()])
        nuevo_df.to_csv(archivo, mode='a', header=not existe, index=False)

        return {"mensaje": f"Usuario {usuario.nombre} agregado correctamente ✅"}
    except Exception as e:
        return {"error": str(e)}