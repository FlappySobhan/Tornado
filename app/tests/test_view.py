import pytest
from decouple import config

from app import app


class TestFlask():

    if bool(config('IS_LOCAL', False)):

        @pytest.fixture
        def setUp(self):
            app.testing = True
            self.client = app.test_client()

        def test_menu_success(self, setUp):
            response = self.client.get('/menu/')
            assert response.status_code == 200
            assert response.charset == 'utf-8'
            assert 'text/html' in response.content_type
            assert response.data != ''

        def test_menu_fails(self, setUp):
            response = self.client.post('/menu/')
            assert response.status_code == 405
