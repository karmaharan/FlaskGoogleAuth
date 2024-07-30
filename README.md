# Flask Google OAuth Authentication

This Flask application integrates Google OAuth for user authentication. It allows users to log in with their Google accounts, access a protected dashboard, and manage sessions securely. The app uses `Authlib` and `dotenv` for OAuth and environment management.

## Features

- **Google OAuth Integration:** Authenticate users with Google.
- **Login/Logout:** Secure login and logout functionality.
- **Protected Dashboard:** Access restricted to authenticated users.
- **Environment Configuration:** Securely manage sensitive data with `.env` files.

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/karmaharan/FlaskGoogleAuth.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd your-repository
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file with the following content:**

   ```env
   SECRET_KEY=your_secret_key
   GOOGLE_CLIENT_ID=your_google_client_id
   GOOGLE_CLIENT_SECRET=your_google_client_secret
   ```

5. **Run the application:**

   ```bash
   python app.py
   ```

## Routes

- `/login`: Start Google OAuth login.
- `/auth`: Handle OAuth callback and user info retrieval.
- `/dashboard`: Display user-specific content.
- `/logout`: Clear session and log out.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

