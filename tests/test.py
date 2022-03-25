import unittest

from config import Config
from gateway import create_app, db
from gateway.models import User
from gateway.mpesa_credentials import LipanaMpesaPpassword
from gateway.odoo_methods.logic import Logic, UserAuthenticator
from gateway.saf_end_points.saf_methods import SafMethods
from gateway.utilities.util import Util
import requests


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SERVER_NAME = 'localhost'


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        u = User(username='susan')
        u.hash_password('cat')
        self.assertFalse(u.verify_password('dog'))
        self.assertTrue(u.verify_password('cat'))

    def test_member(self):
        logic = Logic()
        member = logic.search_member('ramy@gamil.com')
        print(member)
        self.assertTrue(not member)

    def test_url_registration(self):
        end_points = SafMethods()
        response = end_points.register_url()
        print(response)

    def test_push(self):
        args = [
            {
                "transaction_type": " deposits",
                "amount": 2
            },

        ]
        end_points = SafMethods()
        status = end_points.send_push(args, 254727292911)
        print(status)

    def test_add_member(self):
        user = UserAuthenticator()
        ceated_user = user.register_member({
            "name": "Ramdas",
            "password": "Sammy12",
            "email": "alphatesfa789@gmail.com",
            "phone_no": "0722890998"
        })
        print(ceated_user)
        # self.assertDictEqual(created_user)

    def testC2B(self):
        end_points = SafMethods()
        status = end_points.make_payment()
        print(status)

    def test_active_loan(self):
        with Logic() as logic:
            print(logic.get_loans('denokorir@gmail.com'))

    def test_member_ledger(self):
        with Logic() as logic:
            args = {
                "email": "denokorir@gmail.com",
            }
            print(logic.get_member_ledger(args))

    def test_loan_types(self):
        with Logic() as logic:
            print(logic.get_loan_products())

    def test_apply_loan(self):
        with Logic() as logic:
            member = logic.search_member("denokorir@gmail.com")
            # args = {
            #     "loan_product_type": 3,
            #     "loan_category": "mobile",
            #     "member_no": member['id'],
            #     "member_name": member['name'],
            #     "requested_amount": 2
            # }
            print(member)

    def test_get_appraisal(self):
        with Logic() as logic:
            print(logic.get_appraisal_report(39))

    def test_loan_appraisal(self):
        with Logic() as logic:
            print(logic.appraise_loan(42))

    def test_loan_shedual(self):
        with Logic() as logic:
            print(logic.get_loan_schedule(loan=24))

    def test_search_by_phone(self):
        with Logic() as logic:
            member = logic.search_by_phone(phone_number=254727292911)
            print(member)

    def test_pin(self):
        with Logic() as logic:
            print(logic.upload_existing_users('denokorir@gmail.com'))

    def test_loan_cal(self):
        data = {
            "loan_product_type": 2,
            "loan_category": "term",
            "requested_amount": 70000
        }
        with Logic() as logic:
            print(logic.calculate_loan(data))

    def test_password_validation(self):
        util = Util()
        util.otp()

    def test_search_memberby_number(self):
        logic = Logic()
        test_member = {
            "email": "pkimmungai@gmail.com",
            "id": 3,
            "name": "Peter Kimani"
        }
        member = logic.search_member_no('MEMBER0003')
        self.assertDictEqual(member, test_member)

    def test_password_reset(self):
        user = UserAuthenticator()
        logged_user = user.reset_password('alpaksk')
        print(logged_user)

    def test_guarantor_request(self):
        request_ids = [2, 3]
        logic = Logic()
        data = logic.get_guarantee_requests(request_ids)
        print(data)


if __name__ == '__main__':
    unittest.main(verbosity=2)
