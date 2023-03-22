# firebase cloud messaging setup file
# DONT EDIT UNLESS NECESSARY

import fcm_cloud_messaging as fcm

# token will need to be taken from Android application
# the application we built on Android Studio will automatically generate and log the token into console everytime we run the app
# take the token from the android app and throw it inside the list below
tokens = ["elR5_cWOQLmFfkfK4ybhPo:APA91bH4ovNfOj-PsHF7HX8OIcz7_V14FQv6ISJ16a90lgMDepi9P5SV4E8H2OSIB5kCOnqsWDjG925L0u5N58V2lafeYO2qimG2BgBW8NRLvchryrvnUKqVdQ5JB83vWoEDI60g3lbT"]

def sendPush(title, msg, registration_token=tokens, dataObject=None):
    fcm.sendPush(title, msg, registration_token)