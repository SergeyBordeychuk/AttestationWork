from rest_framework.exceptions import ValidationError

class TitleValidator:
    def __init__(self, title):
        self.title = title

    def __call__(self, attrs):
        title = attrs.get(self.title)
        if ('ерунда' in title.lower()) or ('глупость'in title.lower()) or ('чепуха' in title.lower()):
            raise ValidationError('The title has bad words')
