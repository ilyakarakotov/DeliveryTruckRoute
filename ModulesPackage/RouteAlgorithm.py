# this function finds the nearest address to the current address
from datetime import timedelta
from Address import *
from ModulesPackage.CsvParser import create_distance_matrix


# This function finds the nearest address to the current address
def min_distance_from(curr_delivery, truck):

    # Create address lookup and distance matrix
    nearest_address = None
    distance_matrix = create_distance_matrix()
    address_hash = address_lookup_hash()

    curr_address_key = address_lookup(curr_delivery)

    # Initialize nearest distance to infinity distance away, so the first address will always be closer
    nearest_distance = float('inf')

    # Iterates through each package in the truck to find the nearest address
    for package in truck.packages_loaded:
        address = package.delivery_addy
        address_key = address_lookup(address)

        # If the distance from the current address to the address of the package is less than the nearest distance,
        # the current address becomes the nearest address
        if float(distance_matrix[curr_address_key][address_key]) < float(nearest_distance):
            nearest_distance = distance_matrix[curr_address_key][address_key]
            nearest_address = address_hash[address_key]

    # Adds the nearest distance to the truck's total miles
    truck.miles += float(nearest_distance)

    # Adds time to truck based on miles traveled
    truck.time += timedelta(minutes=(float(nearest_distance) / 18) * 60)

    return nearest_address, truck
