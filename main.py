from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import uvicorn

app = FastAPI(title="Microservice Gateway", version="1.0.0")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_token(token: str = Depends(oauth2_scheme)):
    if token != "supersecrettoken":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return token

@app.get("/")
def read_root():
    return {"status": "Gateway Operational", "version": "1.0.0"}

@app.get("/secure-data")
def secure_data(token: str = Depends(verify_token)):
    return {"data": "This is protected data routed through the gateway.", "user_id": "admin"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)