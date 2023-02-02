from django.test import TestCase
from authapp import User
import json

# Create your tests here.
test_user = {"username": "testuser", "password": "testpassword"}

class TokenTest(TestCase):
    def setUp(self):
        new_user = User.objects.create(username=test_user["username"], birth='2000-01-01')
        new_user.set_password(test_user["password"])
        new_user.save()

    def test_token(self):
        res = self.client.post('/api/token/', data=json.dumps({
            'username': test_user["username"],
            'password': test_user["password"],
        }), content_type='application/json')
        result = json.loads(res.content)
        print(result.get("access"), result.get("refresh"))
        access_token = result.get("access")
        refresh_token = result.get("refresh")
        self.assertTrue("access" in result)
        self.assertTrue("refresh" in result)

        res = self.client.post('/api/token/verify/', data=json.dumps({
            'token': access_token}), content_type='application/json')
        result = json.loads(res.content)
        print(result)
        self.assertEqual(res.status_code, 200)
