# this function finds the nearest address to the current address
from datetime import timedelta

from Address import *
from ModulesPackage.CsvParser import create_distance_matrix

# #this function finds the nearest address to the current address
def min_distance_from(curr_delivery, truck):
    global nearest_address
    distance_matrix = create_distance_matrix()

    addresses = address_lookup_hash()

    curr_address_key = address_lookup(curr_delivery)

    # initialize nearest address to unrealistically high miles away
    nearest_distance = 100.0

    for package in truck.packages_loaded:
        address = package.delivery_addy
        address_key = address_lookup(address)

        if float(distance_matrix[curr_address_key][address_key]) < float(nearest_distance):
            nearest_distance = distance_matrix[curr_address_key][address_key]
            nearest_address = addresses[address_key]

    truck.miles += float(nearest_distance)

    # adds time to truck based on miles traveled
    truck.time += timedelta(minutes=(float(nearest_distance) / 18) * 60)



    return nearest_address, truck
