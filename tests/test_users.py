from unittest import TestCase
from models.user import User
from api.app import app
from models import storage
import unittest
from models.user import User
password = 'jweydweyiyebue'
name = 'testWriter'
url_prefix = '/api/meal_magic/users'
email='randomgibberish@gmail.go'

class TestUser(TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.res  = self.app.post('{}'.format(url_prefix),
                                  json=dict(name=name, password=password, email=email))
        user = storage.get(User, email=email)
        user.confirmed = True # verifying the user email so as to enable login
        user.save()
        self.login_res = self.app.post('/auth/login', json={'email':email, 'password': password});

    def test_post_user(self):
        self.assertEqual(201, self.res.status_code)

    def test_login_user(self):
        self.assertEqual(200, self.login_res.status_code)

    def test_get_user(self):
        res = self.app.post('/auth/login', json={'email':email, 'password': password})
        token = self.login_res.json['access_token']
        headers = { 'Authorization': 'Bearer ' + token}
        res = self.app.get('{}'.format(url_prefix), headers=headers)
        self.assertEqual(200, res.status_code)

    def test_update_user(self):
        res = self.app.post('/auth/login', json={'email':email, 'password': password})
        token = self.login_res.json['access_token']
        headers = { 'Authorization': 'Bearer ' + token}
        res = self.app.put('{}'.format(url_prefix), headers=headers, json={'name': 'john'})
        self.assertEqual(201, res.status_code)
    
    def test_delete_user(self):
        res = self.app.post('/auth/login', json={'email':email, 'password': password})
        token = self.login_res.json['access_token']
        headers = { 'Authorization': 'Bearer ' + token}
        res = self.app.delete('{}'.format(url_prefix), headers=headers)
        self.assertEqual(200, res.status_code)

    def test_logout(self):
        res = self.app.post('/auth/login', json={'email':email, 'password': password})
        token = self.login_res.json['access_token']
        headers = { 'Authorization': 'Bearer ' + token}
        res = self.app.post('/auth/logout'.format(url_prefix), headers=headers)
        self.assertEqual(200, res.status_code)


    def tearDown(self):
        user = storage.get(User, email=email)
        if user:
            storage.delete(user)
            storage.save()
            storage.close()


class TestError(TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.res  = self.app.post('{}'.format(url_prefix),
                                  json=dict(name=name, password=password, email=email))
        user = storage.get(User, email=email)
        user.confirmed = True # verifying the user email so as to enable login
        user.save()
        self.login_res = self.app.post('/auth/login', json={'email':email, 'password': password});


    def test_postUser_ErrorHandler(self):
        res  = self.app.post('{}'.format(url_prefix))
        self.assertEqual(400, res.status_code)
        res  = self.app.post('{}'.format(url_prefix), json=dict(name=name, password=password))
        self.assertEqual(400, res.status_code)
        res  = self.app.post('{}'.format(url_prefix), json={'name': name, 'password': password, 'email': email}) #email already in use
        self.assertEqual(400, res.status_code)
        res  = self.app.post('{}'.format(url_prefix), json={'name': name, 'email': 'testingmail@email.com'}) #missing password
        self.assertEqual(400, res.status_code)
        res  = self.app.post('{}'.format(url_prefix), json={'password': password, 'email': 'testingmail@email.com'})
        self.assertEqual(400, res.status_code)


    def test_updateAndDeleteUser_ErrorHandler(self):
        res = self.app.post('/auth/login', json={'email':email, 'password': password})
        token = self.login_res.json['access_token']
        headers = { 'Authorization': 'Bearer ' + token}

        res = self.app.put('{}'.format(url_prefix))
        self.assertEqual(401, res.status_code)
        res = self.app.put('{}'.format(url_prefix), headers=headers)
        self.assertEqual(400, res.status_code)
        self.tearDown() # deleting user so 404 err is thrown
        res = self.app.put('{}'.format(url_prefix), headers=headers)
        self.assertEqual(404, res.status_code)



    def tearDown(self):
        user = storage.get(User, email=email)
        if user:
            storage.delete(user)
            storage.save()
            storage.close()

if __name__ == '__main__':
    unittest.main()
