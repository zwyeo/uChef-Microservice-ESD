from flask import Flask, request, jsonify
import boto3
from botocore.exceptions import ClientError
import json

app = Flask(__name__)

@app.route('/notification', methods=['POST'])
def send_email():
    # Get input data from JSON object
    if request.method == 'POST':
        data = request.get_json()
    print(data)
    price = data['price']
    email = data['email']
    street_address = data['street_address']
    postal_code = data['postal_code']
    delivery_address = street_address + " " + postal_code

    # Create a new SES client
    ses = boto3.client('ses',  aws_access_key_id='AKIAVFEET5SMSLP36BYB',
                   aws_secret_access_key="f6wOJ84/W+8qyUxAasZfnIVcJusVyYr2Led9RJaz", region_name='ap-southeast-1')

    # Create the message body
    message_body = f"Hello,\n\nHere are your payment details:\n\nPrice: {price}\n\nDelivery Address: {delivery_address}"

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
        return jsonify({"code": 200, "data": 'OK. Email sent successfully.'}), 200
    except ClientError as e:
        print(e.response['Error']['Message'])
        return jsonify({"code": 400, "message": "Email failed to send. Please try again"}), 400
    

if __name__ == '__main__':
    app.run(port=5006, debug=True)
