from datetime import timedelta
from Address import address_lookup_hash, address_lookup
from ModulesPackage.CsvParser import create_distance_matrix
from ModulesPackage.RouteAlgorithm import min_distance_from


# This function delivers the packages in the truck
def truck_deliver_packages(truck):
    # Create address lookup and distance matrix
    addresses = address_lookup_hash()
    distance_matrix = create_distance_matrix()

    # Set the current address to the hub
    hub_address = addresses[0]
    curr_address = hub_address

    # Iterates through truck addresses using NN until all packages are delivered
    while len(truck.packages_loaded) != 0:

        # Nearest address is found through the min_distance_from function
        nearest_address, truck = min_distance_from(curr_address, truck)

        # Nearest address becomes the current address truck is at
        curr_address = nearest_address

        # Iterates through packages to find the package that matches the current address
        for i in range(len(truck.packages_loaded)):
            # If the package is at the current address, the info and total truck miles are printed, then package is
            # removed from the truck
            if truck.packages_loaded[i].delivery_addy == curr_address:

                truck.packages_loaded[i].delivery_time = truck.time

                print("Package delivered at " + curr_address + " - Total Miles Driven: " + str(round(truck.miles, 2)))

                truck.packages_loaded.remove(truck.packages_loaded[i])
                break

    # return truck to hub after all packages are delivered, and print total miles and time truck has driven
    truck.miles += float(distance_matrix[address_lookup(curr_address)][0])
    truck.time += timedelta(minutes=(float(distance_matrix[address_lookup(curr_address)][0]) / 18) * 60)
    print("Truck has returned to the hub - Miles Driven By Truck: " + str(truck.miles) + " - Time: " + str(truck.time))
    print()
