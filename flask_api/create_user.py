from app import app, db, User

def create_admin_user(username="admin", password="admin123"):
    with app.app_context():
        if User.query.filter_by(username=username).first():
            print(f"User '{username}' already exists")
            return
        
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        print(f"User '{username}' created successfully")

if __name__ == "__main__":
    create_admin_user()

