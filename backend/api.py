from fastapi import FastAPI

# импортируем корректные подключения
from backend.db.mongo import db
from backend.db.redis_client import redis_client

app = FastAPI(title="EestiLex Backend")


@app.get("/ping")
async def ping():
    return {"status": "ok"}


@app.get("/mongo-test")
async def mongo_test():
    # пишем документ
    result = await db.test.insert_one({"hello": "world"})

    # читаем его обратно
    doc = await db.test.find_one({"_id": result.inserted_id})

    # аккуратный JSON-ответ
    return {
        "id": str(doc["_id"]),   # ObjectId → строка
        "hello": doc.get("hello"),
    }


@app.get("/redis-test")
async def redis_test():
    # записываем ключ
    await redis_client.set("test", "123")

    # читаем его обратно
    value = await redis_client.get("test")

    return {
        "redis": "ok",
        "value": value,
    }


