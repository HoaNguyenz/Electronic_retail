from flask import Flask
from routes.home import home_bp
from routes.auth_routes import auth_bp
from routes.product_routes import product_bp
from routes.shopping_cart_routes import shopping_cart_bp
from routes.order_routes import order_bp
from routes.admin_routes import admin_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(product_bp)
app.register_blueprint(shopping_cart_bp)
app.register_blueprint(order_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(debug=True)
