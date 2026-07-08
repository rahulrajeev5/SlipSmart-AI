from fastapi import FastAPI

app = FastAPI(
    title="SlipSmart AI API",
    description="Backend API for SlipSmart AI",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to SlipSmart AI 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }