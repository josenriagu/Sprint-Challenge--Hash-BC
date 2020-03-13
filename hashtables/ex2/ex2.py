#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable, hash_table_insert, hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    # reduce length of route by 1 so as to not include NONE
    route = [None] * (length - 1)

    """
    YOUR CODE HERE
    """
    # insert each of the tickets in the hashtable using their destinations as values
    for ticket in tickets:  # O(n)
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    # the ticket with source as "NONE" is our trip origin
    route[0] = hash_table_retrieve(hashtable, "NONE")

    # start the iteration from 1 till end of route
    for i in range(1, len(route)):  # O(n)
        # retrive the next destination using the previous destination as sourc;
        route[i] = hash_table_retrieve(hashtable, route[i - 1])

    # return route
    return route
