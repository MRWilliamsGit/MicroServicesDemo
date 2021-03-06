from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello There Friend!"}

@app.get("/adder/{num1}/{num2}")
def adder(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}

@app.get("/hey/{nm}")
def hey(nm: str):
    return {"message": "You have a nice name, "+nm+"!"}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')