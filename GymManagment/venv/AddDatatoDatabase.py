
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("C:/Users/ACER/PycharmProjects/GymManagment/venv/serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' :"https://gymmanagment-b6b92-default-rtdb.firebaseio.com/"
})

ref =db.reference('Students')

data={
    "AJAY":{
        "name":"AJAY MAVAI",
        "blood-type":"B+",
        "contact":9977143620,
        "total_attendance":16,
        "cardio":"N",
        "duration": 360,
        "last_attendance_time":"2022-12-11 00:54:34"
    },
    "ASHUTOSH":{
        "name":"ASHUTOSH TRIPATHI",
        "blood-type":"A+",
        "contact":9977143620,
        "total_attendance":6,
        "cardio":"Y",
        "duration": 30,
        "last_attendance_time":"2022-12-11 00:54:34"
    },
    "AYUSH":{
        "name":"AYUSH THAPA",
        "blood-type":"O+",
        "contact":9977143624,
        "total_attendance":12,
        "cardio":"N",
        "duration": 360,
        "last_attendance_time":"2022-12-11 00:54:34"
    },
    "JATIN":{
        "name":"JATIN MITRANI",
        "blood-type":"O+",
        "contact":9977143627,
        "total_attendance":1,
        "cardio":"Y",
        "duration": 100,
        "last_attendance_time":"2022-12-11 00:54:34"
    },
    "NITIN":{
        "name":"NITIN MALVIYA",
        "blood-type":"AB+",
        "contact":9977143624,
        "total_attendance":12,
        "cardio":"Y",
        "duration": 90,
        "last_attendance_time":"2022-12-11 00:54:34"
    }
,
    "SOURABH":{
        "name":"SOURABH SINGH",
        "blood-type":"B+",
        "contact":9977143677,
        "total_attendance":1,
        "cardio":"Y",
        "duration": 70,
        "last_attendance_time":"2022-12-11 00:54:34"
    }
}

for key,value in data.items():
    ref.child(key).set(value)