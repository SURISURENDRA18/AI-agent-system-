
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from graph.workflow import graph

app = FastAPI()



class QueryRequest(BaseModel):
    query: str


@app.post("/run")
def run(request: QueryRequest):
    try:
        result = graph.invoke({"query": request.query})

        return {
            "research": result.get("research"),
            "analysis": result.get("analysis"),
            "draft": result.get("draft"),
            "final": result.get("final")
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))