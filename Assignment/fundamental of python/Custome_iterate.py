class MyIterator:
    def __init__(self, data):
        self.data = data  # Store the list
        self.index = 0    # Start index

    def __iter__(self):
        return self  # Iterator object returns itself

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration  # End iteration

# List of integers
numbers = [10, 20, 30, 40, 50]

# Creating iterator object
iter_obj = MyIterator(numbers)

# Iterating using the custom iterator
for num in iter_obj:
    print(num)
