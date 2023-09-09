from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
#from schema.user_schema import Userschema, DataUser
from api_capa_negocios.schema.user_schema import Userschema
from typing import List
from capa_comunicacion.model.user import usuario
user = APIRouter()


@user.get("/")
def root():
    return {"message": "Hola soy una api con ruta, jsjsjs"}


@user.get("/api/user", response_model=List[Userschema])
def get_users():
    obtnertabla = usuario()
    pintartabla = obtnertabla.seleccionarUsuarios()
    return pintartabla


@user.get("/api/user/{user_id}", response_model=Userschema)
def get_user(user_id: str):
    buscar_usuario = usuario()
    obtner_usuario = buscar_usuario.buscarUsuario(user_id)
    return obtner_usuario


@user.post("/api/user", status_code=HTTP_201_CREATED)
def create_user(data_user: Userschema):
    insertar_usuario = usuario()
    resultado = insertar_usuario.insertarUsuario(
        data_user.nombres, data_user.apellidos, data_user.password, data_user.fecha)
  
    return Response(status_code=HTTP_201_CREATED)


@user.put("/api/user/{user_id}", response_model=Userschema)
def update_user(data_update: Userschema, user_id: str):
    actualizar_usuario = usuario()
    resultado = actualizar_usuario.actualizarUsuario(data_update.nombres, data_update.apellidos, data_update.password, user_id)
    return resultado


@user.delete("/api/user/{user_id}", status_code=HTTP_204_NO_CONTENT)
def delete_user(user_id: str):
    eliminar_usuario = usuario()
    resultado = eliminar_usuario.eliminarUsuario(user_id)  
    return Response(status_code=HTTP_204_NO_CONTENT)
