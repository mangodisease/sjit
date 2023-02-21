import face_recognition
from flask import Flask, request
from flask_cors import CORS
import numpy as np
from io import BytesIO
from PIL import Image

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/ping", methods=['GET'])
def ping():
    return "Hello, I am alive", 200

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/encode")
def encode():
    file = request.files['file']
    img = face_recognition.load_image_file(file)
    #img = read_file_as_image(await file.read())
    encoded = face_recognition.face_encodings(img)[0]
    print(encoded)
    
    return {
        "encoded": "k"
    }

if __name__ == "__main__":
	app.run()


