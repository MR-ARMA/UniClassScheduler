UniClassScheduler

UniClassScheduler is a Python-based desktop application designed to automate university class scheduling. With a user-friendly Tkinter GUI, it enables administrators to manage professors, courses, and classrooms, generate conflict-free schedules, and ensure specific courses do not overlap in time or place. The project includes a comprehensive sample dataset with intentional overlaps to test scheduling robustness, making it ideal for universities seeking efficient timetable solutions.

Features

Data Management: Add and manage professors, courses, and classrooms with detailed attributes (e.g., availability, course conflicts, classroom features).
Schedule Generation: Automatically create schedules respecting professor availability, course conflicts, and classroom constraints.
Non-Overlapping Courses: Specify two courses (e.g., CS101 and MATH101) to ensure they are scheduled at different times and rooms.
Sample Data: Includes 20 professors, 40 courses, and 15 classrooms with overlaps for realistic testing.
Save/Load Data: Persist schedules and settings to JSON for reuse.
Intuitive GUI: Easy-to-use interface for inputting data, planning courses, and viewing schedules in a table.

Requirements

Python: Version 3.8 or higher (tested with Python 3.12).
Libraries: Tkinter (included with standard Python).
Operating System: Windows, macOS, or Linux.

Installation

Clone the Repository:
git clone https://github.com/<your-username>/UniClassScheduler.git
cd UniClassScheduler


Verify Python Installation:Ensure Python 3.8+ is installed:
python --version

If not installed, download from python.org.

Check Project Structure:Confirm the following structure:
UniClassScheduler/
├── main.py
├── models/
│   ├── __init__.py
│   ├── professor.py
│   ├── course.py
│   ├── classroom.py
│   └── schedule.py
├── utils/
│   ├── __init__.py
│   └── scheduler_engine.py
├── gui/
│   ├── __init__.py
│   ├── app.py
│   ├── input_frames.py
│   └── schedule_view.py
├── data/
│   ├── __init__.py
│   └── sample_data.py
├── screenshots/
│   └── main_interface.png
├── LICENSE
└── README.md


No Additional Dependencies:The project uses only the Python standard library (Tkinter), so no pip install is needed.


Usage
UniClassScheduler offers a straightforward GUI for managing and scheduling university classes. Follow these steps to use it effectively:
1. Run the Application

Navigate to the project directory:cd UniClassScheduler


Launch the application:python main.py

On Windows, use the full Python path if needed:C:\Users\YourName\AppData\Local\Programs\Python\Python312\python.exe main.py


The main window opens, displaying buttons for data management and scheduling.

2. Load Sample Data

Purpose: Test the scheduler with a large dataset (20 professors, 40 courses, 15 classrooms) featuring intentional overlaps.
Steps:
Click Load Sample Data in the main window.
A message confirms: "Success: Sample data loaded successfully."
The dataset includes conflicting courses (e.g., CS101 vs. MATH101) for testing the non-overlap feature.


Note: If you see "Failed to load sample data: No module named 'data.sample_data'", ensure data/__init__.py exists. See Troubleshooting.

3. Add Custom Data (Optional)

Purpose: Input custom professors, courses, or classrooms.
Steps:
Click Add Professor to enter name, availability (e.g., Monday 09:00–12:00), and courses.
Click Add Course to specify name, code, duration, professors, and conflicts.
Click Add Classroom to define name, capacity, availability, and features (e.g., projector).
Additions are logged and reflected in scheduling.



4. Plan Courses to Avoid Overlaps

Purpose: Ensure two courses (e.g., CS101 and MATH101) are scheduled at different times and rooms.
Steps:
Click Plan Courses to open a new window.
Select two courses from dropdowns (e.g., "CS101" and "MATH101").
Click Set Non-Overlapping Constraint to enforce non-overlap. A confirmation appears.
Alternatively, click Check Current Schedule (after generating a schedule) to verify non-overlap.


Example: CS101 (Monday 09:00–10:30, Room 101) and MATH101 (Tuesday 10:00–11:30, Room 102) are scheduled without overlap.
Note: The sample data’s CS101 and MATH101 conflict, making them ideal for testing.


5. Generate a Schedule

Purpose: Create a conflict-free schedule respecting constraints.
Steps:
Click Generate Schedule.
The scheduler processes data, prioritizing non-overlap constraints (e.g., CS101 and MATH101).
A message indicates success or lists unscheduled courses (expected with large data).
If non-overlap is set, a message confirms compliance (e.g., "CS101 and MATH101 do not overlap").


Note: The sample data’s 40 courses may leave some unscheduled due to overlaps.

6. View the Schedule

Purpose: Inspect the schedule in a table.
Steps:
Click View Schedule to open a new window.
View columns: Day, Time, Course, Professor, Classroom.
Verify non-overlapping courses (e.g., CS101 and MATH101).


Example Output:Day       Time          Course   Professor          Classroom
Monday    09:00-10:30   CS101    Dr. Alice Smith    Room 101
Tuesday   10:00-11:30   MATH101  Dr. Bob Johnson    Room 102
Wednesday 09:00-11:00   CS201    Dr. Alice Smith    Lab 201
...




7. Save Data

Purpose: Save data and schedules to JSON.
Steps:
Click Save Data.
A scheduler_data.json file is created in the project directory.
Data loads automatically on restart.


Note: Save before closing to preserve custom data.

8. Close the Application

Steps:
Close the main window.
Choose to save data when prompted.


Note: Saved data ensures continuity.

Troubleshooting

Error: "Failed to load sample data: No module named 'data.sample_data'":

Cause: data directory is not a Python package.
Fix:
Ensure data/__init__.py exists.
Verify sample_data.py is in data/.
Clear cache:rmdir /s /q data/__pycache__


Test import:python -c "from data.sample_data import sample_professors; print('Success')"


Set PYTHONPATH if needed:export PYTHONPATH=$PYTHONPATH:/path/to/UniClassScheduler






Unscheduled Courses:

Cause: Large dataset (40 courses, 15 classrooms) with overlaps.
Fix: Expected for testing. Increase max_iterations in utils/scheduler_engine.py:def generate_schedule(self, non_overlap_courses: Optional[Tuple[str, str]] = None, max_iterations: int = 5000) -> Schedule:




Non-Overlap Failure:

Cause: Tight constraints in sample data.
Fix: Check console logs for warnings. Try different course pairs or increase max_iterations.



Project Structure
UniClassScheduler/
├── main.py                 # Application entry point
├── models/                 # Data models
│   ├── __init__.py
│   ├── professor.py
│   ├── course.py
│   ├── classroom.py
│   └── schedule.py
├── utils/                  # Scheduling logic
│   ├── __init__.py
│   └── scheduler_engine.py
├── gui/                    # GUI components
│   ├── __init__.py
│   ├── app.py
│   ├── input_frames.py
│   └── schedule_view.py
├── data/                   # Sample data
│   ├── __init__.py
│   └── sample_data.py
├── screenshots/            # Screenshots for README
│   ├── main_interface.png
│   ├── plan_courses.png
│   └── schedule_view.png
├── LICENSE
└── README.md

