from models.user import User
from models.base import Session
session = Session()



class UserService:

    user = session.query(User)

    @classmethod
    def create_user(cls, user):
        instance = cls.get_user(user)
        created = False
        if instance is None:
            data = {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username
            }
            instance = User(**data)
            session.add(instance)
            session.commit()
            created = True
        return instance, created

    @classmethod
    def get_user(cls, user):
        return cls.user.filter(User.id == user.id).first()
