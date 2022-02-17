from fastapi import FastAPI

app = FastAPI()

#TODO: 
@app.get("/")
async def root():
    return {"message": "Hello World"}