from sqlalchemy import Column, Integer, String, Date, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column

from snoot.database.base import BaseModel


class UserModel(BaseModel):
    __tablename__ = "user"

    ## Derived Attributes
    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True,
                                         comment="The unique identifier for the user")
    active: Mapped[bool] = mapped_column(nullable=False, default=False, comment="Indicates user pet is given for stay")

    ## Personal Information
    first_name: Mapped[str] = mapped_column(String(60), nullable=False, comment="The first name of the user")
    last_name: Mapped[str] = mapped_column(String(60), nullable=False, comment="The last name of the user")
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False,
                                       comment="The email address of the user")

    phone: Mapped[str] = mapped_column(String(13), unique=True, nullable=True,
                                       comment="The phone number of the user")
    date_of_birth: Mapped[Date] = mapped_column(Date, nullable=False, comment="The date of birth of the user")
    gender: Mapped[str] = mapped_column(String(10), nullable=False, comment="The gender of the user")

    ## Extended Information
    profile_picture_url: Mapped[str] = mapped_column(String(255), nullable=True,
                                                     comment="The URL of the user's profile picture")
    pets: Mapped[list[int]] = mapped_column(JSON, nullable=True,
                                            comment="The list of pet IDs owned by the user stored as JSON array")

    ## Metadata
    created_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False,
                                                 comment="The timestamp when the user account was created")
    updated_at: Mapped[DateTime] = mapped_column(DateTime, nullable=True,
                                                 comment="The timestamp when the user account was last updated")
