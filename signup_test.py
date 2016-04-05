import main
import unittest


class UserSignupTestCase(unittest.TestCase):
    def setUp(self):
        main.app.config['TESTING'] = True
        self.app = main.app.test_client()

    def signUp(self, inputName, inputEmail):
        return self.app.post('/signUp', data=dict(
            inputName = inputName,
            inputEmail = inputEmail
        ),follow_redirects=True)

    def test_signUp_ok(self):
        rv = self.signUp("ray", "ray@gmail.com")
        assert b'Success' in rv.data

    def test_signUp_not_ok(self):
        rv = self.signUp("admin", "admin@admin.com")
        assert b'Fail' in rv.data

if __name__ == '__main__':
    unittest.main()