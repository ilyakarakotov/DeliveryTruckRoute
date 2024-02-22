import datetime


class Package:
    def __init__(self, package_id, delivery_addy, city, zip_code, deadline, weight, status, notes):
        self.package_id = package_id
        self.delivery_addy = delivery_addy
        if deadline == 'EOD':
            self.deadline = datetime.timedelta(hours=23, minutes=59)
        else:
            parsed_date = datetime.datetime.strptime(deadline, '%I:%M %p')
            hours, minutes = parsed_date.hour, parsed_date.minute
            self.deadline = datetime.timedelta(hours=hours, minutes=minutes)
        self.city = city
        self.zip_code = zip_code
        self.weight = weight
        self.status = status
        self.loading_time = 0
        self.delivery_time = 0
        self.notes = notes

    def __str__(self):
        return f'ID: {self.package_id}, Address: {self.delivery_addy}, Delivery Deadline: {self.deadline}, City: {self.city}, Zip code: {self.zip_code}, Weight (KG): {self.weight}, Status: {self.status}, Loading Time: {self.loading_time}, Delivery Time: {self.delivery_time}, Notes: {self.notes}'

    def __repr__(self):
        return f'ID: {self.package_id}, Address: {self.delivery_addy}, Delivery Deadline: {self.deadline}, City: {self.city}, Zip code: {self.zip_code}, Weight (KG): {self.weight}, Status: {self.status}, Loading Time: {self.loading_time}, Delivery Time: {self.delivery_time}, Notes: {self.notes}'