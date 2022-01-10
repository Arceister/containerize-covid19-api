from fastapi import FastAPI
from api.routes import daily_router, monthly_router, root, yearly_router

app = FastAPI()

app.include_router(root.router)
app.include_router(yearly_router.router)
app.include_router(monthly_router.router)
app.include_router(daily_router.router)