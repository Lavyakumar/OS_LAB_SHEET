# -------------------------------------------------------------
# TITLE: System Startup, Process Creation, and Termination Simulation
# COURSE CODE: ENCS351 - Operating System
# PROGRAM: B.Tech CSE 
# AUTHOR: Lavya Kumar
# -------------------------------------------------------------

import multiprocessing
import time
import logging

# -------------------- Sub-Task 1: Logging Configuration --------------------
logging.basicConfig(
    filename='process_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(processName)s - %(message)s'
)

# -------------------- Sub-Task 2: Dummy Process Function --------------------
def system_process(task_name):
    """Simulates a basic system process with start and end logs."""
    logging.info(f"{task_name} started")
    time.sleep(2)  # Simulate system process execution delay
    logging.info(f"{task_name} ended")

# -------------------- Sub-Task 3 & 4: Process Creation and Termination --------------------
if __name__ == '__main__':
    print("System Starting...")
    logging.info("System Booting...")

    # Create multiple processes
    p1 = multiprocessing.Process(target=system_process, args=('Process-1',))
    p2 = multiprocessing.Process(target=system_process, args=('Process-2',))

    # Start processes concurrently
    p1.start()
    p2.start()

    # Wait for both processes to complete
    p1.join()
    p2.join()

    logging.info("All processes completed successfully.")
    print("System Shutdown.")
