# C950 Data Structures and Algorithms II Project - Student ID: 010803145

from datetime import timedelta
from ModulesPackage.CsvParser import *
from ModulesPackage.PackageDelivery import truck_deliver_packages
from ModulesPackage.Truck import Truck

# program interface
print("\n*********************************************")
print("Data Structures and Algorithms - C950")
print("Welcome to the WGUPS Package Delivery System.")
print("*********************************************\n")

exit_check = input("Press Enter to Begin Package Delivery\nType 'exit' to Exit Program:\n")

# If user does not type 'exit', the program will run
if exit_check != "exit":

    # creates and fills the package hash table
    all_packages = create_package_hash()

    # initialize trucks with the time they leave the hub
    truck1 = Truck(timedelta(hours=8, minutes=0), 1)
    truck2 = Truck(timedelta(hours=9, minutes=5), 2)
    truck3 = Truck(timedelta(hours=10, minutes=20), 1)

    # add packages to trucks
    truck1.add_package(all_packages.lookup(1))
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
    truck1.add_package(all_packages.lookup(34))

    truck2.add_package(all_packages.lookup(3))
    truck2.add_package(all_packages.lookup(4))
    truck2.add_package(all_packages.lookup(5))
    truck2.add_package(all_packages.lookup(6))
    truck2.add_package(all_packages.lookup(12))
    truck2.add_package(all_packages.lookup(18))
    truck2.add_package(all_packages.lookup(23))
    truck2.add_package(all_packages.lookup(24))
    truck2.add_package(all_packages.lookup(36))
    truck2.add_package(all_packages.lookup(37))
    truck2.add_package(all_packages.lookup(38))
    truck2.add_package(all_packages.lookup(40))

    truck3.add_package(all_packages.lookup(2))
    truck3.add_package(all_packages.lookup(7))
    truck3.add_package(all_packages.lookup(8))
    truck3.add_package(all_packages.lookup(9))
    truck3.add_package(all_packages.lookup(10))
    truck3.add_package(all_packages.lookup(11))
    truck2.add_package(all_packages.lookup(17))
    truck3.add_package(all_packages.lookup(22))
    truck3.add_package(all_packages.lookup(25))
    truck3.add_package(all_packages.lookup(26))
    truck3.add_package(all_packages.lookup(27))
    truck3.add_package(all_packages.lookup(28))
    truck3.add_package(all_packages.lookup(32))
    truck3.add_package(all_packages.lookup(33))
    truck3.add_package(all_packages.lookup(35))
    truck3.add_package(all_packages.lookup(39))

    # Delivery of packages is initiated
    print("Truck 1 Deliveries:")
    truck_deliver_packages(truck1)

    print("Truck 2 Deliveries:")
    truck_deliver_packages(truck2)

    # Truck 3 leaves after truck 1 or 2 returns, at 10:20am.
    # Package 9 address is also updated in time for the 10:20 departure
    all_packages.lookup(9).delivery_addy = "410 S State St"

    print("Truck 3 Deliveries:")
    truck_deliver_packages(truck3)

    # Total miles driven by all trucks is calculated and printed
    total_miles = truck1.miles + truck2.miles + truck3.miles

    print("****************************************")
    print("All packages are now delivered!")
    print("Total Miles By All Trucks: " + str(round(total_miles, 2)) + " Miles")
    print("****************************************\n")

    # User can look up package(s) status until they way to exit the program
    activity = input("For a list of all deliveries, type 'all'\n"
                     "To look up a package, type the package ID.\n"
                     "If you want to exit the program, type 'exit'.\n")

    while activity != "exit":
        # If user enters all, the status of all the packages is printed
        if activity == "all":
            input_time = input("\nCheck status of all packages at time (HH:MM:SS): ")

            # Input time is converted to a timedelta object
            (h, m, s) = input_time.split(":")
            current_time = timedelta(hours=int(h), minutes=int(m), seconds=int(s))

            # Table headers are printed
            print(f"{'ID': <5}" \
                  f"{'Address': <30}" \
                  f"{'Deadline': <10}" \
                  f"{'City': <20}" \
                  f"{'Zip': <10}" \
                  f"{'Weight': <10}" \
                  f"{'Status': <20}" \
                  f"{'Departure': <20}" \
                  f"{'Delivery': <20}" \
                  f"\t{'Notes': <20}")
            # All package status' are found through the set_status_at_time method
            for i in range(1, 41):
                # Package status is updated at the input time
                package = all_packages.lookup(i)
                package.set_status_at_time(current_time)

                # Package information is printed
                print(package)

            activity = input("\nFor a list of all deliveries, type 'all'\n"
                             "To look up a package, type the package ID. \n"
                             "If you want to exit the program, type 'exit'.\n")
        # If user enters a package ID, the status of that package is printed
        elif 1 <= int(activity) <= 40:
            input_time = input("\nCheck package status at time (HH:MM:SS): ")

            # Input time is converted to a timedelta object
            (h, m, s) = input_time.split(":")
            current_time = timedelta(hours=int(h), minutes=int(m), seconds=int(s))

            # Table headers are printed
            print(f'{"ID": <5}' \
                  f'{"Address": <30}' \
                  f'{"Deadline": <10}' \
                  f'{"City": <20}' \
                  f'{"Zip": <10}' \
                  f'{"Weight": <10}' \
                  f'{"Status": <20}' \
                  f'{"Departure": <20}' \
                  f'{"Delivery": <20}' \
                  f'\t{"Notes": <20}')

            # Package status is updated at the input time with the set_status_at_time method
            package = all_packages.lookup(int(activity))
            package.set_status_at_time(current_time)

            # Package information is printed
            print(package)

            activity = input("\nFor a list of all deliveries, type 'all'\n"
                             "To look up a package, type the package ID. \n"
                             "If you want to exit the program, type 'exit'.\n")
        # If user enters an invalid input, they are prompted to enter a valid input
        else:
            print("Invalid input. Please type 'all' or a package ID.")

print("\nThank you for using the WGUPS Package Delivery System. Goodbye!")
