from application.controllers.users import UserController

user_controller = UserController()
        
USER_ROUTES = [
    ('/', user_controller.welcome_user)
]



