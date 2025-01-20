import logging
from models.invoice_item import InvoiceItem
from utils.database import db

logger = logging.getLogger(__name__)

def get_all_invoice_items():
    """
    Retrieve all invoice items.
    :return: list: A list of dictionaries containing invoice item information.
    """
    try:
        invoice_items = InvoiceItem.query.all()
        return [
            {
                "item_id": item.item_id,
                "description": item.description,
                "cost": item.cost,
                "invoice_id": item.invoice_id,
                "task_id": item.task_id,
            }
            for item in invoice_items
        ]
    except Exception as e:
        logger.error(f"Error fetching all invoice items: {e}")
        return {"error": "Internal Server Error"}

def get_invoice_item(item_id):
    """
    Retrieve an invoice item by ID.
    :param item_id: The ID of the invoice item to retrieve.
    :return: dict: A dictionary containing the invoice item's information or None if not found.
    """
    try:
        invoice_item = InvoiceItem.query.get(item_id)
        if not invoice_item:
            return None
        return {
            "item_id": invoice_item.item_id,
            "description": invoice_item.description,
            "cost": invoice_item.cost,
            "invoice_id": invoice_item.invoice_id,
            "task_id": invoice_item.task_id,
        }
    except Exception as e:
        logger.error(f"Error fetching invoice item {item_id}: {e}")
        raise

def create_invoice_item(description, cost, invoice_id, task_id=None):
    """
    Create a new invoice item.
    :param description: The description of the invoice item.
    :param cost: The cost of the invoice item.
    :param invoice_id: The ID of the associated invoice.
    :param task_id: The ID of the associated task (optional).
    :return: dict: A dictionary containing the created invoice item's information.
    """
    try:
        invoice_item = InvoiceItem(
            description=description,
            cost=cost,
            invoice_id=invoice_id,
            task_id=task_id
        )
        db.session.add(invoice_item)
        db.session.commit()
        return {
            "item_id": invoice_item.item_id,
            "description": invoice_item.description,
            "cost": invoice_item.cost,
            "invoice_id": invoice_item.invoice_id,
            "task_id": invoice_item.task_id,
        }
    except Exception as e:
        logger.error(f"Error creating invoice item: {e}")
        db.session.rollback()
        return {"error": "Internal Server Error"}

def update_invoice_item(item_id, description, cost, invoice_id, task_id=None):
    """
    Update an existing invoice item.
    :param item_id: The ID of the invoice item to update.
    :param description: The new description of the invoice item.
    :param cost: The new cost of the invoice item.
    :param invoice_id: The ID of the associated invoice.
    :param task_id: The ID of the associated task (optional).
    :return: dict: A dictionary containing the updated invoice item's information or an error message.
    """
    try:
        invoice_item = InvoiceItem.query.get(item_id)
        if not invoice_item:
            return {"error": f"Invoice item with ID {item_id} not found."}, 404

        # Update the invoice item's attributes
        invoice_item.description = description
        invoice_item.cost = cost
        invoice_item.invoice_id = invoice_id
        invoice_item.task_id = task_id

        db.session.commit()

        return {
            "item_id": invoice_item.item_id,
            "description": invoice_item.description,
            "cost": invoice_item.cost,
            "invoice_id": invoice_item.invoice_id,
            "task_id": invoice_item.task_id,
        }
    except Exception as e:
        logger.error(f"Error updating invoice item {item_id}: {e}")
        db.session.rollback()
        return {"error": "Internal Server Error"}, 500

def delete_invoice_item(item_id):
    """
    Delete an invoice item.
    :param item_id: The ID of the invoice item to delete.
    :return: dict: A dictionary containing the deleted invoice item's information or None if not found.
    """
    try:
        invoice_item = InvoiceItem.query.get(item_id)
        if not invoice_item:
            return None

        db.session.delete(invoice_item)
        db.session.commit()
        return {
            "item_id": invoice_item.item_id,
            "description": invoice_item.description,
            "cost": invoice_item.cost,
            "invoice_id": invoice_item.invoice_id,
            "task_id": invoice_item.task_id,
        }
    except Exception as e:
        logger.error(f"Error deleting invoice item {item_id}: {e}")
        db.session.rollback()
        return {"error": "Internal Server Error"}, 500
