class ListHelper:

    def __init__(self, collection):
        self.collection = collection
        self.at_end = True

    def toggle_popper(self):
        self.at_end = not self.at_end

        try:
            if self.at_end:
                return self.collection.pop()
            else:
                return self.collection.pop(0)
        except:
            return None


num_list = [1, 2, 3, 4, 5]
lh = ListHelper(num_list)

print(lh.toggle_popper())
print(lh.toggle_popper())
print(lh.toggle_popper())
print(lh.toggle_popper())
print(lh.toggle_popper())
print(lh.toggle_popper())
