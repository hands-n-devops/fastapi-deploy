from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Demo",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {
        "message": "Hello from FastAPI running on Azure App Service!"
    }


@app.get("/health")
async def health():
    return {
        "status": "Healthy"
    }


@app.get("/hello/{name}")
async def hello(name: str):
    return {
        "message": f"Hello {name}"
    }
