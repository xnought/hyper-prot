import uvicorn
from utils import init_fastapi_app, disable_cors, CamelModel

app = init_fastapi_app()
disable_cors(app, ["*"])


@app.get("/test")
def get():
    return {"nice": 1}


class WithinSimilarResponse(CamelModel):
    nodes: list[str]
    edges: list[str]


@app.get("/within-similar", response_model=WithinSimilarResponse)
def within_similar() -> WithinSimilarResponse:
    return WithinSimilarResponse(nodes=[], edges=[])


if __name__ == "__main__":
    uvicorn.run("server:app", host="localhost", port=8000, reload=True)
