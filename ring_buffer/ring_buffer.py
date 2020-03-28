from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        elif len(self.storage) == self.capacity:
            if self.current.next == None:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head
            else:
                self.current.next.delete()
                self.current.insert_after(item)
                self.current = self.current.next

        #     # if there is a next
        #     if self.current.next:
            
        #     # We're at the end of the list
        #     else:
        #     self.storage.remove_from_head()
        #     # self.current = 0
        # # THEN add to tail, keep current/pointer on new tail
        # self.storage.add_to_tail(item)

        # # If out of capacity chop off the head
        # # self.current = len(self.storage) - 1
        # # if self.current == None:
        # #     self.current = -1
        # # self.current += 1
        # # if self.current == self.capacity:
        # #     self.current == 0

        # elif len(self.storage) < self.capacity:
        #     self.storage.add_to_tail(item) 
        #     self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = [i for i in self.storage.make_list()]

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
