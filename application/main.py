from application import create_app
from application.routes.registerer import register_all_routes

# Create App
app = create_app()
# Register Routes
register_all_routes(app)

if __name__ == '__main__':
    app.run()