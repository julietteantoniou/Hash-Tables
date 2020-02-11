# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        #hash the key- hash is independent of array size, is reduced to an index between 0 and self.capacity - 1 w modulo
        index = self._hash_mod(key)
        
        node = self.storage[index]
        
        if node is None:
            self.storage[index] = LinkedPair(key, value)
            return

        prev = node
        while node is not None:
            if key == node.key:
                node.value = value
                return
            prev = node
            node = node.next
            
        prev.next = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        prev = None

        # iterate through until node w correct key is found
        while node is not None and node.key is not key:
            prev = node
            node = node.next

        if node is None:
            print(f"Warning: node with key {key} not found")
            return
        else:

            if node.next is None and prev is None:
                self.storage[index] = None
            elif node.next is None and prev is not None:
                # has to be prev.next and not node bc node is a reference???
                prev.next = None
            elif prev is None:
                # node = node.next
                self.storage[index] = node.next
            else:
                prev.next = node.next
            # return deleted_node


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        
        node = self.storage[index]

        while node is not None:
            if key == node.key:
                return node.value

            node = node.next
            
        return None



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        original = self.storage

        self.capacity *= 2
        self.storage = [None] * self.capacity

        for node in original:
            # if node is not None and node.next is None:
            #     self.insert(node.key, node.value)
            # if node is not None and node.next is not None:
            #     # index = self._hash_mod(node.key)
            #     # self.storage[index] = node
            #     self.insert(node.key, node.value)

            while node is not None:
                self.insert(node.key, node.value)
                node = node.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
