import uvicorn
from fastapi import FastAPI  #type: ignore
from controllers import controllers



app = FastAPI(title="ContasAPI", description="API para gerenciamento de contas")


app.include_router(controllers.router)


if __name__ == '__main__':
  uvicorn.run(app, host='127.0.0.1', port=8080)