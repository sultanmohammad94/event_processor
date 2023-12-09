import factory
from factory import Faker
from application.db.models.user import UserEntity


class UserEntityFactory(factory.Factory):
    """This class Represents a user Factory"""
    class Meta:
        model = UserEntity
    
    id = Faker('random_int', min=1, max=1000)
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = Faker('email')
    