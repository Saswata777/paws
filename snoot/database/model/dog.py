from sqlalchemy import Integer, String, JSON, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from snoot.database.base import BaseModel


class DogModel(BaseModel):
    __tablename__ = "dog"

    # identity & classification
    pet_id: Mapped[int] = mapped_column(Integer, nullable=False, unique=True,  comment="The pet id")
    breed: Mapped[str] = mapped_column(String(50), nullable=False, comment="The breed of the dog")
    is_mixed_breed: Mapped[bool] = mapped_column(nullable=False, comment="Indicates if the dog is a mixed breed")
    size_category: Mapped[str] = mapped_column(String(20), nullable=False, comment="The size category of the dog (e.g., Small, Medium, Large)")

    # physical attributes
    weight_kg: Mapped[float] = mapped_column(nullable=False, comment="The weight of the dog in kilograms")
    height_cm: Mapped[float] = mapped_column(nullable=False, comment="The height of the dog in centimeters")
    coat_type: Mapped[str] = mapped_column(String(30), nullable=False, comment="The type of coat the dog has (e.g., Short, Long, Curly)")
    color: Mapped[str] = mapped_column(String(30), nullable=False, comment="The color of the dog's coat")
    tail_type: Mapped[str] = mapped_column(String(30), nullable=True, comment="The type of tail the dog has (e.g., Straight, Curled)")
    ear_type: Mapped[str] = mapped_column(String(30), nullable=True, comment="The type of ears the dog has (e.g., Floppy, Pointed)")

    # behavior & training
    is_trained: Mapped[bool] = mapped_column(nullable=False, comment="Indicates if the dog is trained")
    training_level: Mapped[str] = mapped_column(String(50), nullable=True, comment="The level of training the dog has received (e.g., Basic, Advanced)")
    energy_level: Mapped[str] = mapped_column(String(20), nullable=False, comment="The energy level of the dog (e.g., Low, Medium, High)")
    temperament: Mapped[str] = mapped_column(String(100), nullable=True, comment="The temperament of the dog (e.g., Friendly, Aggressive, Shy)")
    barks_a_lot: Mapped[bool] = mapped_column(nullable=False, comment="Indicates if the dog barks a lot")
    good_with_kids: Mapped[bool] = mapped_column(nullable=False, comment="Indicates if the dog is good with kids")
    good_with_other_pets: Mapped[bool] = mapped_column(nullable=False, comment="Indicates if the dog is good with other pets")

    # health & medical
    vaccinated : Mapped[bool] = mapped_column(nullable=False, comment="Indicates if the dog is vaccinated")
    neutered: Mapped[bool] = mapped_column(nullable=False, comment="Indicates if the dog is neutered/spayed")
    allergies: Mapped[str] = mapped_column(String(200), nullable=True, comment="Any known allergies the dog has")
    known_conditions: Mapped[str] = mapped_column(String(200), nullable=True, comment="Any known medical conditions the dog has")
    last_vet_visit: Mapped[DateTime] = mapped_column(DateTime, nullable=True, comment="The date of the dog's last vet visit")

    # lifestyle & preferences
    preferred_food: Mapped[str] = mapped_column(String(100), nullable=True, comment="The preferred food of the dog")
    daily_walk_minutes: Mapped[int] = mapped_column(nullable=False, comment="The recommended daily walk time in minutes")
    needs_grooming: Mapped[bool] = mapped_column(nullable=False, comment="Indicates if the dog needs regular grooming")
    last_grooming_date: Mapped[DateTime] = mapped_column(DateTime, nullable=True, comment="The date of the dog's last grooming session")

    # future
    microchip_id: Mapped[str] = mapped_column(String(50), nullable=True, comment="The microchip ID of the dog")
    registration_number: Mapped[str] = mapped_column(String(50), nullable=True, comment="The registration number of the dog, if applicable")
    insurance_provider: Mapped[str] = mapped_column(String(100), nullable=True, comment="The insurance provider for the dog, if applicable")
    insurance_policy_number: Mapped[str] = mapped_column(String(50), nullable=True, comment="The insurance policy number for the dog, if applicable")

