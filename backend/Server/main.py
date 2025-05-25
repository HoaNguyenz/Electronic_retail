from flask import Flask
from flask_cors import CORS
from routes.home import home_bp
from routes.auth_routes import auth_bp
from routes.product_routes import product_bp
from routes.shopping_cart_routes import shopping_cart_bp
from routes.order_routes import order_bp
from routes.admin_routes import admin_bp
from routes.payment_routes import payment_bp

app = Flask(__name__)

# Allow CORS for a specific frontend origin
CORS(app, origins=["http://localhost:3000"]) 

# Register blueprints
app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(product_bp)
app.register_blueprint(shopping_cart_bp)
app.register_blueprint(order_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(payment_bp)

if __name__ == "__main__":
    app.run(debug=True)