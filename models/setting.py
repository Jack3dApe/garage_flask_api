from utils.database import db

class Setting(db.Model):
    """
    Represents the 'settings' table in the database.

    Attributes:
        setting_id (int): Primary key for each setting.
        key_name (str): The unique key name of the setting.
        value (str): The value associated with the key.
        updated_at (datetime): Timestamp of the last update.
    """
    __tablename__ = 'setting'

    setting_id = db.Column(db.Integer, primary_key=True)
    key_name = db.Column(db.String(100), unique=True, nullable=False)
    value = db.Column(db.String(255), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return f"<Setting {self.key_name} - Value: {self.value}>"
