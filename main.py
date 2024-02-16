# C950 Data Structures and Algorithms II Project - Student ID: 010803145

import csv
from datetime import time

from Address import addressLookupHash
from ModulesPackage.DeliveryHash import DeliveryHash
from ModulesPackage.Package import Package
from ModulesPackage.Truck import Truck


# this function creates a hash table of all the packages
def createPackageHash():
    with open('CSV/package_CSV.csv', 'r') as csvfile:
        packages_hash = DeliveryHash()
        reader = csv.reader(csvfile)
        # iterates through each order to deliver
        for row in reader:
            # add content of each delivery to a package
            package_id, delivery_addy, city, _, zip_code, deadline, weight, *notes = row
            package = Package(int(package_id), delivery_addy, city, int(zip_code), deadline, int(weight), "at the hub",
                              notes)

            # add each package to hash table
            packages_hash.add_order(package)

        return packages_hash


# this function reads the distance csv file to the distance matrix
def createDistanceMatrix():
    with open('CSV/distance_CSV.csv', 'r') as csvfile:
        csv_data = []
        reader = csv.reader(csvfile)

        # reads every row to the csv_data array
        for row in reader:
            csv_data.append(row)

        # number of addresses is equal to the amount of rows, so an element is made to represent that number
        num_addresses = len(csv_data)

        # empty distance matrix is created with slots and spaces in each slot equal to num_addresses
        distance_matrix = [[None] * num_addresses for _ in range(num_addresses)]

        # read the csv_data of each element to distance matrix
        for i in range(len(csv_data)):
            for j in range(len(csv_data)):
                if csv_data[i][j] != '':
                    distance_matrix[i][j] = csv_data[i][j]
                # if csv_data is empty at [i][j], [j][i] is added to matrix to avoid empty slots
                else:
                    distance_matrix[i][j] = csv_data[j][i]

        # for row in distance_matrix:
        #     print(row)

        return distance_matrix


def address_lookup(address_to_find):
    for key, value in addresses.items():
        if value == address_to_find:
            return key

    return "Address not found in the hash"


def minDistanceFrom(curr_delivery, packages_loaded, total_miles):
    curr_address_key = address_lookup(curr_delivery)

    # initialize nearest address to unrealistically high miles away
    nearest_distance = 100.0

    for package in packages_loaded:
        address = package.delivery_addy
        address_key = address_lookup(address)

        if float(distance_matrix[curr_address_key][address_key]) < float(nearest_distance):
            nearest_distance = distance_matrix[curr_address_key][address_key]
            nearest_address = addresses[address_key]

    total_miles += float(nearest_distance)

    return nearest_address, total_miles


def truckDeliverPackages(truck):
    total_miles = 0.0
    hub_address = addresses[0]
    curr_address = hub_address


    # iterates through truck addresses using NN until truck load is emptied out
    while len(truck.packages_loaded) != 0:

        # nearest address is found
        nearest_address, total_miles = minDistanceFrom(curr_address, truck.packages_loaded, total_miles)

        # nearest address becomes the current address truck is at
        curr_address = nearest_address

        for i in range(len(truck.packages_loaded)):
            if truck.packages_loaded[i].delivery_addy == curr_address:
                print("Package delivered at " + curr_address + " - Total Miles Driven: " + str(total_miles))
                truck.packages_loaded[i].status = "delivered"
                truck.packages_loaded.remove(truck.packages_loaded[i])
                #print(truck.packages_loaded)
                break


# creates and fills the package hash table
all_packages = createPackageHash()

# creates and fills the distance matrix for all addresses
distance_matrix = createDistanceMatrix()

# creates address lookup for all addresses
addresses = addressLookupHash()

start_time = time(9, 0)
# initialize trucks
truck1 = Truck(start_time, 16, 1, "To-be-completed")
truck2 = Truck(start_time, 16, 2, "To-be-completed")
truck3 = Truck("leaves after driver comes back at ", 16, "tbd", "To-be-completed")

truck1.add_package(all_packages.lookup(1))
truck1.add_package(all_packages.lookup(2))
truck1.add_package(all_packages.lookup(13))
truck1.add_package(all_packages.lookup(14))
truck1.add_package(all_packages.lookup(15))
truck1.add_package(all_packages.lookup(16))
truck1.add_package(all_packages.lookup(19))
truck1.add_package(all_packages.lookup(20))
truck1.add_package(all_packages.lookup(21))
truck1.add_package(all_packages.lookup(29))
truck1.add_package(all_packages.lookup(30))
truck1.add_package(all_packages.lookup(31))
truck1.add_package(all_packages.lookup(32))

truck2.add_package(all_packages.lookup(3))
truck2.add_package(all_packages.lookup(4))
truck2.add_package(all_packages.lookup(6))
truck2.add_package(all_packages.lookup(17))
truck2.add_package(all_packages.lookup(18))
truck2.add_package(all_packages.lookup(25))
truck2.add_package(all_packages.lookup(26))
truck2.add_package(all_packages.lookup(34))
truck2.add_package(all_packages.lookup(36))
truck2.add_package(all_packages.lookup(37))
truck2.add_package(all_packages.lookup(38))
truck2.add_package(all_packages.lookup(40))

truck3.add_package(all_packages.lookup(5))
truck3.add_package(all_packages.lookup(7))
truck3.add_package(all_packages.lookup(8))
truck3.add_package(all_packages.lookup(9))
truck3.add_package(all_packages.lookup(10))
truck3.add_package(all_packages.lookup(11))
truck3.add_package(all_packages.lookup(12))
truck3.add_package(all_packages.lookup(22))
truck3.add_package(all_packages.lookup(23))
truck3.add_package(all_packages.lookup(24))
truck3.add_package(all_packages.lookup(27))
truck3.add_package(all_packages.lookup(28))
truck3.add_package(all_packages.lookup(32))
truck3.add_package(all_packages.lookup(33))
truck3.add_package(all_packages.lookup(35))
truck3.add_package(all_packages.lookup(39))

# truck1_start_time = time(8,0)
# truck2_start_time = time(9,0)
# truck3_start_time = time(10,0)



# print(truck1)
# print(truck2)
# print(truck3)

truckDeliverPackages(truck1)
