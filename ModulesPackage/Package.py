import datetime


# This class creates a package object
class Package:
    def __init__(self, package_id, delivery_addy, city, zip_code, deadline, weight, status, notes):
        self.package_id = package_id
        self.delivery_addy = delivery_addy
        # If the deadline is EOD, the deadline is set to EOD, otherwise deadline becomes timedelta object
        if deadline == 'EOD':
            self.deadline = 'EOD'
        else:
            parsed_date = datetime.datetime.strptime(deadline, '%I:%M %p')
            hours, minutes = parsed_date.hour, parsed_date.minute
            self.deadline = datetime.timedelta(hours=hours, minutes=minutes)
        self.city = city
        self.zip_code = zip_code
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None
        self.notes = notes

    def __str__(self):
        return f'{str(self.package_id): <5}' \
                f'{str(self.delivery_addy)[:30]: <30}' \
                f'{str(self.deadline): <10}' \
                f'{str(self.city): <20}' \
                f'{str(self.zip_code): <10}' \
                f'{str(self.weight): <10}' \
                f'{str(self.status): <20}' \
                f'{str(self.departure_time): <20}' \
                f'{str(self.delivery_time): <20}' \
                f'\t{str(self.notes): <20}'

    def __repr__(self):
        return f'{str(self.package_id): <5}' \
                f'{str(self.delivery_addy)[:30]: <30}' \
                f'{str(self.deadline): <10}' \
                f'{str(self.city): <20}' \
                f'{str(self.zip_code): <10}' \
                f'{str(self.weight): <10}' \
                f'{str(self.status): <20}' \
                f'{str(self.departure_time): <20}' \
                f'{str(self.delivery_time): <20}' \
                f'\t{str(self.notes): <20}'

    # This function sets the status of the package based on a certain time
    def set_status_at_time(self, time):
        if time >= self.delivery_time:
            self.status = "Delivered"
        elif self.departure_time < time:
            self.status = "En route"
        else:
            self.status = "At the hub"
