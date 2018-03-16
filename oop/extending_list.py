class ListExtension(list):
    def sum(self):
        return sum(e for e in self)


num_list = [1, 2, 3]
le = ListExtension(num_list)
le.sum()
