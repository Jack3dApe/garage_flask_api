import logging
from models.invoice import Invoice
from utils.database import db
from datetime import datetime

logger = logging.getLogger(__name__)

def get_all_invoices():
    """
    Retrieve all invoices.
    :return: list: A list of dictionaries containing invoice information.
    """
    try:
        invoices = Invoice.query.all()
        return [
            {
                "invoice_id": invoice.invoice_id,
                "client_id": invoice.client_id,
                "issued_at": invoice.issued_at,
                "total": invoice.total,
                "iva": invoice.iva,
                "total_with_iva": invoice.total_with_iva,
            }
            for invoice in invoices
        ]
    except Exception as e:
        logger.error(f"Error fetching all invoices: {e}")
        return {"error": "Internal Server Error"}

def get_invoice(invoice_id):
    """
    Retrieve an invoice by ID.
    :param invoice_id: The ID of the invoice to retrieve.
    :return: dict: A dictionary containing the invoice's information or None if not found.
    """
    try:
        invoice = Invoice.query.get(invoice_id)
        if not invoice:
            return None
        return {
            "invoice_id": invoice.invoice_id,
            "client_id": invoice.client_id,
            "issued_at": invoice.issued_at,
            "total": invoice.total,
            "iva": invoice.iva,
            "total_with_iva": invoice.total_with_iva,
        }
    except Exception as e:
        logger.error(f"Error fetching invoice {invoice_id}: {e}")
        raise

def create_invoice(client_id, issued_at, total, iva, total_with_iva):
    """
    Create a new invoice.
    :param client_id: The ID of the associated client.
    :param issued_at: The date and time the invoice was issued.
    :param total: The total amount for the invoice.
    :param iva: The IVA (tax) applied to the invoice.
    :param total_with_iva: The total amount including IVA.
    :return: dict: A dictionary containing the created invoice's information.
    """
    try:
        issued_at_obj = datetime.strptime(issued_at, "%Y-%m-%d %H:%M:%S")
        invoice = Invoice(
            client_id=client_id,
            issued_at=issued_at_obj,
            total=total,
            iva=iva,
            total_with_iva=total_with_iva
        )
        db.session.add(invoice)
        db.session.commit()
        return {
            "invoice_id": invoice.invoice_id,
            "client_id": invoice.client_id,
            "issued_at": invoice.issued_at,
            "total": invoice.total,
            "iva": invoice.iva,
            "total_with_iva": invoice.total_with_iva,
        }
    except Exception as e:
        logger.error(f"Error creating invoice: {e}")
        db.session.rollback()
        return {"error": "Internal Server Error"}

def update_invoice(invoice_id, client_id, issued_at, total, iva, total_with_iva):
    """
    Update an existing invoice.
    :param invoice_id: The ID of the invoice to update.
    :param client_id: The new client ID associated with the invoice.
    :param issued_at: The new issue date and time.
    :param total: The new total amount for the invoice.
    :param iva: The new IVA (tax) applied to the invoice.
    :param total_with_iva: The new total amount including IVA.
    :return: dict: A dictionary containing the updated invoice's information or an error message.
    """
    try:
        issued_at_obj = datetime.strptime(issued_at, "%Y-%m-%d %H:%M:%S")
        invoice = Invoice.query.get(invoice_id)
        if not invoice:
            return {"error": f"Invoice with ID {invoice_id} not found."}, 404

        invoice.client_id = client_id
        invoice.issued_at = issued_at_obj
        invoice.total = total
        invoice.iva = iva
        invoice.total_with_iva = total_with_iva

        db.session.commit()
        return {
            "invoice_id": invoice.invoice_id,
            "client_id": invoice.client_id,
            "issued_at": invoice.issued_at,
            "total": invoice.total,
            "iva": invoice.iva,
            "total_with_iva": invoice.total_with_iva,
        }
    except Exception as e:
        logger.error(f"Error updating invoice {invoice_id}: {e}")
        db.session.rollback()
        return {"error": "Internal Server Error"}, 500

def delete_invoice(invoice_id):
    """
    Delete an invoice.
    :param invoice_id: The ID of the invoice to delete.
    :return: dict: A dictionary containing the deleted invoice's information or None if not found.
    """
    try:
        invoice = Invoice.query.get(invoice_id)
        if not invoice:
            return None

        db.session.delete(invoice)
        db.session.commit()
        return {
            "invoice_id": invoice.invoice_id,
            "client_id": invoice.client_id,
            "issued_at": invoice.issued_at,
            "total": invoice.total,
            "iva": invoice.iva,
            "total_with_iva": invoice.total_with_iva,
        }
    except Exception as e:
        logger.error(f"Error deleting invoice {invoice_id}: {e}")
        db.session.rollback()
        return {"error": "Internal Server Error"}, 500
