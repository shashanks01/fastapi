from fastapi import FastAPI
from fastapi.middleware.cors import  CORSMiddleware


from . import models
from .database import engine, get_db
from .routers import post, user, auth, vote
from .config import settings
#import psycopg2
#from psycopg2.extras import RealDictCursor
#import time


# This creates all the tables at the begining. (used prior to alembic)
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='nimda', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("DB connection was succesful")
#         break
#     except Exception as error:
#         print("Connection to DB has failed.")
#         print(f"Error : {error}")
#         time.sleep(2)


# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello world"}