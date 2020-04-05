# project/tests/test_base.py


import json
from project.tests.base import BaseTestCase
from project.tests.utils import TestUtils


class TestBaseBlueprint(BaseTestCase):
    def test_ping(self):
        """Ensure the /ping route behaves correctly."""
        # first login user with request to users service
        auth_token = TestUtils.user_login(TestUtils.user_data_retail)
        response = self.client.get(
            "/base/ping", headers=dict(Authorization=f"Bearer {auth_token}")
        )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn("pong!", data["message"])
        self.assertIn("success", data["status"])

    def test_ping_no_header(self):
        """Ensure error is thrown if 'Authorization' header is empty."""
        response = self.client.get("/base/ping")
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 403)
        self.assertIn("Provide a valid auth token.", data["message"])
        self.assertIn("error", data["status"])

    def test_ping_invalid_token(self):
        """Ensure error is thrown if 'Authorization' header is empty."""
        response = self.client.get(
            "/base/ping", headers=dict(Authorization=f"Bearer asfafa")
        )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 401)
        self.assertIn("Invalid token.", data["message"])
        self.assertIn("error", data["status"])
