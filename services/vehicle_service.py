import logging
from models.vehicle import Vehicle
from utils.database import db
from datetime import datetime

logger = logging.getLogger(__name__)

def get_all_vehicles():
    """
    Retrieve all vehicles.
    :return: list: A list of dictionaries containing vehicle information.
    """
    try:
        vehicles = Vehicle.query.all()
        return [
            {
                "vehicle_id": vehicle.vehicle_id,
                "brand": vehicle.brand,
                "model": vehicle.model,
                "year": vehicle.year,
                "license_plate": vehicle.license_plate,
                "client_id": vehicle.client_id,
                "created_at": vehicle.created_at,
            }
            for vehicle in vehicles
        ]
    except Exception as e:
        logger.error(f"Error fetching all vehicles: {e}")
        return {"error": "Internal Server Error"}

def get_vehicle(vehicle_id):
    """
    Retrieve a vehicle by ID.
    :param vehicle_id: The ID of the vehicle to retrieve.
    :return: dict: A dictionary containing the vehicle's information or None if not found.
    """
    try:
        vehicle = Vehicle.query.get(vehicle_id)
        if not vehicle:
            return None
        return {
            "vehicle_id": vehicle.vehicle_id,
            "brand": vehicle.brand,
            "model": vehicle.model,
            "year": vehicle.year,
            "license_plate": vehicle.license_plate,
            "client_id": vehicle.client_id,
            "created_at": vehicle.created_at,
        }
    except Exception as e:
        logger.error(f"Error fetching vehicle {vehicle_id}: {e}")
        raise  # Raise the exception to let the API layer handle it

def create_vehicle(brand, model, year, license_plate, client_id):
    """
    Create a new vehicle.
    :param brand: The brand of the vehicle.
    :param model: The model of the vehicle.
    :param year: The year of the vehicle.
    :param license_plate: The license plate of the vehicle.
    :param client_id: The ID of the associated client.
    :return: dict: A dictionary containing the created vehicle's information.
    """
    try:
        vehicle = Vehicle(
            brand=brand,
            model=model,
            year=year,
            license_plate=license_plate,
            client_id=client_id
        )
        db.session.add(vehicle)  # Save the new vehicle to the database
        db.session.commit()
        return {
            "vehicle_id": vehicle.vehicle_id,
            "brand": vehicle.brand,
            "model": vehicle.model,
            "year": vehicle.year,
            "license_plate": vehicle.license_plate,
            "client_id": vehicle.client_id,
            "created_at": vehicle.created_at,
        }
    except Exception as e:
        logger.error(f"Error creating vehicle: {e}")
        return {"error": "Internal Server Error"}

def update_vehicle(vehicle_id, brand, model, year, license_plate, client_id):
    """
    Update an existing vehicle.
    :param vehicle_id: The ID of the vehicle to update.
    :param brand: The new brand of the vehicle.
    :param model: The new model of the vehicle.
    :param year: The new year of the vehicle.
    :param license_plate: The new license plate of the vehicle.
    :param client_id: The new associated client ID.
    :return: dict: A dictionary containing the updated vehicle's information or None if not found.
    """
    try:
        vehicle = Vehicle.query.get(vehicle_id)
        if not vehicle:
            return {"error": f"Vehicle with ID {vehicle_id} not found."}, 404

        vehicle.brand = brand
        vehicle.model = model
        vehicle.year = year
        vehicle.license_plate = license_plate
        vehicle.client_id = client_id

        db.session.commit()
        return {
            "vehicle_id": vehicle.vehicle_id,
            "brand": vehicle.brand,
            "model": vehicle.model,
            "year": vehicle.year,
            "license_plate": vehicle.license_plate,
            "client_id": vehicle.client_id,
            "created_at": vehicle.created_at,
        }
    except Exception as e:
        db.session.rollback()  # Rollback on error
        logger.error(f"Error updating vehicle {vehicle_id}: {e}")
        return {"error": "Internal Server Error"}, 500

def delete_vehicle(vehicle_id):
    """
    Delete a vehicle.
    :param vehicle_id: The ID of the vehicle to delete.
    :return: Vehicle: The deleted vehicle object or None if not found.
    """
    try:
        vehicle = Vehicle.query.get(vehicle_id)
        if not vehicle:
            return None
        db.session.delete(vehicle)
        db.session.commit()
        return vehicle
    except Exception as e:
        db.session.rollback()  # Rollback on error
        logger.error(f"Error deleting vehicle {vehicle_id}: {e}")
        return {"error": "Internal Server Error"}, 500
