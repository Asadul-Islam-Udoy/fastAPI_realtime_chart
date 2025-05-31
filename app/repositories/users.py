from sqlalchemy.orm import Session,joinedload
from models.user import User
from models.profile import Profile
from schemas.user import UserCreate
from core.security import get_password_hash
class UserRepository:
    def create(self,db:Session,user:UserCreate):
        db_user = User(
            username = user.username,
            email = user.email,
            role = user.role,
            password = get_password_hash(user.password)
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        db_profile = Profile(
          email=db_user.email,
          user_id = db_user.id
        )
        db.add(db_profile)
        db.commit()
        db.refresh(db_profile)
        db_user.profile = db_profile
        return db_user
    
    
    def get_single_user(self,db:Session,email:str):
        return db.query(User).filter(User.email == email).first()
    
    
    def get_all_user(self,db:Session):
        return db.query(User).options(joinedload(User.profile)).all()
        