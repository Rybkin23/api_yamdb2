from rest_framework.serializers import ValidationError


def validate_username(value):

    if not isinstance(value, str):
        raise ValidationError('username не строковый!!!')
    if value.lower() == 'me':
        raise ValidationError('username не должен быть равен me!!!')
    return value
