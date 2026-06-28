from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.github import router as github_router

from app.api.reviews import router as reviews_router
from app.api.stats import router as stats_router
from app.api.review_details import (
    router as review_details_router
)
from app.api.report import router as report_router


app = FastAPI()

# ==========================================
# CORS MIDDLEWARE - CRITICAL FIX
# ==========================================
# This allows the frontend to communicate with the backend
# from different origins (localhost:3000 to localhost:8000)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",      # Local development
        "http://localhost:3001",      # Alternative local port
        "http://127.0.0.1:3000",      # Local IP variant
        "http://127.0.0.1:3001",      # Local IP variant
        # For production, add your actual frontend URL:
        # "https://yourdomain.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],              # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],              # Allow all headers
)

# ==========================================
# ROUTERS
# ==========================================

app.include_router(
    github_router
)

app.include_router(
    reviews_router
)

app.include_router(
    stats_router
)

app.include_router(
    review_details_router
)

app.include_router(
    report_router
    )


@app.get("/")
def home():

    return {
        "message":
        "AI Code Review Agent"
    }