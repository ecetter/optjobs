
# import necessary libraries
import math
import numpy as np
import random
import time

# import parallel libraries
import socket
import mpi4py
from mpi4py import MPI

# set up MPI communicator
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
    
# start the clock
starttime = time.time()


def main():
    # separate the root and worker processes
    if rank == 0:
        return mpi_root( comm )
    else:
        return mpi_worker( comm )
    return 0


def mpi_root( comm ):
    
    # set number of random points to check
    npoints = int( 1e9 )
    
    # initialize counter for points in circle 
    count = np.zeros( 1 )
    local_count = np.zeros( 1 )
    
    # set number of points for each worker
    numworkers = comm.Get_size() - 1
    chunk = math.floor( npoints / numworkers )
    lastchunk = npoints % numworkers
    
    # delegate work to workers
    local_n = np.zeros( 1 )
    for w in range( 1, numworkers + 1 ):
        if w < numworkers:
            local_n[0] = chunk
        elif w == numworkers:
            local_n[0] = chunk + lastchunk
        comm.Send( local_n, dest = w )

    # collect results
    comm.Reduce( local_count, count, op = MPI.SUM, root = 0 )
    
    # calculate the ratio of points that are in the circle to total points
    P = float( count[0] ) / float( npoints )
    
    # estimate pi
    pi = 4.0 * P

    # get runtime
    runtime = ( time.time() - starttime )
    
    print( "pi (estimate) =  ", pi )
    print( "num points    =  ", npoints )
    print( "runtime [s]   =  ", str( round( runtime, 4 ) ) )    

    return 0


def mpi_worker( comm ):

    local_n = np.zeros( 1 )
    count = np.zeros( 1 )
    local_count = np.zeros( 1 )
    
    comm.Recv( local_n, source = 0 )
    
    for i in range( int( local_n[0] ) ):
        
        # choose random location
        x = random.uniform( -1.0, 1.0 )
        y = random.uniform( -1.0, 1.0 )
        
        # check distance from origin to see if it is within the circle
        d = math.sqrt( x*x + y*y )
        if d < 1:
            local_count[0] += 1

    # communicate local_count to root process
    comm.Reduce( local_count, count, op = MPI.SUM, root = 0 )

    return 0

    
if __name__ == '__main__':
    import sys
    sys.exit( main() )
