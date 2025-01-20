from utils.database import db


class Invoice(db.Model):
    """
    Invoice model: This class represents the 'Invoice' table in the database.

    Attributes:
        invoice_id (int): Primary key, unique identifier for each invoice.
        client_id (int): Foreign key referencing the client associated with the invoice.
        issued_at (datetime): The date and time when the invoice was issued.
        total (float): The total amount for the invoice.
        iva (float): The IVA (tax) applied to the invoice.
        total_with_iva (float): The total amount including IVA.
    """
    # Primary key column
    invoice_id = db.Column(db.Integer, primary_key=True)

    # Invoice details
    client_id = db.Column(db.Integer, db.ForeignKey('client.client_id'), nullable=False)
    issued_at = db.Column(db.DateTime, nullable=False)  # Issue date and time (mandatory)
    total = db.Column(db.Float, nullable=False)  # Total amount (mandatory)
    iva = db.Column(db.Float, nullable=False)  # IVA (mandatory)
    total_with_iva = db.Column(db.Float, nullable=False)  # Total including IVA (mandatory)

    # Relationships
    client = db.relationship('Client', backref='invoices')
    items = db.relationship(
        'InvoiceItem',
        backref='parent_invoice',
        cascade='all, delete-orphan',
        overlaps="invoice_items"
    ) # Relationship with InvoiceItem model

    def __repr__(self):
        """
        String representation of the Invoice object.

        :return: A string showing the invoice ID and total amount.
        """
        return f"<Invoice {self.invoice_id} - Total: {self.total_with_iva}>"
