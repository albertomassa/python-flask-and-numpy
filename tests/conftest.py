import pytest

from app.app import create_app

@pytest.fixture()
def testapp(request):
    app = create_app()
    client = app.test_client()
    return client
