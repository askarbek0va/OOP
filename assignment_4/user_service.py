
class UserService:

    users={}

    @classmethod
    def add_user(cls,user):
        user_id=user.user_id
        cls.users[user_id]=user

    @classmethod
    def find_user(cls,user_id):
        return cls.users.get(user_id,None)

    @classmethod
    def delete_user(cls,user_id):
        if user_id in cls.users:
            del cls.users[user_id]

    @classmethod
    def update_user(cls,user_id,user_update):
        user=cls.users.get(user_id)
        if user:
            for key, value in user_update.items():
                if hasattr(user,key):
                    setattr(user,key,value)

    @classmethod
    def get_number(cls):
        return len(cls.users)