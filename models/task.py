from utils.database import db


class Task(db.Model):
    """
    Task model: This class represents the 'Task' table in the database.

    Attributes:
        task_id (int): Primary key, unique identifier for each task.
        description (str): Description of the task.
        employee_id (int): Foreign key referencing the employee assigned to the task.
        start_date (date): Start date of the task.
        end_date (date): End date of the task (optional).
        status (str): Status of the task (e.g., 'pending', 'completed').
        work_id (int): Foreign key referencing the work associated with the task.
        created_at (datetime): Timestamp indicating when the task was created. Auto-generated by the database.
    """
    # Primary key column
    task_id = db.Column(db.Integer, primary_key=True)

    # Task details
    description = db.Column(db.Text, nullable=False)  # Task description (mandatory)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.employee_id'), nullable=False)  # Foreign key to Employee
    start_date = db.Column(db.Date, nullable=False)  # Start date (mandatory)
    end_date = db.Column(db.Date)  # End date (optional)
    status = db.Column(db.String(20), nullable=False, default="default_task_status")  # Status with default value 'pending'
    work_id = db.Column(db.Integer, db.ForeignKey('work.work_id'), nullable=False)  # Foreign key to Work

    # Audit information
    created_at = db.Column(db.DateTime, server_default=db.func.now())  # Timestamp for when the record was created

    # Relationships
    employee = db.relationship('Employee', backref='tasks')  # Relationship with Employee model
    work = db.relationship('Work', backref='tasks')  # Relationship with Work model


    def __repr__(self):
        """
        String representation of the Task object.

        :return: A string showing the task's description.
        """
        return f"<Task {self.description}>"
