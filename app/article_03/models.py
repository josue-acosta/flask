import os

from flask import request, redirect
from app import app


def allowed_file_types(filename):
    if not "." in filename:
        return False

    extension = filename.rsplit(".", 1)[1]

    if extension.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


def upload_file(uploaded_file):
	uploaded_file = uploaded_file

	if uploaded_file.filename == "":
		print("No filename")
		return redirect(request.url)
		
	if allowed_file_types(uploaded_file.filename):
		uploaded_file.save(os.path.join(app.config["UPLOAD_FILES"], uploaded_file.filename))
		return redirect(request.url)
	else:
		print("That file extension is not allowed")
		return redirect(request.url)