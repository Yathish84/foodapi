from ..utils import db
from enum import Enum
from datetime import datetime

# create enum class for accessing our choices
class Size(Enum):
    SMALL='small'
    MEDIUM='medium'
    LARGE='large'
    EXTRA_LARGE='extra-large'


class OrderStatus(Enum):
    PENDING='pending'
    IN_TRANSIT='in-transit'
    DELIVERED='delivered'


class Order(db.Model):
    __tablename__='orders'

    id=db.Column(db.Integer(),primary_key=True)
    size=db.Column(db.Enum(Size),default=Size.SMALL)
    order_status=db.Column(db.Enum(OrderStatus) ,default=OrderStatus.PENDING)
    flavour=db.Column(db.String(),nullable=False)
    date_created=db.Column(db.DateTime(),default=datetime.utcnow)
    quantity=db.Column(db.Integer())
    customer=db.Column(db.Integer(),db.ForeignKey('users.id')) # foriegnkey ( tablename.columns)

    def __str__(self):
        return f"<Order {self.id}>"

    def save(self):
        db.session.add(self)
        db.session.commit()