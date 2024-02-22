# C950 Data Structures and Algorithms II Project - Student ID: 010803145

from datetime import timedelta
from ModulesPackage.CsvParser import *
from ModulesPackage.PackageDelivery import truck_deliver_packages
from ModulesPackage.Truck import Truck


# creates and fills the package hash table
all_packages = create_package_hash()

# initialize trucks
truck1 = Truck(timedelta(hours=8, minutes=0), 10)
truck2 = Truck(timedelta(hours=9, minutes=5), 2)
# TODO: change truck 3 to leave after truck 1 or 2 returns and it's 10:20 (for the delayed delivery)
truck3 = Truck(timedelta(hours=10, minutes=20),  "TBD")

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

# delivery of packages is initiated
truck_deliver_packages(truck1)
truck_deliver_packages(truck2)
truck_deliver_packages(truck3)

print(truck1.miles)
print(truck1.time)

print(truck2.miles)
print(truck2.time)

print(truck3.miles)
print(truck3.time)
