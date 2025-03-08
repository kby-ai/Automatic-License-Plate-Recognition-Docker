<p align="center">
  <a href="https://play.google.com/store/apps/dev?id=7086930298279250852" target="_blank">
    <img alt="" src="https://github-production-user-asset-6210df.s3.amazonaws.com/125717930/246971879-8ce757c3-90dc-438d-807f-3f3d29ddc064.png" width=500/>
  </a>  
</p>

### Our facial recognition algorithm is globally top-ranked by NIST in the FRVT 1:1 leaderboards. <span><img src="https://github.com/kby-ai/.github/assets/125717930/bcf351c5-8b7a-496e-a8f9-c236eb8ad59e" alt="badge" width="36" height="20"></span>  
[Latest NIST FRVT evaluation report 2024-12-20](https://pages.nist.gov/frvt/html/frvt11.html)  

![FRVT Sheet](https://github.com/user-attachments/assets/16b4cee2-3a91-453f-94e0-9e81262393d7)

#### 🆔 ID Document Liveness Detection - Linux - [Here](https://web.kby-ai.com)  <span><img src="https://github.com/kby-ai/.github/assets/125717930/bcf351c5-8b7a-496e-a8f9-c236eb8ad59e" alt="badge" width="36" height="20"></span>
#### 🤗 Hugging Face - [Here](https://huggingface.co/kby-ai)
#### 📚 Product & Resources - [Here](https://github.com/kby-ai/Product)
#### 🛟 Help Center - [Here](https://docs.kby-ai.com)
#### 💼 KYC Verification Demo - [Here](https://github.com/kby-ai/KYC-Verification-Demo-Android)
#### 🙋‍♀️ Docker Hub - [Here](https://hub.docker.com/r/kbyai/license-plate-recognition)
```bash
sudo docker pull kbyai/license-plate-recognition:latest
sudo docker run -v ./license.txt:/home/openvino/kby-ai-alpr/license.txt -p 8081:8080 -p 9001:9000 kbyai/license-plate-recognition:latest
```
# Automatic-License-Plate-Recognition

## Overview

This repository demonstrates  `ANPR/ALPR(Automatic Number/License Plate Recognition)` SDK with unmatched accuracy and precision by applying `SOTA(State-of-the-art)` deep learning techniques. </br>
`KBY-AI`'s `LPR` solutions utilizes artificial intelligence and machine learning to greatly surpass legacy solutions. Now, in real-time, users can receive a vehicle's plate number through `API`.
> We can customize the `SDK` to align with customer's specific requirements.
> 
The `ALPR` system consists of the following steps:
- Vehicle image capture
- Preprocessing
- Vehicle detection
- Number plate extraction
- Charater segmentation
- Optical Character Recognition(OCR) </br>

The `ALPR` system works in these strides, the initial step is the location of the vehicle and capturing a vehicle image of front or back perspective of the vehicle, the second step is the localization of Number Plate and then extraction of vehicle Number Plate is an image. The final stride uses image segmentation strategy, for the segmentation a few techniques neural network, mathematical morphology, color analysis and histogram analysis. Segmentation is for individual character recognition. Optical Character Recognition (OCR) is one of the strategies to perceive the every character with the assistance of database stored for separate alphanumeric character.


### ◾License Plate Recognition SDK Product List
  | No.      | Repository | SDK Details | Status |
  |------------------|------------------|------------------|------------------|
  | ➡️        | <b>[LPR - Linux](https://github.com/kby-ai/Automatic-License-Plate-Recognition-Docker)</b>    | <b>License Plate Recognition Linux SDK</b> | <b>Available</b> |
  | 2        | [LPR - Docker](https://hub.docker.com/r/kbyai/license-plate-recognition)    | License Plate Recognition Docker Image | Available |
  | 3        | [LPR - Flutter](https://github.com/kby-ai/Automatic-License-Plate-Recognition-Flutter)    | License Plate Recognition Flutter SDK | Available |
  | 4        | [LPR - C#](https://github.com/kby-ai/Automatic-License-Plate-Recognition-CSharp-.NET)    | License Plate Recognition C# SDK | Available |
  | 5        | LPR - Android    | License Plate Recognition Android SDK | Developing |
  | 6        | LPR - iOS    | License Plate Recognition iOS SDK | Developing |

> To get more products, please visit products [here](https://github.com/kby-ai):<br/>

## Try the API
## Online Demo
To try `KBY-AI` `ALPR` online, please visit [here](https://web.kby-ai.com/)
> Please select tab 'ALPR/ANPR` for this `SDK`
  ![image](https://github.com/user-attachments/assets/3e63c286-f3d6-4bf4-80b7-22139eaec003)

### Postman
  The `API` can be evaluated through `Postman` tool. Here are the endpoints for testing:
  - Test with an image file: Send a `POST` request to `http://89.116.159.229:8085/alpr`.
  - Test with a `base64-encoded` image: Send a `POST` request to `http://89.116.159.229:8085/alpr_base64`.
  ![image](https://github.com/user-attachments/assets/a434f9f7-9efb-4c66-a1ea-c728a8074458)

## SDK License
This project demonstrates `KBY-AI`'s `License Plate Recognition Server SDK`, which requires a license per machine.</br>
- The code below shows how to use the license: https://github.com/kby-ai/Automatic-License-Plate-Recognition-Docker/blob/06a13d653646b9b123e5d164c18af9ae13351d53/app.py#L17-L28
- To request the license, please provide us with the `machine code` obtained from the `getMachineCode` function.</br>
#### Please contact us:</br>
🧙`Email:` contact@kby-ai.com</br>
🧙`Telegram:` [@kbyai](https://t.me/kbyai)</br>
🧙`WhatsApp:` [+19092802609](https://wa.me/+19092802609)</br>
🧙`Skype:` [live:.cid.66e2522354b1049b](https://join.skype.com/invite/OffY2r1NUFev)</br>
🧙`Discord:` [KBY-AI](https://discord.gg/CgHtWQ3k9T)</br>
🧙`Teams:` [KBY-AI](https://teams.live.com/l/invite/FAAYGB1-IlXkuQM3AQ)</br>

## How to run

### 1. System Requirements
  - `CPU`: 2 cores or more (Recommended: 2 cores)
  - `RAM`: 4 GB or more (Recommended: 8 GB)
  - `HDD`: 4 GB or more (Recommended: 8 GB)
  - `OS`: `Ubuntu 20.04` or later
  - Dependency: `OpenVINO™ Runtime` (Version: 2022.3)

### 2. Setup and Test
  - Clone the project:
    ```bash
    git clone https://github.com/kby-ai/Automatic-License-Plate-Recognition-Docker.git
    ```
    ```bash
    cd Automatic-License-Plate-Recognition-Docker
    ```
  - Build the `Docker` image:
    ```bash
    sudo docker build --pull --rm -f Dockerfile -t kby-ai-alpr:latest .
    ```
  - Run the `Docker` container:
    ```bash
    sudo docker run -v ./license.txt:/home/openvino/kby-ai-alpr/license.txt -p 8081:8080 -p 9001:9000 kby-ai-alpr
    ```
  - Send us the `machine code` and then we will give you a license key to make the `SDK` activate.
  
    After that, update the `license.txt` file by overwriting the `license key` that you received. Then, run the `Docker` container again.

    ![image](https://github.com/user-attachments/assets/e718a509-85da-469f-b491-27b99063d0ec)
    
    ![image](https://github.com/user-attachments/assets/cb2806e0-93be-4b0a-be9f-713559b89d35)

  - Here are the endpoints to test the `API` through `Postman`:

    Test with an image file: Send a `POST` request to `http://{xx.xx.xx.xx}:8081/alpr`.
    
    Test with a `base64-encoded` image: Send a `POST` request to `http://{xx.xx.xx.xx}:8081/alpr_base64`.

### 3. Execute the Gradio demo
  - Setup `Gradio`
    Ensure that the necessary dependencies are installed. </br>
    `Gradio` requires `Python 3.7` or above. </br>
    Install `Gradio` using `pip` by running the following command:
    ```bash
    pip install -r requirements.txt
    ```
  - Run the demo with the following command:
    ```bash
    cd gradio
    python demo.py
    ```
  - `SDK` can be tested on the following URL: `http://127.0.0.1:9000`

## About SDK

### 1. Initializing the SDK

- Import SDK python script
  ```python
  from alprsdk import initSDK, getLicensePlate, getMachineCode, freeLicenseResults, setActivation
  ```
- Obtain the `machine code` to activate and request a license
  ```python
  machineCode = getMachineCode()
  print("\nmachineCode: ", machineCode.decode('utf-8'))
  ```
- Activate the `SDK` using the license key
  ```python
  ret = setActivation(license.encode('utf-8'))
  print("\nactivation: ", ret)
  ```
- Initializing `SDK`
  ```python
  ret = initSDK()
  ```
  Once `ret` value is zero, SDK can get work started

### 2. APIs
  - Getting License Number & Coordinate
  
    The `SDK` provides a single API for getting license plate number and its coordinate(x, y, width, height).</br>
    The function can be used as follows:
    ```python
    recog_array = (c_int * 1024)()  # Assuming a maximum of 256 rectangles
    license_plate_ptr = POINTER(c_char_p)()
    cnt = getLicensePlate(img_byte, len(img_byte), byref(license_plate_ptr), recog_array)
    ```
    * `recog_array`: coordinate(`x`, `y`, `width`, `height`).
    * `img_byte`: image data in binary format.
    * `license_plate_ptr`: pointer to variable with license plate number.
  - Analyzing the result from `SDK`
    Result values from `SDK` inference can be analyzed as follows.</br>
    ```python    
    license_plate = [license_plate_ptr[i].decode('utf-8') for i in range(cnt)]
    rectangles = [
    (recog_array[i * 4], recog_array[i * 4 + 1], recog_array[i * 4 + 2], recog_array[i * 4 + 3])
    for i in range(cnt)]

    freeLicenseResults(license_plate_ptr, cnt)
    
    print("number: ", cnt, rectangles, license_plate)
    ```
    * `cnt`: the number of detected license plate.
    * `rectangles`: list of `coordinate`.
    * `license plate`: list of `license number`.    
  - Free Memory
    ```python
    freeLicenseResults(license_plate_ptr, cnt)
    ```
## Performance Video

You can visit our YouTube video for `ANPR/ALPR` model's performance [here](https://www.youtube.com/watch?v=sLBYxgMdXlA) to see how well our demo app works.</br></br>
[![ANPR/ALPR Demo](https://img.youtube.com/vi/sLBYxgMdXlA/0.jpg)](https://www.youtube.com/watch?v=sLBYxgMdXlA)</br>

## Application of ALPR
`Automatic license-plate recognition (ALPR)` is a technology that uses `OCR(optical character recognition)` on images to read vehicle registration plates. It can use existing closed-circuit television, road-rule enforcement cameras, or cameras specifically designed for the task. ALPR can be used by police forces around the world for law enforcement purposes, including to check if a vehicle is registered or licensed. It is also used for electronic toll collection on pay-per-use roads and as a method of cataloguing the movements of traffic, for example by highways agencies.</br>
`ALPR` has many uses including:
- Recovering stolen cars
- Identifying drivers with an open warrant for arrest
- Catching speeders by comparing the average time it takes to get from stationary camera A to stationary camera B
- Determining what cars do and do not belong in a parking garage
- Expediting parking by eliminating the need for human confirmation of parking passes

