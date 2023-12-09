import random
from unittest import TestCase
from typing import List
from application.db.models.user import UserEntity, UserListRepository
from application.factories.users import UserEntityFactory

class TestUserEntity(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.repository: UserListRepository = UserListRepository()

    def test_create_user(self)->None:
        user = UserEntityFactory()
        self.repository.save(user)
        self.assertEqual(self.repository.total, 1 )
        
    
    def test_get_user_by_id(self)->None:
        user = UserEntityFactory()
        self.repository.save(user)
        found_user: UserEntity = self.repository.get(user.id)
        self.assertIsNotNone(found_user, 'User should be found')
        self.assertEqual(found_user.id, user.id)
        
    def test_get_non_exist_user_by_id(self)->None:
        user = UserEntityFactory()
        self.repository.save(user)
        with self.assertRaises(ValueError) as context:
            id = random.randint(user.id+1, user.id+100)
            found_user: UserEntity = self.repository.get(id)
            self.assertEqual(str(context.exception), f'User with ID {id} not found')
            
    def test_get_all_users(self)->None:
        users = UserEntityFactory.create_batch(3)
        for user in users:
            self.repository.save(user)
        self.assertEqual(self.repository.total, 3)
    
    def test_delete_user(self)->None:
        users = UserEntityFactory.create_batch(100)
        _ = [self.repository.save(user) for user in users]
        old_total = self.repository.total
        id = random.choice(users).id
        self.repository.delete(id)
        new_total = self.repository.total
        self.assertEqual(new_total + 1, old_total)
        
    def test_delete_none_exist_user(self)->None:
        users = UserEntityFactory.create_batch(100)
        _ = [self.repository.save(user) for user in users]
        id =  random.randint(random.choice(users).id +1000, random.choice(users).id+2000)
        with self.assertRaises(ValueError) as context:
            self.repository.delete(id)
            self.assertEqual(context.exception, f'Could not delete the User with ID {id}')
        
        