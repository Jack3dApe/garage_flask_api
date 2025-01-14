import logging
from utils.database import db
from models.work import Work

logger = logging.getLogger(__name__)


def get_all_works():
    """
    Retrieve all works.
    :return: list: A list of dictionaries containing information about all works.
    """
    try:
        works = Work.query.all()  # Retrieve all works from the database
        return [
            {
                "work_id": work.work_id,
                "description": work.description,
                "cost": work.cost,
                "status": work.status,
                "vehicle_id": work.vehicle_id,
                "created_at": work.created_at,
                "start_date": work.start_date,
                "end_date": work.end_date,
            }
            for work in works
        ]
    except Exception as e:
        logger.error(f"Error fetching all works: {e}")
        return {"error": "Internal Server Error"}


def get_work(work_id):
    """
    Retrieve a work by ID.
    :param work_id: The ID of the work to retrieve.
    :return: dict: A dictionary containing the work's information or None if not found.
    """
    try:
        work = Work.query.get(work_id)
        if not work:
            return None
        return {
            "work_id": work.work_id,
            "description": work.description,
            "cost": work.cost,
            "status": work.status,
            "vehicle_id": work.vehicle_id,
            "created_at": work.created_at,
            "start_date": work.start_date,
            "end_date": work.end_date,
        }
    except Exception as e:
        logger.error(f"Error fetching work {work_id}: {e}")
        return {"error": "Internal Server Error"}


def create_work(description, cost, status, vehicle_id, start_date=None, end_date=None):
    """
    Create a new work.
    :param description: The description of the work.
    :param cost: The cost of the work.
    :param status: The status of the work.
    :param vehicle_id: The ID of the associated vehicle.
    :param start_date: The start date of the work (optional).
    :param end_date: The end date of the work (optional).
    :return: dict: A dictionary containing the newly created work's information.
    """
    try:
        work = Work(
            description=description,
            cost=cost,
            status=status,
            vehicle_id=vehicle_id,
            start_date=start_date,
            end_date=end_date,
        )
        db.session.add(work)  # Add the new work to the database
        db.session.commit()  # Commit the changes
        return {
            "work_id": work.work_id,
            "description": work.description,
            "cost": work.cost,
            "status": work.status,
            "vehicle_id": work.vehicle_id,
            "created_at": work.created_at,
            "start_date": work.start_date,
            "end_date": work.end_date,
        }
    except Exception as e:
        logger.error(f"Error creating work: {e}")
        db.session.rollback()  # Rollback if there's an error
        return {"error": "Internal Server Error"}


def update_work(work_id, description=None, cost=None, status=None, vehicle_id=None, start_date=None, end_date=None):
    """
    Update an existing work.
    :param work_id: The ID of the work to update.
    :param description: The new description of the work (optional).
    :param cost: The new cost of the work (optional).
    :param status: The new status of the work (optional).
    :param vehicle_id: The ID of the associated vehicle (optional).
    :param start_date: The new start date of the work (optional).
    :param end_date: The new end date of the work (optional).
    :return: dict: A dictionary containing the updated work's information or None if not found.
    """
    try:
        work = Work.query.get(work_id)
        if not work:
            return None

        # Update fields if new values are provided
        if description:
            work.description = description
        if cost:
            work.cost = cost
        if status:
            work.status = status
        if vehicle_id:
            work.vehicle_id = vehicle_id
        if start_date:
            work.start_date = start_date
        if end_date:
            work.end_date = end_date

        db.session.commit()  # Commit the changes
        return {
            "work_id": work.work_id,
            "description": work.description,
            "cost": work.cost,
            "status": work.status,
            "vehicle_id": work.vehicle_id,
            "created_at": work.created_at,
            "start_date": work.start_date,
            "end_date": work.end_date,
        }
    except Exception as e:
        logger.error(f"Error updating work {work_id}: {e}")
        db.session.rollback()  # Rollback if there's an error
        return {"error": "Internal Server Error"}


def delete_work(work_id):
    """
    Delete a work.
    :param work_id: The ID of the work to delete.
    :return: Work: The deleted work object or None if not found.
    """
    try:
        work = Work.query.get(work_id)
        if not work:
            return None

        db.session.delete(work)  # Delete the work
        db.session.commit()  # Commit the changes
        return work
    except Exception as e:
        logger.error(f"Error deleting work {work_id}: {e}")
        db.session.rollback()  # Rollback if there's an error
        return {"error": "Internal Server Error"}
