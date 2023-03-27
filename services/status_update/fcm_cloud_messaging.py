# firebase cloud messaging setup file
# DONT EDIT UNLESS NECESSARY

import firebase_admin
from firebase_admin import credentials, messaging, db

# replace this path with the actual path for serviceAccountKey.json
# right click serviceAccountKey.json in VSCode and click on copy path, then paste it into the path below
# e.g. cred = credentials.Certificate("/Users/douglastoh99/Documents/GitHub/uChef-Microservice-ESD/services/notification/serviceAccountKey.json")
cred = credentials.Certificate("/Users/douglastoh99/Documents/GitHub/uChef-Microservice-ESD/services/status_update/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://uchef-9f3e5.firebaseio.com/'})

# token will need to be taken from Android application
# the application we built on Android Studio will automatically generate and log the token into console everytime we run the app
# take the token from the android app and throw it inside the list below
tokens = ["d19Pzaw1TSOuPTdCDji4R-:APA91bH3kUXeOTwJE_zK5nY8T4uTFELHhUzzXoDs1Miob6Ty5d71bgglvA8dkfjq3cXNlp9mwxWCRjMEJznNh8fejXqyR-kWcZaxutsuNlKBsPrChUh4RL8T2e61rGWh0ApHSM9AmF9g"]

def sendPush(title, msg, registration_token=tokens, dataObject=None):
    # See documentation on defining a message payload.
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=msg
        ),
        data=dataObject,
        tokens=registration_token
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send_multicast(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)