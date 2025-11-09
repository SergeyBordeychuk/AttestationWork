from datetime import date

from rest_framework.exceptions import ValidationError


class EmailValidator:
    def __init__(self, email):
        self.email = email

    def __call__(self, value):
        email = value.get(self.email)
        if not (('mail.ru' in email) or ('yandex.ru' in email)):
            raise ValidationError('Invalid email')


class PasswordValidator:
    def __init__(self, password):
        self.password = password

    def __call__(self, value):
        password = value.get(self.password)
        if len(password) < 8:
            raise ValidationError('Password too short')
        if not (('1' in password) or ('2' in password) or ('3' in password) or ('4' in password) or (
                '5' in password) or ('6' in password) or ('7' in password) or ('8' in password) or (
                        '9' in password) or ('0' in password)):
            raise ValidationError('Password without numbers')

class AgeValidator:
    def __init__(self, birthday):
        self.birthday = birthday

    def __call__(self, attrs):
        birthday = attrs.get(self.birthday)
        print(str(date.today()))
        print(str(birthday))
        if int(str(date.today())[:4])-int(str(birthday)[:4]) < 18:
            raise ValidationError('The age is too low')
        if int(str(date.today())[:4]) - int(str(birthday)[:4]) == 18:
            if int(str(date.today())[5:7])-int(str(birthday)[5:7]) < 0:
                raise ValidationError('The age is too low')
            else:
                if int(str(date.today())[8:10])-int(str(birthday)[8:10]) <= 0:
                    raise ValidationError('The age is too low')
