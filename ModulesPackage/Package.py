import datetime


class Package:
    def __init__(self, package_id, delivery_addy, city, zip_code, deadline, weight, status, notes):
        self.package_id = package_id
        self.delivery_addy = delivery_addy
        if deadline == 'EOD':
            # self.deadline = datetime.timedelta(hours=23, minutes=59)
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

    # def __str__(self):
    #     return f'ID: {self.package_id}, Address: {self.delivery_addy}, Delivery Deadline: {self.deadline}, City: {self.city}, Zip code: {self.zip_code}, Weight (KG): {self.weight}, Status: {self.status}, Departure Time: {self.departure_time}, Delivery Time: {self.delivery_time}, Notes: {self.notes}'
    #
    # def __repr__(self):
    #     return f'ID: {self.package_id}, Address: {self.delivery_addy}, Delivery Deadline: {self.deadline}, City: {self.city}, Zip code: {self.zip_code}, Weight (KG): {self.weight}, Status: {self.status}, Departure Time: {self.departure_time}, Delivery Time: {self.delivery_time}, Notes: {self.notes}'

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

    # this function sets the status of the package at a certain time
    def set_status_at_time(self, time):
        if time >= self.delivery_time:
            self.status = "Delivered"
        elif self.departure_time < time:
            self.status = "En route"
        else:
            self.status = "At the hub"
