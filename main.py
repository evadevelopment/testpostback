import os
from jose import jwt
from fastapi import FastAPI, Form, HTTPException
from typing import Optional
import uvicorn

app = FastAPI()

secret_key = os.environ.get("ULTRA_SECRET_KEY")

@app.get("/test")
async def handle_test():
    return {"message": "TEST OK"}


@app.post("/")
async def handle_postback(
    status: Optional[str] = Form(None),
    invoice_id: Optional[str] = Form(None),
    amount_crypto: Optional[str] = Form(None),
    currency: Optional[str] = Form(None),
    order_id: Optional[str] = Form(None),
    token: Optional[str] = Form(None)
):
    print(status, invoice_id, amount_crypto, currency, order_id, token)
    try:
        if token:
            # decoded = jwt.decode(token, secret_key, algorithms=['HS256'])
            decoded = "itried"
        else:
            raise HTTPException(status_code=400, detail="Token is required")

        print(f"Payment status: {status}\n" \
                   f"Invoice ID: {invoice_id}\n" \
                   f"Amount in crypto: {amount_crypto} {currency}\n" \
                   f"Order ID: {order_id}\n" \
                   f"Decoded: {decoded}\n")

        return {"message": "Postback received"}
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
