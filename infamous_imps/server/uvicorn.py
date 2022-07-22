import uvicorn


def start():
    """Launched with `poetry run dev` at root level"""
    uvicorn.run("infamous_imps.server.api:app", host="0.0.0.0", port=8000, reload=True)
