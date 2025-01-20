from utils.database import db


class InvoiceItem(db.Model):
    """
    InvoiceItem model: This class represents the 'InvoiceItem' table in the database.

    Attributes:
        item_id (int): Primary key, unique identifier for each invoice item.
        description (str): Description of the invoice item.
        cost (float): Cost of the invoice item.
        invoice_id (int): Foreign key referencing the associated invoice.
        task_id (int): Foreign key referencing the associated task (optional).
    """
    # Primary key column
    item_id = db.Column(db.Integer, primary_key=True)

    # Invoice item details
    description = db.Column(db.Text, nullable=False)  # Item description (mandatory)
    cost = db.Column(db.Float, nullable=False)  # Cost of the item (mandatory)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.invoice_id'), nullable=False) # Foreign key to Invoice
    task_id = db.Column(db.Integer, db.ForeignKey('task.task_id'), nullable=True)  # Foreign key to Task (optional)

    # Relationships
    invoice = db.relationship(
        'Invoice',
        backref='invoice_items',
        overlaps="items,parent_invoice"
    )  # Relationship with Invoice model
    task = db.relationship('Task', backref='invoice_items')  # Relationship with Task model

    def __repr__(self):
        """
        String representation of the InvoiceItem object.

        :return: A string showing the description and cost of the item.
        """
        return f"<InvoiceItem {self.description} - Cost: {self.cost}>"
