from copy import deepcopy
from unittest import TestCase

from members.models import Member


class TestClass(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_member_is_valid_request(self):
        test_obj = {
                    "first_name": "Test First Name",
                    "last_name": "Test Last name",
                    "phone_number": "1034517890",
                    "email": "test.test@test.com",
                    "role": "admin",
                }

        self.assertTrue(Member.is_valid_request(test_obj)[0])

        for key in test_obj.keys():
            new_test_obj = deepcopy(test_obj)
            new_test_obj[key] = ""
            if key == "role":
                self.assertTrue(Member.is_valid_request(new_test_obj)[0])
            else:
                self.assertFalse(Member.is_valid_request(new_test_obj)[0])
        
