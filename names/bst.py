
class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value == None:
            self.value = value
        # if value to be inserted is >=
        if value >= self.value:
            # if something exist to the right --> recursion of insert...
            if self.right:
                # move right, recurse 'insert()'
                self.right.insert(value)
            # otherwise assign value at the empty spot to right
            else:
                self.right = BinarySearchTree(value)
        # else value must be smaller than compared to so move left...
        elif value < self.value:
            # same recursion as before but to the left
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # base-case: the thing we're looking for is in front of us
        if target == self.value:
            return True
        # if target is smaller than value, then move left & recurse (if something there)
        elif target < self.value and self.left:
            return self.left.contains(target)
        # look right if target is bigger and recurse (if something is there)
        elif target > self.value and self.right:
            return self.right.contains(target)
        else:
            return False
