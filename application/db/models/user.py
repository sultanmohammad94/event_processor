from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import List
from application.utils.list_helpers import find_by_id


@dataclass
class UserEntity:
    """This class represents a user entity"""
    id:int
    first_name: str
    last_name: str
    email: str

@dataclass
class BaseUserRepository:
    
    @abstractmethod
    def save(self, user: UserEntity)->None:
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, id: int)->None:
        raise NotImplementedError
    
    @abstractmethod
    def get(self, id: int)->UserEntity:
        raise NotImplementedError
    
    @abstractmethod
    def get_all(self)->List[UserEntity]:
        raise NotImplementedError


class UserListRepository(BaseUserRepository):
    def __init__(self):
        self.repository: list = []
        
    def save(self, user: UserEntity)->None:
        if not user:
            raise ValueError('Can not save Empty user')
        self.repository.append(user)
        
    
    def delete(self, id: int)->None:
        try:
            user: UserEntity = find_by_id(self.repository, id)
            self.repository.remove(user)
        except Exception as e:
            raise ValueError(f'Could not delete the User with ID {id}')
        
            
    
    def get(self, id: int)->UserEntity:    
        user: UserEntity = find_by_id(self.repository, id)
        if not user:
            raise ValueError('User not found Error')
        return user
    
    def get_all(self)->List[UserEntity]:
        return self.repository

    @property
    def total(self)->int:
        return len(self.repository)
    