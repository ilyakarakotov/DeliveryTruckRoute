class DeliveryHash:
    # creates an empty hash table with a bucket capacity of 10
    def __init__(self, capacity=10):
        self.table = []
        for i in range(capacity):
            self.table.append([])

    def __str__(self):
        # Iterates through each bucket, and each package in each bucket, and outputs the package information
        result = ""
        for bucket_list in self.table:
            for package in bucket_list:
                result += f'{package}\n'
        return result

    def __repr__(self):
        # Iterates through each bucket, and each id in each bucket, and outputs the package information
        result = ""
        for bucket_list in self.table:
            for package in bucket_list:
                result += f'{package}\n'
        return result

    def add_order(self, package):
        # Find the bucket to place order in
        bucket = package.package_id % 10
        bucket_list = self.table[bucket]

        # Input order id and order into bucket list
        key_value = [package.package_id, package]
        bucket_list.append(key_value)
        return True

    # Looks up a package in the hash table
    def lookup(self, package_id):
        bucket = package_id % 10
        bucket_list = self.table[bucket]

        # Iterates through bucket, and if pkg id is in it, return the package at the id.
        for pkg_id in bucket_list:
            if pkg_id[0] == package_id:
                return pkg_id[1]
        return None
