import sendgrid
from sendgrid.helpers.mail import Email, To, Content, Mail
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    sg = sendgrid.SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
    from_email = Email("uemersonpinheirojunior@gmail.com")
    to_email = To("uemersonpinheirojunior@gmail.com")
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


if __name__ == "__main__":
    main()
