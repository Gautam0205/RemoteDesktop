from app import db
from sqlalchemy.dialects.postgresql import JSON
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """User model to represent users in the database."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(15), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    desk_id = db.Column(db.String(20))
    _password = db.Column(db.String(256), nullable=False)  # Stored as a hash
    is_online = db.Column(db.Boolean, default=True)
    contacts = db.Column(JSON)

    def __init__(
        self, ip_address, name, desk_id, password, is_online=True, contacts=None
    ):
        self.ip_address = ip_address
        self.name = name
        self.desk_id = desk_id
        self.password = password
        self.is_online = is_online
        self.contacts = contacts

    @property
    def password(self):
        """Getter method for password."""
        raise AttributeError("Password is not a readable attribute.")

    @password.setter
    def password(self, password):
        """Setter method for password that automatically hashes it."""
        self._password = generate_password_hash(password)

    def verify_password(self, password):
        """Verify the entered password against the hashed password."""
        return check_password_hash(self._password, password)
