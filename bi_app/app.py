"""
BI Forecasting Dashboard - Main Application
A simple Flask app with Bokeh integration
"""
import os
from flask import Flask
from flask_login import LoginManager

# Initialize login manager
login_manager = LoginManager()

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__, template_folder='templates')
    app.config['SECRET_KEY'] = 'your-secret-key-change-this'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    
    # Import db AFTER app is created to avoid issues
    from models import db, User
    
    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    # Import routes AFTER models/db
    from routes import dashboard_bp, auth_bp
    
    # User loader
    @login_manager.user_loader
    def load_user(user_id):
        from models import User
        return User.query.get(int(user_id))
    
    # Register blueprints
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(auth_bp)
    
    # Create tables and default user
    with app.app_context():
        db.create_all()
        
        try:
            if not User.query.filter_by(username='admin').first():
                admin = User(username='admin')
                admin.set_password('admin123')
                db.session.add(admin)
                db.session.commit()
                print("✅ Admin user created: admin / admin123")
        except Exception as e:
            print(f"⚠️  Could not create admin user: {e}")
    
    return app

# Create the app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
