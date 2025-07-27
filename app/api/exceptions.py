from fastapi import FastAPI, HTTPException, Request
from loguru import logger

from app.utilities.files import templates


def include_exception_handlers(app: FastAPI) -> None:
    """
    Add exception handlers to the FastAPI app.
    This function registers a handler for HTTP exceptions to render a custom error page.
    """

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        logger.error(f'HTTP error occurred: {exc.detail}')
        return templates.TemplateResponse(
            'error.html',
            {'request': request, 'detail': exc.detail},
            status_code=exc.status_code,
        )
