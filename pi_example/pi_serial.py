
# import necessary libraries
import math
import numpy as np
import random
import time


def main():

    # start the clock
    starttime = time.time()
    
    # set number of random points to check
    npoints = int( 1e9 )
    
    # initialize counter for points in circle 
    count = 0
    
    for i in range( npoints ):
        
        # choose random location
        x = random.uniform( -1.0, 1.0 )
        y = random.uniform( -1.0, 1.0 )
        
        # check distance from origin to see if it is within the circle
        d = math.sqrt( x*x + y*y )
        if d < 1:
            count += 1
            
    # calculate the ratio of points that are in the circle to total points
    P = float( count ) / float( npoints )
    
    # estimate pi
    pi = 4.0 * P
    
    # get runtime
    runtime = ( time.time() - starttime )
    
    print( "pi (estimate) =  ", pi )
    print( "num points    =  ", npoints )
    print( "runtime [s]   =  ", str( round( runtime, 4) ) )
            

if __name__ == '__main__':
    import sys
    sys.exit( main() )
