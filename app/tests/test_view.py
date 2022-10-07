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

        def test_contact_us_success(self, setUp):
            response = self.client.get("/contact_us/")
            assert response.status_code == 200
            response = self.client.post("/contact_us/")
            assert response.status_code == 200
            assert response.charset == 'utf-8'
            assert 'text/html' in response.content_type
            assert response.data != ''

        def test_home_success(self, setUp):
            response = self.client.get('/')
            assert response.status_code == 200
            assert response.charset == 'utf-8'
            assert 'text/html' in response.content_type
            assert response.data != ''

        def test_home_fails(self, setUp):
            response = self.client.post('/')
            assert response.status_code == 405

        def test_not_found(self, setUp):
            response = self.client.post('/notExist')
            assert response.status_code == 404
