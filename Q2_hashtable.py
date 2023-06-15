import random


class HashTable:
    def __init__(self, size):
        self.__size = size
        self.__chaining_table = [[] for _ in range(size)]  # creates an empty lists for chaining
        self.__open_addressing_table = [None] * size
        self.total_collision_chaining = 0  # variable assign to calculate the total collision
        self.total_collision_open_addressing = 0

    def __hash(self, key):
        return key % self.__size  # return the remainder of the value / size of hash table

    def insert_chaining(self, key):  # insert the hash key (remainder) using chaining
        index = self.__hash(key)
        self.__chaining_table[index].append(key)

    def insert_open_addressing(self, key):  # insert the hash key (remainder) using open addressing
        index = self.__hash(key)
        while self.__open_addressing_table[index] is not None:  # if collision occurs
            self.total_collision_open_addressing += 1  # calculate the total collision of open addressing
            index = (index + 1) % self.__size  # keep increasing the index by 1 to find the available slot to insert
        self.__open_addressing_table[index] = key  # insert the key into after found the available slot

    def calculate_total_collision_chaining(self):  # calculate the total collisions in chaining
        for n in self.__chaining_table:
            if len(n) > 1:  # if there has element(s) in the hash table
                self.total_collision_chaining += len(n) - 1  # increase the counter with the length of slot and
                # subtract 1 to exclude the first key that was inserted without collision
        return self.total_collision_chaining


def run_program():
    number_items = 5000
    table_size = 6001
    num_execute = 10  # Number of execute times

    chaining_min_collisions = float('inf')  # positive infinity value
    chaining_max_collisions = float('-inf')  # negative infinity value
    chaining_avg_collisions = 0  # to calculate the total average of chaining for 10 execution

    open_addressing_min_collisions = float('inf')
    open_addressing_max_collisions = float('-inf')
    open_addressing_avg_collisions = 0  # to calculate the total average of open addressing for 10 execution

    for _ in range(num_execute):
        items = [random.randint(0, 100000) for _ in range(number_items)]  # autogenerate 5000 random numbers

        chaining_table = HashTable(table_size)
        open_addressing_table = HashTable(table_size)

        for item in items:  # insert the numbers into hash table
            chaining_table.insert_chaining(item)
            open_addressing_table.insert_open_addressing(item)

        # calculate the total collision of every execution for collision and open addressing
        total_collision_chaining = chaining_table.calculate_total_collision_chaining()
        print(f"Total collision Chaining: {total_collision_chaining}")
        print(f"Total collision Open Addressing: {open_addressing_table.total_collision_open_addressing}\n")

        # Update minimum and maximum collisions for chaining
        # compares the current value of min or max with total_collision_chaining,
        # then selects the smaller of the two values and assigns it back
        chaining_min_collisions = min(chaining_min_collisions, total_collision_chaining)
        chaining_max_collisions = max(chaining_max_collisions, total_collision_chaining)

        # Update minimum and maximum collisions for open addressing
        open_addressing_min_collisions = min(open_addressing_min_collisions, open_addressing_table.total_collision_open_addressing)
        open_addressing_max_collisions = max(open_addressing_max_collisions, open_addressing_table.total_collision_open_addressing)

        # Add the total collisions to calculate the average after every execution
        chaining_avg_collisions += total_collision_chaining
        open_addressing_avg_collisions += open_addressing_table.total_collision_open_addressing

        # Clean up hash tables after every execution
        chaining_table.chaining_table = [[] for _ in range(table_size)]
        open_addressing_table.open_addressing_table = [None] * table_size

    # Calculate average collisions
    chaining_avg_collisions /= num_execute  # average = total average / 10
    open_addressing_avg_collisions /= num_execute

    # Print results in tabular format
    print("-------------------------------------------------------------------------------------")
    print("|\t\t\t\t\t\t\t\t\tAverage cost\t\t\t\t\t\t\t\t\t|")
    print("-------------------------------------------------------------------------------------")
    print("|\t\t\t\tChaining\t\t\t\t|\t\t\t\tOpen Addressing\t\t\t\t|")
    print("-------------------------------------------------------------------------------------")
    print("|\tMin\t\t|\tMax\t\t|\t  Avg\t\t|\t\tMin\t\t|\t Max\t  | \tAvg\t\t|")
    print("-------------------------------------------------------------------------------------")
    print(f"|\t{chaining_min_collisions}\t|\t{chaining_max_collisions}\t|\t{chaining_avg_collisions:.2f}\t\t|\t\t"
          f"{open_addressing_min_collisions}\t|\t{open_addressing_max_collisions}\t  |  {open_addressing_avg_collisions:.2f}\t|")
    print("-------------------------------------------------------------------------------------")


run_program()

"""References:
EntilZha (2015) Hash Table (Open Address) Implementation in Python Practicing for Interviews.
https://gist.github.com/EntilZha/5397c02dc6be389c85d8/revisions

Simranjenny84 (n.d.) Implementation of Hashing with Chaining in Python
https://www.geeksforgeeks.org/implementation-of-hashing-with-chaining-in-python/

stephengrice (2018) Hashtable. 
<https://github.com/pagekeytech/education/tree/master/HashTable>

Zaczyński, B. (n.d.) Build a Hash Table in Python With TDD 
<https://realpython.com/python-hash-table/>a
"""
