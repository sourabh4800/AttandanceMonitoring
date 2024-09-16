# AttandanceMonitoringSystem
This project is a Gym Management System that uses face recognition to track attendance. It integrates with Firebase for storing student data and images.

## Prerequisites

- Python 3.x
- OpenCV
- face_recognition
- Firebase Admin SDK
- cvzone
- numpy

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/sourabh4800/AttandanceMonitoring.git
    cd gym-management-system
    ```

2. Install the required libraries:
    ```sh
    pip install opencv-python face_recognition firebase-admin cvzone numpy
    ```

3. Set up Firebase:
    - Download your `serviceAccountKey.json` from Firebase Console.
    - Place it in the root directory of the project.

4. Update the paths in the scripts to match your local setup.

## Usage

### EncodeGenerator.py

This script encodes the student images and saves the encodings to a file.

```sh
python EncodeGenerator.py
```

AddDataToDatabase.py
This script adds initial student data to the Firebase database.

```sh
python AddDataToDatabase.py
```

Main.py
This script captures video from the webcam, recognizes faces, and updates attendance in Firebase.

```sh
python Main.py
```
File Descriptions
EncodeGenerator.py: Encodes student images and uploads them to Firebase Storage.

Main.py: Captures video, recognizes faces, and updates attendance.

AddDataToDatabase.py: Adds initial student data to Firebase Realtime Database.
