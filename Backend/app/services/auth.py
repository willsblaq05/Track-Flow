from sqlmodel import Session, select

from app.core.security import verify_password
from app.crud.user import get_user_by_email
from app.core.security import get_password_hash
from app.models.user import User

def get_user_by_id(session: Session, user_id: int) -> User | None:
    statement = select(User).where(User.id == user_id)
    return session.exec(statement).first()

def authenticate_user(session: Session, email: str, password: str) -> User | None:
    user = get_user_by_email(session, email)
    if user is None or not user.is_active:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def create_user(session: Session, email: str, password: str) -> User:
    hashed_password = get_password_hash(password)
    user = User(email=email, hashed_password=hashed_password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

