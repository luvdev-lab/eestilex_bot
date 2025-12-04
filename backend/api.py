from fastapi import FastAPI

app = FastAPI(title="EestiLex Backend")


@app.get("/ping")
async def ping():
    return {"status": "ok"}
