
from app.api.deps import get_db
from app.core.security import create_access_token
from app.crud.user import get_user_by_email
from app.schemas.auth import Token
from app.services.auth import authenticate_user, create_user
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_db),
) -> Token:
    user = authenticate_user(session, form_data.username, form_data.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token({"sub": str(user.id), "role": user.role})
    return Token(access_token=access_token)

@router.post("/register", response_model=Token)
def register(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_db),
) -> Token:
    existing_user = get_user_by_email(session, form_data.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    user = create_user(session, form_data.username, form_data.password)
    access_token = create_access_token({"sub": str(user.id), "role": user.role})
    return Token(access_token=access_token)