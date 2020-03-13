#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable, hash_table_insert, hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    # make a hashTable of length equivalent to the length of the weights array
    ht = HashTable(len(weights) or length)

    """
    YOUR CODE HERE
    """
    # insert each of the weights in the hashtable using their indices as values
    for index, weight in enumerate(weights):
        hash_table_insert(ht, weight, index)
        
    # initialize variables to hold our matching indices    
    match_pair_index = None
    weight_index = None
    
    # loop through the weights and find the matching pair index, if exists
    for weight in weights:
        # determine the matching digit
        match = limit - weight
        # retrieve match: should return None if not existing yet
        match_pair_index = hash_table_retrieve(ht, match)
        # if match is a weight in the hashtable
        if match_pair_index is not None:
            # retrieve the index of the weight from hashtable
            weight_index = hash_table_retrieve(ht, weight)

            # format responses, with highest value in first index
            if match == weight:
                return (1, 0)
            elif match_pair_index > weight_index:
                return (match_pair_index, weight_index)
            elif match_pair_index < weight_index:
                return (weight_index, match_pair_index)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
