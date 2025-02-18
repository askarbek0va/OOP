from user_service import UserService
from user import User
from user_util import UserUtil

from datetime import datetime

if __name__=='__main__':
    name=input('Your name:')
    surname=input('Your surname:')

    user= User(UserUtil.generate_user_id(),name,surname, email=UserUtil.generate_email(name,surname,'example.com'), password=UserUtil.generate_password(), birthday=datetime(2005,12,8))

    print(user.get_details())
    print(f'Age: {user.get_age()}')

    print(UserUtil.generate_password())

    UserService.add_user(user)
    print(UserService.find_user(user.user_id).get_details())
    print(f'Number of users: {UserService.get_number()}')






