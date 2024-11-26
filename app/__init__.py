from fastapi import FastAPI
from app.clovaOCR import router as clova_router
app = FastAPI()
app.include_router(clova_router)
