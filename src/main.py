from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi.responses import RedirectResponse
import random
import os


app = FastAPI()

arg_path    = ["img/leo.jpg", "img/scaloni.jpg", "img/argentina1.jpg", "img/argentina2.jpg"]
france_path = ["img/francia2.jpeg", "img/francia3.webp"] #"img/francia1.jpg"
brasil_path = ["img/brasil.jpg"] #"img/brasil.webp"

@app.get("/")
async def root():
    html_content = """
    <html>
        <head>
        <style>
        body {
            background-image: url('/background');
            background-repeat: no-repeat;
            background-size: 1500px 1000px;
        }

        .button {
            background-color: #4CAF50; /* Green */
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 20px;
            margin: 0;
            position: absolute;
            top: 10%;
            left: 50%;
            -ms-transform: translate(-50%, -50%);
            transform: translate(-50%, -50%);
        }
        </style>
            <title>Who is the champ?</title>
        </head>
        <body>
            <h1 style="color:black; text-align: center; background-color: #e7e7e7;" >Who is the champ?</h1>
            <button class="button" onclick="location.href = '/env';" id="myButton" class="float-left submit-button" >Click here</button>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/argentina", response_class=FileResponse)
async def root():
    return FileResponse(arg_path[random.randint(0, len(arg_path) - 1)])

@app.get("/francia", response_class=FileResponse)
async def root():
    return FileResponse(france_path[random.randint(0, len(france_path) - 1)])

@app.get("/brasil", response_class=FileResponse)
async def root():
    return FileResponse(brasil_path[random.randint(0, len(brasil_path) - 1)])

@app.get("/background", response_class=FileResponse)
def root():
    return FileResponse("img/background2.jpeg")

@app.get("/env", response_class=HTMLResponse)
async def root():
    name = os.getenv("champ")
    return RedirectResponse("/{}".format(name))

@app.get("/host")
async def root():
    import socket
    return {"hostname": socket.gethostname(), 
            "ip": socket.gethostbyname(socket.gethostname())}