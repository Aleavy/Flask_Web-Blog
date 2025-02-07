# Import sys module for modifying Python's runtime environment
import sys
# Import os module for interacting with the operating system
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the Flask app instance from the main app file
from app import create_app

app = create_app()
app.config["TESTING"] = True 
# Import pytest for writing and running tests
import pytest

@pytest.fixture
def client():
    """A test client for the app."""
    with app.test_client() as client:
        yield client

def test_home(client):
    """ Test the Home route. """
    response = client.get("/")
    assert response.status_code == 200

def test_signup(client):
    """ Test the SignUp route. """
    response = client.get("/auth/sign_up")
    assert response.status_code == 200

def test_login(client):
    """ Test the Login route. """
    response = client.get("/auth/login")
    assert response.status_code == 200

def test_not_owner_redirect(client):
    """ Test editing a post that arent from the user."""
    response = client.get("/dashboard/edit_post/1")

    
    assert response.status_code == 302  
