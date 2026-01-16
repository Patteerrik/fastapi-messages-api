import os
from fastapi import Header, HTTPException, status


def require_api_key(x_api_key: str | None = Header(default=None)) -> str:
    expected = os.getenv("API_KEY")

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
