import pytest
from setup import app
from fastapi.testclient import TestClient

client = TestClient(app)

class TestFixtures:
    
    @pytest.fixture
    def endpoints_response(self):
        response = client.get('/projects')
        return response
    
    @pytest.fixture
    def profile_response(self):
        response = client.get('/profile')
        return response
    
    
    @pytest.fixture
    def education_response(self):
        response = client.get('/education')
        return response
    
    @pytest.fixture
    def experience_response(self):
        response = client.get('/experience')
        return response
    
    @pytest.fixture
    def projects_response(self):
        response = client.get('/projects')
        return response
    
    @pytest.fixture
    def skills_response(self):
        response = client.get('/skills')
        return response
    
    


class Testfuncs:
    @pytest.fixture
    def fixtures(self):
        return TestFixtures()
        
    
    def test_get_endpoints(self):
        response = client.get('/endpoints')
        assert response.status_code == 200
        assert response.json['message'] == 'Success'
    
    def test_get_profile(self):
        response = client.get('/profile')
        assert response.status_code == 200
        assert response.json['message'] == 'Success'
        
    
    
    def test_get_education(self):
        response = client.get('/education')
        assert response.status_code == 200
        assert response.json['message'] == 'Success'
    
    
    def test_get_experience(self):
        response = client.get('/experience')
        assert response.status_code == 200
        assert response.json['message'] == 'Success'
    
    
    def test_get_projects(self):
        response = client.get('/projects')
        assert response.status_code == 200
        assert response.json['message'] == 'Success'
    
    
    def test_get_skills(self):
        response = client.get('/skills')
        assert response.status_code == 200
        assert response.json['message'] == 'Success'
    
    