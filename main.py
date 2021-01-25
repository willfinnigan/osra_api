from fastapi import FastAPI, File, UploadFile
import os
import subprocess as sp
import shutil
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/process_image")
def process_image(image: UploadFile = File(...)):
    if image.filename.endswith('.png'):
        with open('image.png', "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        cmd = f"osra image.png"
        output = sp.run(cmd, shell=True, capture_output=True)
        smi_byte_string = output.stdout
        list_smi = smi_byte_string.decode().split('\n')
        if "" in list_smi:
            list_smi.remove("")
        os.remove('image.png')
        return list_smi
    return 'File must end with png'