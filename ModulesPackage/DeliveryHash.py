class DeliveryHash:
    def __init__(self, initial_capacity=10, load_factor=.7):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def __str__(self):
        # iterates through each bucket, and each package in each bucket, and outputs the package information
        result = ""
        for bucket_list in self.table:
            for package in bucket_list:
                result += f'{package}\n'
        return result

    def __repr__(self):
        # iterates through each bucket, and each id in each bucket, and outputs the package information
        result = ""
        for bucket_list in self.table:
            for package in bucket_list:
                result += f'{package}\n'
        return result

    def add_order(self, package):
        # find the bucket to place order in
        bucket = package.package_id % 10
        bucket_list = self.table[bucket]

        # input order id and order into bucket list
        key_value = [package.package_id, package]
        bucket_list.append(key_value)
        return True

    def lookup(self, package_id):
        bucket = package_id % 10
        bucket_list = self.table[bucket]

        # iterates through bucket, and if pkg id is in it, return the package at the id.
        for pkg_id in bucket_list:
            if pkg_id[0] == package_id:
                return pkg_id[1]
        return None
