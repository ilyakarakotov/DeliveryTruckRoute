from datetime import datetime


class Truck:
    def __init__(self, time, driver):
        self.time = time
        self.miles = 0
        self.package_capacity = 16
        self.packages_loaded = []
        self.driver = driver

    def __str__(self):
        result = "Truck Info:\nDriver ID: {}\n".format(self.driver)
        result += "Leave Time: {}\n".format(self.time)
        result += "Packages:\n"
        for package in self.packages_loaded:
            result += f'{package}\n'
        return result

    def add_package(self, package):
        # if the number of packages loaded is less than the capacity, load the package to the truck
        if self.package_capacity > len(self.packages_loaded):
            self.packages_loaded.append(package)
            package.departure_time = self.time
        else:
            print('Truck is at maximum capacity')