from datetime import datetime

class User:

    def __init__(self, user_id,name,surname,email='', password='', birthday=datetime):
        self.user_id=user_id
        self.name=name
        self.surname=surname
        self.email=email
        self.password=password
        self.birthday=birthday


    def get_details(self):
        return (f'\nUser ID: {self.user_id} \nName: {self.name} \nSurname: {self.surname} \nEmail: {self.email} \nBirthday: {self.birthday.strftime('%Y-%m-%d')}')


    def get_age(self):
        today=datetime.today()
        age=today.year-self.birthday.year
        if (today.month, today.day) < (self.birthday.month, self.birthday.day):
            age -= 1
        return age




