from fastapi import FastAPI, UploadFile, File
import uvicorn

app = FastAPI()

@app.get('/ping')
async def ping():
    return 'Hello, I am alive'

@app.post('/ping')
async def predict(file: UploadFile = File(...)):
    bytes = file.read()

if __name__ =="__main__":
    uvicorn.run(app, host='localhost', port=8000)