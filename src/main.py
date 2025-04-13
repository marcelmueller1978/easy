from fastapi import FastAPI

import redis

r = redis.Redis(host="redis123", port=6379)
app = FastAPI()

# import debugpy

# debugpy.listen(("0.0.0.0", 5678))
# print("Waiting for client to attach...")
# debugpy.wait_for_client()


@app.get("/")
def read_root():
    return {"Hello": "World!"}