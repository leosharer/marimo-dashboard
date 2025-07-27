from fastapi import (
    APIRouter,
    Depends,
    Form,
    Request,
    status,
)
from fastapi.responses import RedirectResponse
from loguru import logger

from app.utilities.files import notebooks, templates
from app.utilities.users import get_current_user, users

router = APIRouter()


@router.get('/login')
async def get_login(request: Request):
    return templates.TemplateResponse('login.html', {'request': request})


@router.post('/login')
async def post_login(
    request: Request, username: str = Form(...), password: str = Form(...)
):
    if username in users and password == users[username]:
        request.session['username'] = username
        logger.info(f'User {username} logged in successfully')
        return RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    logger.warning(f'Failed login attempt for user {username}')
    return templates.TemplateResponse(
        'login.html', {'request': request, 'error': 'Invalid credentials'}
    )


@router.get('/logout')
async def logout(request: Request):
    username = request.session.get('username')
    request.session.clear()
    logger.info(f'User {username} logged out')
    return RedirectResponse(url='/login')


@router.get('/')
async def home(request: Request, username: str = Depends(get_current_user)):
    return templates.TemplateResponse(
        'home.html', {'request': request, 'username': username, 'notebooks': notebooks}
    )


@router.get('/ping')
async def root():
    return {'message': 'pong'}
