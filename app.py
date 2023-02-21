import face_recognition
from flask import Flask, request
from flask_cors import CORS
import numpy as np
from io import BytesIO
from pymongo import MongoClient
import base64

client = MongoClient("mongodb+srv://sjit:pass@attendance.3txyowa.mongodb.net")
#database
db = client["Attendance"]
#tables
students = db.students
teachers = db.teachers
schedule = db.schedule
attendance_log = db.attendance_log
reports = db.reports

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/ping", methods=['GET'])
def ping():
    return "Hello, I am alive", 200

@app.route("/test", methods=['POST'])
def testencode_img():
	try:
		students.insert_one({
		"encoded_img": "test", "img_url": "test"
		})
		
		return {
			"added": True
		}
	except:
		return {
			"added": False
		}
	
@app.route("/encode-img", methods=['POST'])
def encode_img():
	try:
		
		file = request.files['file']
		img_url = base64.b64encode(file.read())
		img = face_recognition.load_image_file(file)
		encoded_img = face_recognition.face_encodings(img)[0]
		students.insert_one({
		"encoded_img": encoded_img
		})
		print(encoded_img)
		return {
			"added": True
		}
	except:
		return {
			"added": False
		}
	
@app.route("/add-student", methods=['POST'])
def add_student():
	try:

		name = request.form["name"]
		course = request.form["course"]
		year_level = request.form["year_level"]
		birthdate = request.form["birthdate"]
		parent_name = request.form["parent_name"]
		parent_contact = request.form["parent_contact"]

		img_url = request.form['img_url']
		encoded_img = request.form['encoded_img']
		students.insert_one({
		"name": name, "course": course, "year_level": year_level, "birthdate": birthdate, 
		"parent_name": parent_name, "parent_contact": parent_contact,
		"encoded_img": encoded_img, "img_url": img_url
		})
		return {
			"added": True
		}
	except:
		return {
			"added": False
		}

if __name__ == "__main__":
	app.run()


