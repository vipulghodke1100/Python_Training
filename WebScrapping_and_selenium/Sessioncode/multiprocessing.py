import time
import multiprocessing

def print_cube(num):
  """
  Function to print cube of given num
  """
  print("Cube function")
  print("Cube: {}".format(num * num * num))

def print_square(num):
  """
  Function to print square of given num
  """
  print("Square function")
  print("Square: {}".format(num * num))

def func1():
    print("New process started..")
    time.sleep(2)
    print(f"The process name is : {multiprocessing.current_process()}")

def main_fn1():
    p1 = multiprocessing.Process(target=func1)
    # start the process
    p1.start()
    # wait for process to complete its task
    p1.join()
    print("Finished execution..")

def main_fn2():
    """
    In below code, p1 calculates sqaure and p2 calculates cube of a number
    After starting the thread, when we are using join on p1 and then on p2
    p2 will wait for p1 to complete its task i.e. calculating sqaure and 
    then p2 will calculate cube of a number. 
    
    These processes run independently in separate memory spaces.
    """
    
    # creating process
    p1 = multiprocessing.Process(target=print_square, args=(10,))
    p2 = multiprocessing.Process(target=print_cube, args=(10,))

    # starting process 1
    p1.start()
    # starting process 2
    p2.start()

    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()
    
    

    print("Execution Finished!") 

#Used to know whether the script is run directly or imported as module.
#If it is imported as module than print statements won't work inside main.
if __name__ == "__main__":
    """
    Before the child process completes, the main process continues to execute 
    and prints "Finished execution.." 
    because it has already completed its task of starting the child process
    """
    # main_fn1()
    
    
    main_fn2()
