import calendar


class DVD:
    def __init__(self, name: str, c_id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = c_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, c_id: int, name: str, date: str, age_restriction: int):
        s_date = date.split(".")
        return cls(name, c_id, int(s_date[2]), calendar.month_name[int(s_date[1])], age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})" \
               f" has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"
