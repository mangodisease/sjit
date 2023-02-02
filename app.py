from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
import face_recognition
from io import BytesIO
from PIL import Image

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/")
def test():
    return "Testing OK"

@app.post("/encode")
async def encode(
    file: UploadFile = File(...)
):
    print(file)
    image = face_recognition.load_image_file(file)
    encoded = face_recognition.face_encodings(image)[0]

    return {
        "encoded": encoded
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=5000)

