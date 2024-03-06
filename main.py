from fastapi import FastAPI, HTTPException,Request,Form, status
from fastapi.responses import JSONResponse,HTMLResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

app = FastAPI()

# Template setup
templates_directory = os.path.join(os.path.dirname(__file__), 'templates')
templates = Jinja2Templates(directory=templates_directory)

# Static files setup
static_files_path = os.path.join(os.path.dirname(__file__), 'Static')
app.mount("/Static", StaticFiles(directory=static_files_path), name="Static")

# Login page route
@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

#signup page route
@app.get("/signup", response_class=HTMLResponse)
def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

#dashboardd page route
@app.get("/dashboard", response_class=HTMLResponse)
def signup_page(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

#my account page route
@app.get("/account", response_class=HTMLResponse)
def signup_page(request: Request):
    return templates.TemplateResponse("account.html", {"request": request})

#device data stream route
@app.get("/ddstream", response_class=HTMLResponse)
def signup_page(request: Request):
    return templates.TemplateResponse("ddstream.html", {"request": request})

#my shipment page route
@app.get("/myshipment", response_class=HTMLResponse)
def signup_page(request: Request):
    return templates.TemplateResponse("m_shipment.html", {"request": request})

#new shipment page route
@app.get("/newshipment", response_class=HTMLResponse)
def signup_page(request: Request):
    return templates.TemplateResponse("n_shipment.html", {"request": request})

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["SCM"]  # Replace with your MongoDB database name
collection = db["details"]

# Pydantic model for request body
class User(BaseModel):
    username: str
    email: str
    password: str
    confirm_password: str


# Handle signup form submission
# Handle signup form submission
@app.post("/signup")
def sign_up(username: str = Form(...), email: str = Form(...), password: str = Form(...), confirm_password: str = Form(...)):
    # Validate password match
    if password != confirm_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Passwords do not match",
        )

    # Check if the user already exists
    existing_user = collection.find_one({"username": username})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )

    # Insert user into MongoDB
    user_data = {
        "email": email,
        "username": username,
        "password": password,
    }

    result = collection.insert_one(user_data)

    return {"message": "User has been registered successfully"}
# Handle signup form submission
@app.post("/signup")
def sign_up(username: str = Form(...), email: str = Form(...), password: str = Form(...), confirm_password: str = Form(...)):
    # Validate password match
    if password != confirm_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Passwords do not match",
        )

    # Check if the user already exists
    existing_user = collection.find_one({"username": username})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )

    # Insert user into MongoDB
    user_data = {
        "email": email,
        "username": username,
        "password": password,
    }

    result = collection.insert_one(user_data)

    return {"message": "User has been registered successfully"}

    

    
    