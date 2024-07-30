from functools import wraps
from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
import os
import uuid

# Load environment variables from cred.env file
load_dotenv('cred.env')

# Create the Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY') or os.urandom(24)

# Configure OAuth
oauth = OAuth(app)

# Register Google OAuth
google = oauth.register(
    name='google',
    client_id=os.environ.get('GOOGLE_CLIENT_ID'),
    client_secret=os.environ.get('GOOGLE_CLIENT_SECRET'),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid profile email'},
)

# Login decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Login route
@app.route('/login')
def login():
    google_client = oauth.create_client('google')
    nonce = str(uuid.uuid4())
    session['nonce'] = nonce
    redirect_uri = url_for('auth', _external=True)
    return google_client.authorize_redirect(redirect_uri, nonce=nonce)

# Authentication route
@app.route('/auth')
def auth():
    google_client = oauth.create_client('google')
    token = google_client.authorize_access_token()
    nonce = session.pop('nonce', None)
    user_info = google_client.parse_id_token(token, nonce=nonce)

    # Save user info in session
    session['user'] = {
        'id': user_info['sub'],
        'name': user_info['name'],
        'email': user_info['email'],
        'picture': user_info['picture'],
    }
    
    return redirect('/dashboard')

# Dashboard route
@app.route('/dashboard')
@login_required
def dashboard():
    user = session.get('user')
    return f"Hello, {user['name']}!"

# Logout route
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
