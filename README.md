🧠 Operating Systems Lab Sheets (ENCS351)
This repository contains all Operating Systems Laboratory Assignments (Lab Sheets) for the B.Tech CSE course 
Each lab sheet demonstrates core OS concepts through Python simulations involving process management, multiprocessing, and system behavior logging.

📁 Folder Structure
LAB_SHEETS/
│
├── Lab_Sheet_1/
│   ├── process_management.py
│   ├── output.txt
│   ├── report.pdf
│   └── README.md
│
├── Lab_Sheet_2/
│   ├── system_startup_simulation.py
│   ├── process_log.txt
│   ├── report.pdf
│   └── README.md
│
└── README.md  ← (this main file)

🧩 Lab Sheet Details

🧪 Lab Sheet 1: Process Creation and Management Using Python OS Module
Objectives:
Understand Linux process lifecycle.
Create child processes using os.fork().
Execute system commands via os.execvp() or subprocess.run().
Simulate Zombie and Orphan processes.
Inspect process info from /proc and manipulate nice values.
Files:
process_management.py → main Python script
output.txt → sample program output
report.pdf → explanation with code snippets and results

⚙️ Lab Sheet 2: System Startup, Process Creation, and Termination Simulation
Objectives:
Simulate system startup and shutdown using Python.
Use the multiprocessing module to create concurrent processes.
Implement logging to record start and end of each process.
Generate process_log.txt showing lifecycle tracking.
Files:
system_startup_simulation.py → main simulation code
process_log.txt → generated log output
report.pdf → experiment report

🚀 How to Run

Prerequisites
Ensure Python 3.x is installed.
You can verify with:
python --version
Run Lab Sheet 1
cd Lab_Sheet_1
python process_management.py
Run Lab Sheet 2
cd Lab_Sheet_2
python system_startup_simulation.py
After execution, check:
output.txt for Lab 1 results
process_log.txt for Lab 2 logs

🧑‍💻 Author
Name: Lavya Kumar
Course: B.Tech Computer Science & Engineering
University: K.R Mangalam University 
