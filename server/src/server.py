import uvicorn
from utils import init_fastapi_app, disable_cors, CamelModel
from foldseek import Foldseek
from typing import Any
import os

app = init_fastapi_app()
disable_cors(app, ["*"])

VENOME = "/Users/donnybertucci/datasets/venome"
VENOME_FILENAMES = [fn.strip(".pdb") for fn in os.listdir(VENOME)]
FOLDSEEK = os.path.join("..", "exec", "foldseek", "bin", "foldseek")
fs = Foldseek(executable=FOLDSEEK)


class WithinSimilarResponse(CamelModel):
    nodes: list[str]
    edges: list[list[Any]]


@app.get("/within-similar", response_model=WithinSimilarResponse)
def within_similar() -> WithinSimilarResponse:
    nodes = VENOME_FILENAMES
    edges = fs.search(query=VENOME, target=VENOME)
    return WithinSimilarResponse(nodes=nodes, edges=edges)


if __name__ == "__main__":
    uvicorn.run("server:app", host="localhost", port=8000, reload=True)
