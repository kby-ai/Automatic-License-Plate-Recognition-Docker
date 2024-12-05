import sys
sys.path.append('.')

import os
import base64
import json
from ctypes import *
from alprsdk import initSDK, getLicensePlate, getMachineCode, freeLicenseResults, setActivation
import cv2
import numpy as np
from flask import Flask, request, jsonify


licensePath = "license.txt"
license = ""

machineCode = getMachineCode()
print("\nmachineCode: ", machineCode.decode('utf-8'))

try:
    with open(licensePath, 'r') as file:
        license = file.read().strip()
except IOError as exc:
    print("failed to open license.txt: ", exc.errno)

print("\nlicense: ", license)

ret = setActivation(license.encode('utf-8'))
print("\nactivation: ", ret)

ret = initSDK()
print("init: ", ret)

app = Flask(__name__) 

def mat_to_bytes(mat):
    """
    Convert cv::Mat image data (NumPy array in Python) to raw bytes.
    """
    # Encode cv::Mat as PNG bytes
    is_success, buffer = cv2.imencode(".png", mat)
    if not is_success:
        raise ValueError("Failed to encode cv::Mat image")
    return buffer.tobytes()

@app.route('/alpr', methods=['POST'])
def alpr():
    result = "None"
    license = {}
    box = {}
    
    file = request.files['file']
    
    try:
        image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

    except:
        result = "Failed to open file1"
        response = jsonify({"result": result, "plate number": license, "coordinate": box})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    
    img_byte = mat_to_bytes(image)
    
    recog_array = (c_int * 1024)()  # Assuming a maximum of 256 rectangles
    
    license_plate_ptr = POINTER(c_char_p)()
    cnt = getLicensePlate(img_byte, len(img_byte), byref(license_plate_ptr), recog_array)

    license_plate = [license_plate_ptr[i].decode('utf-8') for i in range(cnt)]
    rectangles = [
    (recog_array[i * 4], recog_array[i * 4 + 1], recog_array[i * 4 + 2], recog_array[i * 4 + 3])
    for i in range(cnt)]

    freeLicenseResults(license_plate_ptr, cnt)
    
    # print("number: ", cnt, rectangles, license_plate)
    if cnt == 0:
        result = "Nothing Detected !"
        response = jsonify({"result": result, "plate number": license, "coordinate": box})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    
    result = "License Plate Number Detected !"
    for i in range(cnt):
        license[f"vehicle {i + 1}"] = license_plate[i]
        box[f"vehicle {i + 1}"] = rectangles[i]
    
    response = jsonify({"result": result, "plate number": license, "coordinate": box})

    response.status_code = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

@app.route('/alpr_base64', methods=['POST'])
def alpr_base64():

    result = "None"
    license = {}
    box = {}
    
    content = request.get_json()

    try:
        imageBase64 = content['base64']
        image_data = base64.b64decode(imageBase64) 
        np_array = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)   
    except:
        result = "Failed to open file1"
        response = jsonify({"result": result, "plate number": license, "coordinate": box})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    

    img_byte = mat_to_bytes(image)
    
    recog_array = (c_int * 1024)()  # Assuming a maximum of 256 rectangles
    
    license_plate_ptr = POINTER(c_char_p)()
    cnt = getLicensePlate(img_byte, len(img_byte), byref(license_plate_ptr), recog_array)

    license_plate = [license_plate_ptr[i].decode('utf-8') for i in range(cnt)]
    rectangles = [
    (recog_array[i * 4], recog_array[i * 4 + 1], recog_array[i * 4 + 2], recog_array[i * 4 + 3])
    for i in range(cnt)]

    freeLicenseResults(license_plate_ptr, cnt)
    
    # print("number: ", cnt, rectangles, license_plate)
    if cnt == 0:
        result = "Nothing Detected !"
        response = jsonify({"result": result, "plate number": license, "coordinate": box})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    
    result = "License Plate Number Detected !"
    for i in range(cnt):
        license[f"vehicle {i + 1}"] = license_plate[i]
        box[f"vehicle {i + 1}"] = rectangles[i]
    
    response = jsonify({"result": result, "plate number": license, "coordinate": box})

    response.status_code = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)