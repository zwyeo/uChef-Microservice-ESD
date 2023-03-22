import firebase_admin
from firebase_admin import credentials, messaging

# replace this path with the actual path for serviceAccountKey.json
# right click serviceAccountKey.json in VSCode and click on copy path, then paste it into the path below
# e.g. cred = credentials.Certificate("/Users/douglastoh99/Documents/GitHub/uChef-Microservice-ESD/services/notification/serviceAccountKey.json")
cred = credentials.Certificate("/Users/douglastoh99/Documents/GitHub/uChef-Microservice-ESD/services/status_update/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def sendPush(title, msg, registration_token, dataObject=None):
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