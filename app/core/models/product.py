from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from app.core.models.base import Base

if TYPE_CHECKING:
    from app.core.models.order import Order
    from app.core.models.order_product_association import OrderProductAssociation


class Product(Base):
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
    orders: Mapped[list["Order"]] = relationship(
        secondary="order_product_association",
        back_populates="products",
    )
    orders_details: Mapped[list["OrderProductAssociation"]] = relationship(
        back_populates="product",
    )