from datetime import timedelta

from Address import address_lookup_hash, address_lookup
from ModulesPackage.CsvParser import create_distance_matrix
from ModulesPackage.RouteAlgorithm import min_distance_from


# this function delivers the packages in the truck
def truck_deliver_packages(truck):
    # create address lookup and distance matrix
    addresses = address_lookup_hash()
    distance_matrix = create_distance_matrix()

    hub_address = addresses[0]
    curr_address = hub_address

    # iterates through truck addresses using NN until truck load is emptied out
    while len(truck.packages_loaded) != 0:

        # nearest address is found
        nearest_address, truck = min_distance_from(curr_address, truck)

        # nearest address becomes the current address truck is at
        curr_address = nearest_address

        for i in range(len(truck.packages_loaded)):
            if truck.packages_loaded[i].delivery_addy == curr_address:

                print("Package delivered at " + curr_address + " - Total Miles Driven: " + str(truck.miles))
                truck.packages_loaded[i].status = "delivered"
                if truck.time > truck.packages_loaded[i].deadline:
                    print("Delivery Deadline: " + str(truck.packages_loaded[i].deadline) + "\nDelivered At: " + str(
                        truck.time))
                    print("Delivery was late!")
                    print()
                else:
                    print("Delivery Deadline: " + str(truck.packages_loaded[i].deadline) + "\nDelivered At: " + str(
                        truck.time))
                    print("Delivery was made on time!")
                    print()
                truck.packages_loaded.remove(truck.packages_loaded[i])
                # print(truck.packages_loaded)
                break
    # return truck to hub
    truck.miles += float(distance_matrix[address_lookup(curr_address)][0])
    truck.time += timedelta(minutes=(float(distance_matrix[address_lookup(curr_address)][0]) / 18) * 60)
    print("Truck has returned to the hub - Total Miles Driven: " + str(truck.miles) + " - Time: " + str(truck.time))
