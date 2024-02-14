from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/webhook/")
async def webhook_receiver(request: Request):
    # 接收请求体作为JSON
    request_body = await request.json()
    # 打印接收到的内容
    print(request_body)
    # 返回确认信息
    return {"message": "Content received"}
