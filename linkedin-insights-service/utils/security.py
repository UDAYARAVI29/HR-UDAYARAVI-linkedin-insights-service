import jwt
import os
from datetime import datetime, timedelta

SECRET_KEY = os.getenv("JWT_SECRET", "your_secret_key")

class Security:
    @staticmethod
    def generate_token(user_id: str, expiry_minutes: int = 60):
        """Generate JWT token for a user"""
        payload = {
            "user_id": user_id,
            "exp": datetime.utcnow() + timedelta(minutes=expiry_minutes)
        }
        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    @staticmethod
    def verify_token(token: str):
        """Verify and decode JWT token"""
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            return {"error": "Token expired"}
        except jwt.InvalidTokenError:
            return {"error": "Invalid token"}

# Example usage:
# token = Security.generate_token("user123")
# print(Security.verify_token(token))
