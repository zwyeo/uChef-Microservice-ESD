from flask import Flask, request
import boto3
from botocore.exceptions import ClientError
import json

app = Flask(__name__)

@app.route('/send_email', methods=['POST'])
def send_email():
    # Get input data from JSON object
    data = {
        "payment_details": [{
            "payment_id": "14",
            "price": 454.95
        }],
        "email": "joseph.ho.2021@scis.smu.edu.sg",
        "delivery_address": "55 Rocky Road"
    }
    payment_details = data['payment_details']
    email = data['email']
    delivery_address = data['delivery_address']

    # Create a new SES client
    ses = boto3.client('ses',  aws_access_key_id='AKIAVFEET5SMSLP36BYB',
                   aws_secret_access_key="f6wOJ84/W+8qyUxAasZfnIVcJusVyYr2Led9RJaz", region_name='ap-southeast-1')

    # Create the message body
    message_body = f"Hello,\n\nHere are your payment details:\n\nPayment ID: {payment_details[0]['payment_id']}\nPrice: {payment_details[0]['price']}\n\nDelivery Address: {delivery_address}"

    # Try to send the email
    try:
        response = ses.send_email(
            Source='uchef216@gmail.com',
            Destination={
                'ToAddresses': [
                    email,
                ],
            },
            Message={
                'Subject': {
                    'Data': 'Payment Details',
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Text': {
                        'Data': message_body,
                        'Charset': 'UTF-8'
                    },
                }
            }
        )
        return "Email sent successfully"
    except ClientError as e:
        print(e.response['Error']['Message'])
        return "Error sending email"

if __name__ == '__main__':
    app.run(port=5088, debug=True)
