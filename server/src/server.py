import uvicorn
from utils import init_fastapi_app, disable_cors

app = init_fastapi_app()
disable_cors(app)


@app.get("/test")
def get():
    return {"nice": 1}


if __name__ == "__main__":
    uvicorn.run("server:app", host="localhost", port=8000, reload=True)
