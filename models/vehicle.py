from utils.database import db


# Model definition for the 'Vehicle' table
class Vehicle(db.Model):
    """
    Represents a vehicle in the database.

    Attributes:
        vehicle_id (int): The primary key for the vehicle table.
        brand (str): The brand of the vehicle. Cannot be null.
        model (str): The model of the vehicle. Cannot be null.
        year (int): The year of the vehicle. Cannot be null.
        license_plate (str): The license plate of the vehicle. Must be unique and cannot be null.
        client_id (int): Foreign key referencing the client associated with the vehicle. Cannot be null.
        created_at (datetime): Timestamp when the vehicle was created. Defaults to the current time.
    """

    # Define columns for the table
    vehicle_id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each vehicle
    brand = db.Column(db.String(80), nullable=False)  # Vehicle brand
    model = db.Column(db.String(80), nullable=False)  # Vehicle model
    year = db.Column(db.Integer, nullable=False)  # Year of the vehicle
    license_plate = db.Column(db.String(20), unique=True, nullable=False)  # Unique license plate
    client_id = db.Column(db.Integer, db.ForeignKey('client.client_id'), nullable=False)  # Associated client
    created_at = db.Column(db.DateTime, server_default=db.func.now())  # Auto-generated timestamp

    # Relationship (optional, for accessing related client data)
    client = db.relationship('Client', backref='vehicles', lazy=True)

    def __repr__(self):
        """
        String representation of the Vehicle object.
        Useful for debugging and logging purposes.
        """
        return f"<Vehicle {self.license_plate} - {self.brand} {self.model}>"
