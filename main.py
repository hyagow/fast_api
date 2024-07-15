import uvicorn
from fastapi import FastAPI  #type: ignore
from controllers import controllers



app = FastAPI()

@app.get('/')
def hello_world():
  return 'Hello World'

app.include_router(controllers.router)


if __name__ == '__main__':
  uvicorn.run(app, host='127.0.0.1', port=8080)