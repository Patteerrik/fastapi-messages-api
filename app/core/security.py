from fastapi import Header, HTTPException, status
from app.core.config import settings


def require_api_key(x_api_key: str | None = Header(default=None)) -> str:
    expected = settings.api_key

    if not expected:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Server API key is not configured",
        )

    if x_api_key != expected:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )

    return x_api_key
