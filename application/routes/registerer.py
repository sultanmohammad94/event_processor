from .users import USER_ROUTES

ROUTES = []
def register_all_routes(app):
    ROUTES.extend(USER_ROUTES)
    for item in ROUTES:
        route, view_func = item[0], item[1]
        app.add_url_rule(route, view_func=view_func)

        
    
