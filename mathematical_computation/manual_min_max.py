import operator

class ListHelper():
    def __init__(self, nums):
        self.nums = nums

    def min(self):
        return self._min_max(min = True)

    def max(self):
        return self._min_max(max = True)

    def _min_max(self, min = None, max = None):
        ops = {
            '<': operator.lt,
            '<=': operator.le,
            '==': operator.eq,
            '!=': operator.ne,
            '>=': operator.ge,
            '>': operator.gt
        }

        final_num = self.nums[0]

        selected_operator = '<' if min == True else '>'

        operation = ops.get(selected_operator)

        for num in self.nums:
            if operation(num, final_num):
                final_num = num

        return final_num


list_of_nums = [12, 1, 33, 100]
list_helper = ListHelper(list_of_nums)
print(list_helper.min())
print(list_helper.max())
