from utils.database import db


# Model definition for the 'Work' table
class Work(db.Model):
    """
    Represents a work (repair job) in the database.

    Attributes:
        work_id (int): The primary key for the work table.
        description (str): A brief description of the work. Cannot be null.
        cost (float): The cost of the work. Cannot be null.
        status (str): The current status of the work (e.g., pending, in_progress, completed). Cannot be null.
        vehicle_id (int): Foreign key referencing the vehicle associated with this work. Cannot be null.
        created_at (datetime): Timestamp when the work was created. Defaults to the current time.
        start_date (date): The date when the work started.
        end_date (date): The date when the work was completed.
    """

    # Define columns for the table
    work_id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each work
    description = db.Column(db.String(255), nullable=False)  # Brief description of the work
    cost = db.Column(db.Float, nullable=False)  # Cost of the work
    status = db.Column(db.String(20), nullable=False)  # Current status of the work
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.vehicle_id'), nullable=False)  # Associated vehicle
    created_at = db.Column(db.DateTime, server_default=db.func.now())  # Auto-generated timestamp
    start_date = db.Column(db.Date, nullable=True)  # Start date of the work
    end_date = db.Column(db.Date, nullable=True)  # End date of the work

    # Relationship (optional, for accessing related vehicle data)
    vehicle = db.relationship('Vehicle', backref='works', lazy=True)

    def __repr__(self):
        """
        String representation of the Work object.
        Useful for debugging and logging purposes.
        """
        return f"<Work {self.description}, Status: {self.status}>"
