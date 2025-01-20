import logging
from models.task import Task
from utils.database import db
from datetime import datetime

logger = logging.getLogger(__name__)

def get_all_tasks():
    """
    Retrieve all tasks.
    :return: list: A list of dictionaries containing task information.
    """
    try:
        tasks = Task.query.all()
        return [
            {
                "task_id": task.task_id,
                "description": task.description,
                "employee_id": task.employee_id,
                "start_date": task.start_date,
                "end_date": task.end_date,
                "status": task.status,
                "work_id": task.work_id,
                "created_at": task.created_at,
            }
            for task in tasks
        ]
    except Exception as e:
        logger.error(f"Error fetching all tasks: {e}")
        return {"error": "Internal Server Error"}

def get_task(task_id):
    """
    Retrieve a task by ID.
    :param task_id: The ID of the task to retrieve.
    :return: dict: A dictionary containing the task's information or None if not found.
    """
    try:
        task = Task.query.get(task_id)
        if not task:
            return None
        return {
            "task_id": task.task_id,
            "description": task.description,
            "employee_id": task.employee_id,
            "start_date": task.start_date,
            "end_date": task.end_date,
            "status": task.status,
            "work_id": task.work_id,
            "created_at": task.created_at,
        }
    except Exception as e:
        logger.error(f"Error fetching task {task_id}: {e}")
        raise

def create_task(description, employee_id, start_date, end_date=None, status="pending", work_id=None):
    """
    Create a new task.
    :param description: The description of the task.
    :param employee_id: The ID of the employee assigned to the task.
    :param start_date: The start date of the task.
    :param end_date: The end date of the task (optional).
    :param status: The status of the task (default is 'pending').
    :param work_id: The ID of the associated work (optional).
    :return: dict: A dictionary containing the created task's information.
    """
    try:
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date_obj = None
        if end_date:
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()

        task = Task(
            description=description,
            employee_id=employee_id,
            start_date=start_date_obj,
            end_date=end_date_obj,
            status=status,
            work_id=work_id,
        )
        db.session.add(task)
        db.session.commit()
        return {
            "task_id": task.task_id,
            "description": task.description,
            "employee_id": task.employee_id,
            "start_date": task.start_date,
            "end_date": task.end_date,
            "status": task.status,
            "work_id": task.work_id,
            "created_at": task.created_at,
        }
    except Exception as e:
        logger.error(f"Error creating task: {e}")
        db.session.rollback()
        return {"error": "Internal Server Error"}

def update_task(task_id, description, employee_id, start_date, end_date=None, status="pending", work_id=None):
    """
    Update an existing task.
    :param task_id: The ID of the task to update.
    :param description: The new description of the task.
    :param employee_id: The new employee ID assigned to the task.
    :param start_date: The new start date of the task.
    :param end_date: The new end date of the task (optional).
    :param status: The new status of the task (default is 'pending').
    :param work_id: The new associated work ID (optional).
    :return: dict: A dictionary containing the updated task's information or an error message.
    """
    try:
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date_obj = None
        if end_date:
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()

        task = Task.query.get(task_id)
        if not task:
            return {"error": f"Task with ID {task_id} not found."}, 404

        task.description = description
        task.employee_id = employee_id
        task.start_date = start_date_obj
        task.end_date = end_date_obj
        task.status = status
        task.work_id = work_id

        db.session.commit()
        return {
            "task_id": task.task_id,
            "description": task.description,
            "employee_id": task.employee_id,
            "start_date": task.start_date,
            "end_date": task.end_date,
            "status": task.status,
            "work_id": task.work_id,
            "created_at": task.created_at,
        }
    except Exception as e:
        logger.error(f"Error updating task {task_id}: {e}")
        db.session.rollback()
        return {"error": "Internal Server Error"}, 500

def delete_task(task_id):
    """
    Delete a task.
    :param task_id: The ID of the task to delete.
    :return: dict: A dictionary containing the deleted task's information or None if not found.
    """
    try:
        task = Task.query.get(task_id)
        if not task:
            return None

        db.session.delete(task)
        db.session.commit()
        return {
            "task_id": task.task_id,
            "description": task.description,
            "employee_id": task.employee_id,
            "start_date": task.start_date,
            "end_date": task.end_date,
            "status": task.status,
            "work_id": task.work_id,
            "created_at": task.created_at,
        }
    except Exception as e:
        logger.error(f"Error deleting task {task_id}: {e}")
        db.session.rollback()
        return {"error": "Internal Server Error"}, 500
