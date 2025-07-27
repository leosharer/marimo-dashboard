import marimo
from fastapi import FastAPI
from loguru import logger

from app.api.exceptions import include_exception_handlers
from app.api.middleware import include_middleware
from app.api.router import router
from app.utilities.files import notebooks

# Create a FastAPI app
app = FastAPI()
app.include_router(router)

# Create marimo server & add routes
server = marimo.create_asgi_app()
for nbk in notebooks:
    logger.info(f'Mounting notebook: {nbk.name} at path: {nbk.path}')
    server.with_app(path=f'/{nbk.name}', root=nbk.path)

# Mount the marimo server at the root path
app.mount('/', server.build())

# Include middleware and exception handlers
include_middleware(app)
include_exception_handlers(app)


if __name__ == '__main__':
    import uvicorn

    logger.info('Starting application...')
    uvicorn.run(app, host='0.0.0.0', port=8080)
