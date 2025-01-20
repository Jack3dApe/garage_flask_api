import logging
from flask_restx import Namespace, Resource
from werkzeug.exceptions import HTTPException
from services.invoice_item_service import (
    get_all_invoice_items,
    get_invoice_item,
    create_invoice_item,
    update_invoice_item,
    delete_invoice_item
)
from utils.utils import generate_swagger_model
from models.invoice_item import InvoiceItem

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Namespace for managing invoice items
invoice_items_ns = Namespace('invoice_item', description='CRUD operations for managing invoice items')

# Generate the Swagger model for the invoice item resource
invoice_item_model = generate_swagger_model(
    api=invoice_items_ns,          # Namespace to associate with the model
    model=InvoiceItem,             # SQLAlchemy model representing the invoice item resource
    exclude_fields=[],             # No excluded fields in this model
    readonly_fields=['item_id']    # Fields that cannot be modified
)


@invoice_items_ns.route('/')
class InvoiceItemList(Resource):
    """
    Handles operations on the collection of invoice items.
    Supports retrieving all invoice items (GET) and creating new invoice items (POST).
    """

    @invoice_items_ns.doc('get_all_invoice_items')
    @invoice_items_ns.marshal_list_with(invoice_item_model)
    def get(self):
        """
        Retrieve all invoice items.
        :return: List of all invoice items
        """
        try:
            # Fetch all invoice items from the service layer
            return get_all_invoice_items()
        except HTTPException as http_err:
            # Allow HTTP exceptions to propagate their status codes and messages
            logger.error(f"HTTP error while retrieving invoice items: {http_err}")
            raise http_err
        except Exception as e:
            # Log error and return a 500 status code
            logger.error(f"Error retrieving invoice items: {e}")
            invoice_items_ns.abort(500, "An error occurred while retrieving the invoice items.")

    @invoice_items_ns.doc('create_invoice_item')
    @invoice_items_ns.expect(invoice_item_model, validate=True)
    @invoice_items_ns.marshal_with(invoice_item_model, code=201)
    def post(self):
        """
        Create a new invoice item.
        :return: The created invoice item with HTTP status code 201
        """
        data = invoice_items_ns.payload  # Extract JSON payload
        try:
            # Call the service to create a new invoice item
            return create_invoice_item(data["description"], data["cost"], data["invoice_id"], data.get("task_id")), 201
        except HTTPException as http_err:
            logger.error(f"HTTP error while creating invoice item: {http_err}")
            raise http_err
        except Exception as e:
            # Log error and return a 500 status code
            logger.error(f"Error creating invoice item: {e}")
            invoice_items_ns.abort(500, "An error occurred while creating the invoice item.")


@invoice_items_ns.route('/<int:item_id>')
@invoice_items_ns.param('item_id', 'The ID of the invoice item')
class InvoiceItem(Resource):
    """
    Handles operations on a single invoice item.
    Supports retrieving (GET), updating (PUT), and deleting (DELETE) an invoice item.
    """

    @invoice_items_ns.doc('get_invoice_item')
    @invoice_items_ns.marshal_with(invoice_item_model)
    def get(self, item_id):
        """
        Retrieve an invoice item by ID.
        :param item_id: The ID of the invoice item
        :return: The invoice item details or 404 if not found
        """
        try:
            # Fetch invoice item by ID
            invoice_item = get_invoice_item(item_id)
            if not invoice_item:
                # Return a 404 error if invoice item does not exist
                invoice_items_ns.abort(404, f"Invoice item with ID {item_id} not found.")
            return invoice_item
        except HTTPException as http_err:
            logger.error(f"HTTP error while retrieving invoice item with ID {item_id}: {http_err}")
            raise http_err
        except Exception as e:
            # Log error and return a 500 status code
            logger.error(f"Error retrieving invoice item with ID {item_id}: {e}")
            invoice_items_ns.abort(500, "An error occurred while retrieving the invoice item.")

    @invoice_items_ns.doc('update_invoice_item')
    @invoice_items_ns.expect(invoice_item_model, validate=True)
    @invoice_items_ns.marshal_with(invoice_item_model)
    def put(self, item_id):
        """
        Update an invoice item by ID.
        :param item_id: The ID of the invoice item
        :return: The updated invoice item details or 404 if not found
        """
        data = invoice_items_ns.payload  # Extract JSON payload
        try:
            # Call the service to update the invoice item
            invoice_item = update_invoice_item(item_id, data["description"], data["cost"], data["invoice_id"], data.get("task_id"))
            if not invoice_item:
                # Return a 404 error if invoice item does not exist
                invoice_items_ns.abort(404, f"Invoice item with ID {item_id} not found.")
            return invoice_item
        except HTTPException as http_err:
            logger.error(f"HTTP error while updating invoice item with ID {item_id}: {http_err}")
            raise http_err
        except Exception as e:
            # Log error and return a 500 status code
            logger.error(f"Error updating invoice item with ID {item_id}: {e}")
            invoice_items_ns.abort(500, "An error occurred while updating the invoice item.")

    @invoice_items_ns.doc('delete_invoice_item')
    @invoice_items_ns.response(204, 'Invoice item successfully deleted')
    def delete(self, item_id):
        """
        Delete an invoice item by ID.
        :param item_id: The ID of the invoice item
        :return: HTTP 204 status code if deleted successfully or 404 if not found
        """
        try:
            # Call the service to delete the invoice item
            invoice_item = delete_invoice_item(item_id)
            if not invoice_item:
                # Return a 404 error if invoice item does not exist
                invoice_items_ns.abort(404, f"Invoice item with ID {item_id} not found.")
            return '', 204  # Return no content with status code 204
        except HTTPException as http_err:
            logger.error(f"HTTP error while deleting invoice item with ID {item_id}: {http_err}")
            raise http_err
        except Exception as e:
            # Log error and return a 500 status code
            logger.error(f"Error deleting invoice item with ID {item_id}: {e}")
            invoice_items_ns.abort(500, "An error occurred while deleting the invoice item.")
