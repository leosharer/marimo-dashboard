from fastapi import HTTPException, Request, status
from pydantic import BaseModel

# Simulated user database (replace with a real database in production)
users = {'admin': 'password123'}


class LoginForm(BaseModel):
    username: str
    password: str


def get_current_user(request: Request):
    username = request.session.get('username')
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Not authenticated'
        )
    return username
