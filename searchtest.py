'''
searchtest.py
Linda Mannila 2010
Demonstrates linear and binary search and outputs a comparison of their
execution times.
NOTE! The execution time of linear search differs depending on whether
it is implemented with for or while.
'''

import search

def test_search_algorithms():
    ''' Times the execution of the three search functions '''
    
    import time
    the_list = range(1000000)

    # --- Run and time linear search implemented with a for loop --- #
    t1 = time.clock()
    index = search.linear_search_for(the_list, 750000)
    t2 = time.clock()
    
    # Convert from seconds to milliseconds
    exec_time = (t2-t1)*1000
    print "Linear search: %.4f ms (with for loop)" % exec_time
    print "Element found in index %d" % index

    # --- Run and time linear search implemented with a while loop --- #
    t1 = time.clock()
    index = search.linear_search_while(the_list, 750000)
    t2 = time.clock()
    
    # Convert from seconds to milliseconds
    exec_time = (t2-t1)*1000
    print "\nLinear search: %.4f ms (with while loop)" % exec_time
    print "Element found in index %d" % index

    # --- Run and time binary search --- #
    t1 = time.clock()
    index = search.binary_search(the_list, 750000)
    t2 = time.clock()
    
    # Convert from seconds to milliseconds
    exec_time = (t2-t1)*1000
    print "\nBinary search: %.4f ms" % exec_time
    print "Element found in index %d" % index

def main():
    test_search_algorithms()
