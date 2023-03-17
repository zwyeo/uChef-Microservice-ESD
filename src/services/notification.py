from flask import Flask, request
from mailersend import emails

app = Flask(__name__)

# configure MailerSend API key
mailer = emails.NewEmail("eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMGE5NWRlZDgyZjgxMzE1NDg0Yzg2YzNkY2Q0NjlhMjVkZTMzZjIzNzMzMzhjM2ZiY2EwM2Q5M2Y5ZjFiMTEwMTk1ODRmN2ZjMDMyYTYxY2EiLCJpYXQiOjE2NzkwMzk2MTQuMTEyNDI0LCJuYmYiOjE2NzkwMzk2MTQuMTEyNDI2LCJleHAiOjQ4MzQ3MTMyMTQuMTA1OTIzLCJzdWIiOiI2MzMwNyIsInNjb3BlcyI6WyJlbWFpbF9mdWxsIiwiZG9tYWluc19mdWxsIiwiYWN0aXZpdHlfZnVsbCIsImFuYWx5dGljc19mdWxsIiwidG9rZW5zX2Z1bGwiLCJ3ZWJob29rc19mdWxsIiwidGVtcGxhdGVzX2Z1bGwiLCJzdXBwcmVzc2lvbnNfZnVsbCIsInNtc19mdWxsIiwiZW1haWxfdmVyaWZpY2F0aW9uX2Z1bGwiLCJpbmJvdW5kc19mdWxsIiwicmVjaXBpZW50c19mdWxsIiwic2VuZGVyX2lkZW50aXR5X2Z1bGwiXX0.JFnAVWWDwyotoSjAYjT0SLogqPHYxYuwlVAyrHy_CcfqZ2LEO2m39MYGh-JxzUMzzpo65KzjG07QnCIUR_9HWTss1CoBHT2AFf3wH00MJGwa2eepTp5IuguWr09AysjFPGGylrsoQBvgTnw8AcRqCAJxRpMFiIvv3GTP-6Co0r08ragmiwXwfG_dT7Y9M6yHQFTDPBnfkE8PZZmhIbbPCpDu9FiYffqk-FBP5j2eXo1dPc82reZ1Bl659qeWABie5b3rMvPInr8XyhqrNEb1eA3AgkN-XgkLSsyJfD1q1_4Mz262kP1XvmnohM7-pWLPllhs_V2bl64la90ZpJnwlFTYDmxe0DnDsj93u894m58qH-4dxV7gX7yPfL_HGHicvo2R92TdOc8G-Of6wOpZy8cCl8zNJJqqj0ER20s6k8z7DYBsPcucoETOYVdov3ZsuRLF217KgJ2wTxclz5sMng_z396-rZ9wOZAR5AU5HWYN9iJ_z9NJyyKhNnO3mwj2FqVkVTWqvwPqtiZWNynNGCOdpmqSYexaTvZpE_eigFJQxmFWHCYw9CWy9866Cpv2f1HrY_3Ng7PT2_iV1IyzyiiNEZf2o2lUoBysNQtFEVk4oaylgdPmioP4dWoDaUsIjWVPBlnSePi0KSF8EYiOYQfRTKfkOP2b5BZ20OVyDmE")

@app.route('/send-email', methods=['POST'])
def send_email():
    # retrieve JSON data from request
    data = {
	"payment_details": [{
		"payment_id": "1",
		"price": 25
	}],
	"email": "jadengohipod@gmail.com",
	"delivery_address": "Rock Road",
	"recipient_name": "Jaden"
}
    
    # extract information from JSON data
    payment_id = data['payment_details'][0]['payment_id']
    price = data['payment_details'][0]['price']
    email = data['email']
    delivery_address = data['delivery_address']
    recipient_name = data['recipient_name']
    
    # set up email content
    mail_body = {}
    mail_from = {
        "name": "uChef",
        "email": "uchef216@gmail.com",
    }
    recipients = [
        {
            "name": recipient_name,
            "email": email,
        }
    ]
    reply_to = [
        {
            "name": "uChef",
            "email": "uchef216@gmail.com",
        }
    ]
    subject = f"Payment {payment_id} Confirmation"
    html_content = f"""
        <p>Dear {recipient_name},</p>
        <p>Thank you for your payment of ${price}.</p>
        <p>Your order will be delivered to {delivery_address}.</p>
        <p>Regards,</p>
        <p>Your Name</p>
    """
    plaintext_content = f"Dear {recipient_name},\n\nThank you for your payment of ${price}.\n\nYour order will be delivered to {delivery_address}.\n\nRegards,\nYour Name"
    
    # set email content using MailerSend API
    mailer.set_mail_from(mail_from, mail_body)
    mailer.set_mail_to(recipients, mail_body)
    mailer.set_subject(subject, mail_body)
    mailer.set_reply_to(reply_to, mail_body)
    mailer.set_html_content(html_content, mail_body)
    mailer.set_plaintext_content(plaintext_content, mail_body)

    # send email
    response = mailer.send(mail_body)

    # return response to client
    return response

if __name__ == '__main__':
    app.run(port=5099, debug=True)
