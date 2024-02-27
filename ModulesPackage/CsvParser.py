import csv

from ModulesPackage.DeliveryHash import DeliveryHash
from ModulesPackage.Package import Package


# This function creates a hash table of all the packages
def create_package_hash():
    with open('CSV/package_CSV.csv', 'r') as csvfile:
        packages_hash = DeliveryHash()
        reader = csv.reader(csvfile)
        # Iterates through each order to deliver
        for row in reader:
            # Add content of each delivery to a package
            package_id, delivery_addy, city, _, zip_code, deadline, weight, *notes = row
            package = Package(int(package_id), delivery_addy, city, int(zip_code), deadline, int(weight), "at the hub",
                              notes)

            # Add each package to hash table
            packages_hash.add_order(package)

        return packages_hash


# This function reads the distance csv file to the distance matrix
def create_distance_matrix():
    with open('CSV/distance_CSV.csv', 'r') as csvfile:
        csv_data = []
        reader = csv.reader(csvfile)

        # Reads every row to the csv_data array
        for row in reader:
            csv_data.append(row)

        # Number of addresses is equal to the amount of rows, so an element is made to represent that number
        num_addresses = len(csv_data)

        # Empty distance matrix is created with slots and spaces in each slot equal to num_addresses
        distance_matrix = [[None] * num_addresses for _ in range(num_addresses)]

        # Read the csv_data of each element to distance matrix
        for i in range(len(csv_data)):
            for j in range(len(csv_data)):
                if csv_data[i][j] != '':
                    distance_matrix[i][j] = csv_data[i][j]
                # If csv_data is empty at [i][j], [j][i] is added to matrix to avoid empty slots
                else:
                    distance_matrix[i][j] = csv_data[j][i]

        return distance_matrix
