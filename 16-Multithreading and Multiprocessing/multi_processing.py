## Processes that run in Parallel
### CPU-Bound Tasks-Tasks that are heavy on CPU usage (e.g., mathematical computation,data Prosessing)
## Parallel execution - multiple cores of the CPU

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square of {i} is {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube of {i} is {i*i*i}")

if __name__ == "__main__":
    
    ## create 2 processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)
    t = time.time()

    ## start the processes
    p1.start()
    p2.start()

    ## wait for the processes to finish
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(f"Finished in {finished_time:.2f} seconds")