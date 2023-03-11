from typing import Optional

from fastapi import FastAPI

from config.database import PSQLConfig

app = FastAPI()
psqlConfig = PSQLConfig()
d = psqlConfig.dsn


@app.get("/")
def read_root():
    print(d)
    return {"Hello": d}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
