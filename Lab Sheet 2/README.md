# Lab Sheet 2 – System Startup, Process Creation, and Termination Simulation

## Course Information
**Course Code:** ENCS351  
**Course Name:** Operating System  
**Program:** B.Tech CSE 
**Author:** Lavya Kumar Beriwal

---

## 🧠 Objective
Simulate the startup, process creation, and shutdown sequence of an operating system using Python. The experiment demonstrates process lifecycle and logging mechanisms.

---

## 🧰 Tools Used
- Python 3.x  
- multiprocessing  
- logging  
- time  

---

## 🧪 How to Run

- 1. Open terminal and navigate to the folder:
   ```bash
   cd LAB_SHEET_2
- 2. Run the Python script:
    python3 system_startup_simulation.py
- 3. After execution, check the generated log file:
    cat process_log.txt
## Expected Output
    - Terminal:
      -   System Starting...
       -  System Shutdown.
       -  process_log.txt:
       -  2025-10-06 21:25:42,110 - MainProcess - System Booting...
       -  2025-10-06 21:25:42,111 - Process-1 - Process-1 started
       -  2025-10-06 21:25:42,112 - Process-2 - Process-2 started
       -  2025-10-06 21:25:44,115 - Process-1 - Process-1 ended
        - 2025-10-06 21:25:44,116 - Process-2 - Process-2 ended
### 🧩 Files Included

- system_startup_simulation.py---	Python code simulating OS startup and process lifecycle
- process_log.txt	              ---  Log file showing process start and end
- report.pdf	                   --- Report summarizing objectives, code, and output
- README.md                   ---	Execution guide
### 🏁 Learning Outcomes
- Learned process creation and concurrency using multiprocessing.
- Implemented logging with timestamps for process tracking.
- Simulated OS boot and shutdown behavior programmatically.

### ✍️ Author
- Name: Lavya Kumar
- Roll no.: 2301010012
- Institution: School of Engineering and Technology
- Course: ENCS351 – Operating Systems Lab
