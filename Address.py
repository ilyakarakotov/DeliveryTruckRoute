# This function creates a hash table of all the addresses
def address_lookup_hash():
    address_hash = {}
    address_hash[0] = "4001 South 700 East"
    address_hash[1] = "1060 Dalton Ave S"
    address_hash[2] = "1330 2100 S"
    address_hash[3] = "1488 4800 S"
    address_hash[4] = "177 W Price Ave"
    address_hash[5] = "195 W Oakland Ave"
    address_hash[6] = "2010 W 500 S"
    address_hash[7] = "2300 Parkway Blvd"
    address_hash[8] = "233 Canyon Rd"
    address_hash[9] = "2530 S 500 E"
    address_hash[10] = "2600 Taylorsville Blvd"
    address_hash[11] = "2835 Main St"
    address_hash[12] = "300 State St"
    address_hash[13] = "3060 Lester St"
    address_hash[14] = "3148 S 1100 W"
    address_hash[15] = "3365 S 900 W"
    address_hash[16] = "3575 W Valley Central Station bus Loop"
    address_hash[17] = "3595 Main St"
    address_hash[18] = "380 W 2880 S"
    address_hash[19] = "410 S State St"
    address_hash[20] = "4300 S 1300 E"
    address_hash[21] = "4580 S 2300 E"
    address_hash[22] = "5025 State St"
    address_hash[23] = "5100 South 2700 West"
    address_hash[24] = "5383 South 900 East #104"
    address_hash[25] = "600 E 900 South"
    address_hash[26] = "6351 South 900 East"

    return address_hash

addresses = address_lookup_hash()

# This function looks up the address key in the address hash table
def address_lookup(address_to_find):
    for key, value in addresses.items():
        if value == address_to_find:
            return key

    return "Address not found in the hash"
