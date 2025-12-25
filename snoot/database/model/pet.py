from sqlalchemy import Integer, String, JSON, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from snoot.database.base import BaseModel


class PetModel(BaseModel):
    __tablename__ = "user"

    ## Derived Attributes
    pet_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True,
                                        comment="The unique identifier for the pet")
    user_id: Mapped[int] = mapped_column(Integer, nullable=False,
                                         comment=" Foreign key referencing users.id (pet owner)")

    ## Personal Information
    pet_type: Mapped[str] = mapped_column(String(50), nullable=False, comment="Type of the pet (e.g., Dog, Cat)")
    name: Mapped[str] = mapped_column(String(50), nullable=False, comment="Name of the pet")
    image_urls: Mapped[list[str]] = mapped_column(JSON, nullable=True,
                                                  comment="List of image URLs of the pet stored as JSON array")
    description: Mapped[str] = mapped_column(String(500), nullable=True, comment="Description of the pet")
    created_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False,
                                                 comment="The timestamp when the pet profile was created")
    updated_at: Mapped[DateTime] = mapped_column(DateTime, nullable=True,
                                                 comment="The timestamp when the pet profile was last updated")
