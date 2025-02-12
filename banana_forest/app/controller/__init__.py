from fastapi import APIRouter
from starlette.responses import HTMLResponse

from app.controller.prediction_controller import router as prediction_router

all_routers = APIRouter()
all_routers.include_router(prediction_router)


@all_routers.get("/", response_class=HTMLResponse)
async def root():
    html_content = """
    <html>
        <head>
            <title>Banana Predication Service</title>
        </head>
        <body>
            <h1>Welcome to Banana Predication Service</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
