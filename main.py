from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api_capa_negocios.router.router import user

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)

