import fcm_cloud_messaging as fcm

# token will need to be taken from Android application
# the application we built on Android Studio will automatically generate and log the token into console everytime we run the app
# take the token from the android app and throw it inside the list below
tokens = ["INSERT TOKEN HERE"]

def sendPush(title, msg, registration_token=tokens, dataObject=None):
    fcm.sendPush(title, msg, registration_token)