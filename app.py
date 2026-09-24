from fastapi import FastAPI

app = FastAPI(title="Practice API", version="1.0")

@app.get("/")
def read_root():
    return {
        "message": "Python DevOps practice",
        "status": "success",
        "developer": "Стас"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}