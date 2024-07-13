def count_up(5, 7, 1):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # YOUR CODE HERE
def count_up(start stop):
    while start <= stop:
        print(start)
        start = start + 1

count_up(5, 7)        
