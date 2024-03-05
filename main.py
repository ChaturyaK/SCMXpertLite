from fastapi import FastAPI, HTTPException,Request,Form
from fastapi.responses import JSONResponse,HTMLResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

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

