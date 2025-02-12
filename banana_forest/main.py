import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.controller import all_routers

app = FastAPI(
    description="Banana Predication Service",
    version="1.0",
    title="Banana Predication",
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*"],
)

app.include_router(all_routers)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8006)
