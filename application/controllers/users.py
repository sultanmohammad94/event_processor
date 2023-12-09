from application.services import users

class UserController:
    def __init__(self):
        self.__service = users.UserServices()
        
    def welcome_user(self):
        return self.__service.welcome()