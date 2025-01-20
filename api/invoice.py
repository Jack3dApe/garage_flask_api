import logging
from flask_restx import Namespace, Resource, abort
from models.invoice import Invoice
from services.invoice_service import get_all_invoices, get_invoice, create_invoice, update_invoice, delete_invoice
from utils.utils import generate_swagger_model
from werkzeug.exceptions import HTTPException, BadRequest, NotFound

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Namespace for invoices
invoices_ns = Namespace('invoice', description='CRUD operations for managing invoices')

# Generate the Swagger model for invoices
invoice_model = generate_swagger_model(
    api=invoices_ns,
    model=Invoice,
    exclude_fields=[],
    readonly_fields=['invoice_id']
)

# Routes for managing invoices
@invoices_ns.route('/')
@invoices_ns.response(500, 'Internal Server Error')
class InvoiceList(Resource):
    @invoices_ns.doc('get_all_invoices')
    @invoices_ns.marshal_list_with(invoice_model)
    def get(self):
        try:
            invoices = get_all_invoices()
            return invoices
        except HTTPException as http_err:
            raise http_err
        except Exception as e:
            logger.error(f"Error fetching all invoices: {e}")
            invoices_ns.abort(500, "Internal Server Error")

    @invoices_ns.doc('create_invoice')
    @invoices_ns.expect(invoice_model)
    @invoices_ns.marshal_with(invoice_model, code=201)
    @invoices_ns.response(400, 'Bad Request')
    def post(self):
        try:
            data = invoices_ns.payload
            invoice = create_invoice(
                client_id=data['client_id'],
                issued_at=data['issued_at'],
                total=data['total'],
                iva=data['iva'],
                total_with_iva=data['total_with_iva']
            )
            return invoice, 201
        except HTTPException as http_err:
            raise http_err
        except Exception as e:
            logger.error(f"Error creating invoice: {e}")
            invoices_ns.abort(400, "Bad Request")


@invoices_ns.route('/<int:invoice_id>')
@invoices_ns.response(404, 'Invoice ID not found')
@invoices_ns.response(500, 'Internal Server Error')
@invoices_ns.param('invoice_id', 'Invoice ID')
class Invoice(Resource):
    @invoices_ns.doc('get_invoice')
    @invoices_ns.marshal_with(invoice_model)
    def get(self, invoice_id):
        try:
            invoice = get_invoice(invoice_id)
            if not invoice:
                invoices_ns.abort(404, f"Invoice with ID {invoice_id} not found.")
            return invoice
        except HTTPException as http_err:
            raise http_err
        except Exception as e:
            logger.error(f"Error fetching invoice {invoice_id}: {e}")
            invoices_ns.abort(500, "Internal Server Error")

    @invoices_ns.doc('update_invoice')
    @invoices_ns.expect(invoice_model)
    @invoices_ns.marshal_with(invoice_model)
    @invoices_ns.response(400, 'Bad Request')
    def put(self, invoice_id):
        try:
            data = invoices_ns.payload
            updated_invoice = update_invoice(
                invoice_id,
                client_id=data['client_id'],
                issued_at=data['issued_at'],
                total=data['total'],
                iva=data['iva'],
                total_with_iva=data['total_with_iva']
            )
            if not updated_invoice:
                invoices_ns.abort(404, f"Invoice with ID {invoice_id} not found.")
            return updated_invoice
        except HTTPException as http_err:
            raise http_err
        except Exception as e:
            logger.error(f"Error updating invoice {invoice_id}: {e}")
            invoices_ns.abort(400, "Bad Request")

    @invoices_ns.doc('delete_invoice')
    def delete(self, invoice_id):
        try:
            deleted = delete_invoice(invoice_id)
            if not deleted:
                invoices_ns.abort(404, f"Invoice with ID {invoice_id} not found.")
            return '', 204
        except HTTPException as http_err:
            raise http_err
        except Exception as e:
            logger.error(f"Error deleting invoice {invoice_id}: {e}")
            invoices_ns.abort(500, "Internal Server Error")
