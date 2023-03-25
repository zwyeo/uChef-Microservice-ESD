# firebase cloud messaging setup file
# DONT EDIT UNLESS NECESSARY

import fcm_cloud_messaging as fcm

# token will need to be taken from Android application
# the application we built on Android Studio will automatically generate and log the token into console everytime we run the app
# take the token from the android app and throw it inside the list below
tokens = ["fDvSQgEsTq6Y5unPRekfKq:APA91bHJxv7sJRoHsLUinvMdimuz7eoSMnFUFba7rPFD5fjsMA8W__XoSsjzu4-l9sVzbpjjhZtfoetG2mIoZd8LK4rLt9ie_QXIYqsYR0AJsAGovMEzzQyRoiT6RDgMwiM0b1bYTITg"]

def sendPush(title, msg, registration_token=tokens, dataObject=None):
    fcm.sendPush(title, msg, registration_token)