import re
import pyotp
from itsdangerous import URLSafeTimedSerializer
from flask import current_app as app
from gateway import mail
from flask_mail import Message


class Util:

    def validate(self, password):
        if len(password) < 9 and len(password) > 14:
            return"Make sure your password is at lest 8 letters"
        elif re.search('[0-9]', password) is None:
            return "Make sure your password contains a number in it"
        elif re.search('[A-Z]', password) is None:
            return"Make sure your password contains a capital letter"
        else:
            return "Ok"

    def otp(self):
        totp = pyotp.TOTP('base32secret3232')
        code = totp.now()
        print(code)

        def verify(self):
            print(totp.verify(code))

    def generate_confirmation_token(self, email):
        serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        return serializer.dumps(email,
                                salt=app.config['SECURITY_PASSWORD_SALT'])

    def confirm_token(self, token, expiration=3600):
        serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        try:
            email = serializer.loads(
                token,
                salt=app.config['SECURITY_PASSWORD_SALT'],
                max_age=expiration
            )
        except Exception as e:
            print(e)
            return False
        return email

    def send_email(self, to, subject, template):
        msg = Message(
            subject,
            recipients=[to],
            html=template,
            sender=app.config['MAIL_DEFAULT_SENDER']
        )
        mail.send(msg)
