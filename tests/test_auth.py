import pytest
import json 

@pytest.mark.usefixtures("testapp")
class TestLogin:
    
    def test_login(self, testapp):
        """ Test auth endpointn """

        data = dict(
            username='user',
            password='password'
        )

        rv = testapp.post('/auth/login', data=json.dumps(data),
                       content_type='application/json')

        assert rv.status_code == 200
