###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
file_name = "ps1_cow_data.txt"

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    with open(filename, "r") as file:
        cow_dict = {}
        for line in file:
            cow_dict[line[:line.find(",")]] = int(line[line.find(",")+1:])
    return cow_dict
    
# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trip_list = []
    ordered_cows = sorted(cows, key=cows.get, reverse=True)
    while len(ordered_cows) >= 1:
        trip = [] ; limit = 10
        while len(ordered_cows) > 0 and limit >= cows[ordered_cows[-1]]:
            for cow in ordered_cows[:]:
                if cows[cow] <= limit:
                    trip.append(cow)
                    limit -= cows[cow]
                    ordered_cows.remove(cow)
            trip_list.append(trip)
    return trip_list


# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    """ 
        First version with fewer lines of code but it takes more time to run. 
    """
    best_trip = []
    ordered_cows = sorted(cows, key=cows.get, reverse=True)
    for partition in get_partitions(ordered_cows):
        max_weight = 0
        for trip in partition:
            sum1 = sum(cows[cow] for cow in trip)
            max_weight = max(sum1, max_weight)
        if max_weight <= limit and (len(best_trip) == 0 or len(best_trip) > len(partition)):
            best_trip = partition
    return best_trip
    """
        Second version with more lines of code but it takes less time to run.
    """
#    ordered_cows = sorted(cows, key=cows.get, reverse=True)
#    trip_list = [] ; len_list = []
#    partitions = get_partitions(ordered_cows)
#    for partition in partitions:
#        weight_list = []
#        for trip in partition:
#            weight = 0
#            for cow in trip:
#                weight += cows[cow]
#            weight_list.append(weight)
#        if max(weight_list) <= limit:
#            trip_list.append(partition)
#    for trip in trip_list:
#        len_list.append(len(trip))
#    return trip_list[len_list.index(min(len_list))]

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time()
    print(greedy_cow_transport(load_cows(file_name),limit=10))
    end = time.time()
    print(end-start)
    a = end - start

    start = time.time()
    print(brute_force_cow_transport(load_cows(file_name),limit=10))
    end = time.time()
    print(end-start)
    b = end - start

    print(b/a)

if __name__ == '__main__':
    #print(greedy_cow_transport(load_cows(file_name),limit=10))
    #brute_force_cow_transport(load_cows(file_name),limit=10)
    compare_cow_transport_algorithms()
    