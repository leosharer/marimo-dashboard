from typing import Callable, Coroutine

from fastapi import FastAPI, Request, Response, status
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware


def include_middleware(app: FastAPI) -> None:
    """
    Add middleware to the FastAPI app.
    This middleware checks if the user is authenticated before allowing access to protected routes.
    """

    # Middleware to check if user is authenticated
    @app.middleware('http')
    async def auth_middleware(
        request: Request,
        call_next: Callable[[Request], Coroutine[None, None, Response]],
    ) -> Response:
        if request.url.path == '/login':
            return await call_next(request)

        if 'username' not in request.session:
            return RedirectResponse(url='/login', status_code=status.HTTP_302_FOUND)

        return await call_next(request)

    # Add session middleware for managing user sessions
    app.add_middleware(SessionMiddleware, secret_key='your-secret-key')
