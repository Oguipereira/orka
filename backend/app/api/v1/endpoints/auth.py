from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.base import get_db
from app.core.security import hash_password, verify_password, create_access_token
from app.models.user import User, Organization, UserOrganization
from pydantic import BaseModel, EmailStr
from sqlalchemy import select
import uuid

router = APIRouter()

class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str
    org_name: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

@router.post("/register", status_code=201)
async def register(data: RegisterRequest, db: AsyncSession = Depends(get_db)):
    existing = await db.execute(select(User).where(User.email == data.email))
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    org = Organization(name=data.org_name)
    db.add(org)
    user = User(name=data.name, email=data.email, password_hash=hash_password(data.password))
    db.add(user)
    await db.flush()
    db.add(UserOrganization(user_id=user.id, organization_id=org.id, role="admin"))
    await db.commit()
    token = create_access_token(str(user.id))
    return {"access_token": token, "token_type": "bearer"}

@router.post("/login")
async def login(data: LoginRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == data.email))
    user = result.scalar_one_or_none()
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = create_access_token(str(user.id))
    return {"access_token": token, "token_type": "bearer"}
