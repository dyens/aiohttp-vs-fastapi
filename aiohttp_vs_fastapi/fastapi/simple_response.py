from fastapi import FastAPI

app = FastAPI()


@app.get("/{name}")
async def handle(name: str):
    return {"name": name}
