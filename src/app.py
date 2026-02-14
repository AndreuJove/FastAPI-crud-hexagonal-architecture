from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.shared.database import Base, engine
from src.users.infrastructure.port.http.routes import user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router, tags=["Users"], prefix="/api/users")


@app.get("/api/healthchecker")
def root() -> Dict:
    return {"message": "The API is LIVE!!"}
