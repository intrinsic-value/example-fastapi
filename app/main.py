"""
1、启动：uvicorn app.main:app --reload
2、postman设定url在environments
3、数据库设定外键，tableThis_tableFK_fkey
4、在.env 设定环境变量，密码等等，修改数据库启动设定
5、sqlalchemy无法自动更新数据表的格式，需要使用alembic 去更新，alembic里面有版本控制
6、
"""


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote


# alembic 可以替代这个部分
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "*",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

"""
import time
import psycopg2
from psycopg2.sql import RealDictCursor
while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="fastapi",
            user="postgres",
            password="rong5807*",
            cursor_factory=RealDictCursor,
        )
        cursor = conn.cursor()
        print("Database connection was successfully")
        break

    except Exception as error:
        print("Database connection was failed!")
        print(error)
        time.sleep(2)    
    

    Returns:
        _type_: _description_
    """


# 路径操作
@app.get("/")  # 根目录就会有反应
def root():
    return {"message": "bind mount works"}


if __name__ == "__main__":
    pass
