class Truck:
    def __init__(self, truck_leave_time, package_capacity, driver, route):
        self.truck_leave_time = truck_leave_time
        self.package_capacity = package_capacity
        self.packages_loaded = []
        self.driver = driver
        self.route = route

    def __str__(self):
        result = "Truck Info:\nDriver ID: {}\n".format(self.driver)
        result += "Leave Time: {}\n".format(self.truck_leave_time)
        result += "Packages:\n"
        for package in self.packages_loaded:
            result += f'{package}\n'
        return result

    def add_package(self, package):
        # if the number of packages loaded is less than the capacity, load the package to the truck
        if self.package_capacity > len(self.packages_loaded):
            self.packages_loaded.append(package)
            package.status = "en route"
        else:
            print('Truck is at maximum capacity')