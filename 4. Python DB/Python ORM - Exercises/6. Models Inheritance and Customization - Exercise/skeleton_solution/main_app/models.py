from datetime import timedelta

from django.core.exceptions import ValidationError
from django.db import models


# CUSTOM FIELDS:
class StudentIDField(models.PositiveIntegerField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MaskedCreditCardField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 20
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        super().to_python(value)

        if not isinstance(value, str):
            raise ValidationError(message="The card number must be a string")

        if not value.isdigit():
            raise ValidationError(message="The card number must contain only digits")

        if len(value) != 16:
            raise ValidationError(message="The card number must be exactly 16 characters long")

        return f"****-****-****-{value[-4:]}"


class BaseCharacter(models.Model):
    name = models.CharField(
        max_length=100
    )

    description = models.TextField()

    class Meta:
        abstract = True


class Mage(BaseCharacter):
    elemental_power = models.CharField(
        max_length=100
    )

    spellbook_type = models.CharField(
        max_length=100
    )


class Assassin(BaseCharacter):
    weapon_type = models.CharField(
        max_length=100
    )

    assassination_technique = models.CharField(
        max_length=100
    )


class DemonHunter(BaseCharacter):
    weapon_type = models.CharField(
        max_length=100
    )

    demon_slaying_ability = models.CharField(
        max_length=100
    )


class TimeMage(Mage):
    time_magic_mastery = models.CharField(
        max_length=100
    )

    temporal_shift_ability = models.CharField(
        max_length=100
    )


class Necromancer(Mage):
    raise_dead_ability = models.CharField(
        max_length=100
    )


class ViperAssassin(Assassin):
    venomous_strikes_mastery = models.CharField(
        max_length=100
    )

    venomous_bite_ability = models.CharField(
        max_length=100
    )


class ShadowbladeAssassin(Assassin):
    shadowstep_ability = models.CharField(
        max_length=100
    )


class VengeanceDemonHunter(DemonHunter):
    vengeance_mastery = models.CharField(
        max_length=100
    )

    retribution_ability = models.CharField(
        max_length=100
    )


class FelbladeDemonHunter(DemonHunter):
    felblade_ability = models.CharField(
        max_length=100
    )


class UserProfile(models.Model):
    username = models.CharField(
        max_length=70,
        unique=True
    )

    email = models.EmailField(
        unique=True
    )

    bio = models.TextField(
        null=True,
        blank=True
    )


class Message(models.Model):
    sender = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="sent_messages"
    )

    receiver = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="received_messages"
    )

    content = models.TextField()

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    is_read = models.BooleanField(
        default=False
    )

    def mark_as_read(self):
        self.is_read = True
        self.save()

    def mark_as_unread(self):
        self.is_read = False
        self.save()

    def reply_to_message(self, reply_content, receiver):
        new_message = Message.objects.create(
            sender=self.receiver,
            receiver=receiver,
            content=reply_content
        )

        return new_message

    def forward_message(self, sender, receiver):
        new_message = Message.objects.create(
            sender=sender,
            receiver=receiver,
            content=self.content
        )

        return new_message


class Student(models.Model):
    name = models.CharField(
        max_length=100
    )

    student_id = StudentIDField()


class CreditCard(models.Model):
    card_owner = models.CharField(
        max_length=100
    )

    card_number = MaskedCreditCardField()


class Hotel(models.Model):
    name = models.CharField(
        max_length=100
    )

    address = models.CharField(
        max_length=200
    )


class Room(models.Model):
    hotel = models.ForeignKey(
        to='Hotel',
        on_delete=models.CASCADE
    )

    number = models.CharField(
        max_length=100,
        unique=True
    )

    capacity = models.PositiveIntegerField()

    total_guests = models.PositiveIntegerField()

    price_per_night = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def save(self, *args, **kwargs):
        if self.total_guests > self.capacity:
            raise ValidationError(message=f"Total guests are more than the capacity of the room")

        super().save(*args, **kwargs)
        return f"Room {self.number} created successfully"


class BaseReservation(models.Model):

    class Meta:
        abstract = True

    room = models.ForeignKey(
        to='Room',
        on_delete=models.CASCADE
    )

    start_date = models.DateField()

    end_date = models.DateField()

    def reservation_period(self):
        return (self.end_date - self.start_date).days

    def calculate_total_cost(self):
        total = self.reservation_period() * self.room.price_per_night

        return round(total, 1)


def check_dates(start, end):
    if start >= end:
        raise ValidationError(message=f"Start date cannot be after or in the same end date")


def overlapping_with_existing_reservation(reservation_type, curr_room, start, end):
    reservations = {
        'regular': RegularReservation,
        'special': SpecialReservation
    }

    another_room = reservations[reservation_type].objects.filter(
        room=curr_room,
        start_date__lte=end,
        end_date__gte=start
    )

    if another_room.exists():
        raise ValidationError(message=f"Room {curr_room.number} cannot be reserved")


class RegularReservation(BaseReservation):
    def save(self, *args, **kwargs):
        check_dates(self.start_date, self.end_date)

        overlapping_with_existing_reservation('regular', self.room, self.start_date, self.end_date)

        super().save(*args, **kwargs)
        return f"Regular reservation for room {self.room.number}"


class SpecialReservation(BaseReservation):
    def save(self, *args, **kwargs):
        check_dates(self.start_date, self.end_date)

        overlapping_with_existing_reservation('special', self.room, self.start_date, self.end_date)

        super().save(*args, **kwargs)
        return f"Special reservation for room {self.room.number}"

    def extend_reservation(self, days: int):
        another_room = SpecialReservation.objects.filter(
            room=self.room,
            start_date__lte=self.end_date,
            end_date__gte=self.start_date
        )

        if another_room.exists():
            raise ValidationError(f"Error during extending reservation")

        self.end_date = self.end_date + timedelta(days=days)

        return f"Extended reservation for room {self.room.number} with {days} days"
