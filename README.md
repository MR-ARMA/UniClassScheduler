
# UniClassScheduler

**UniClassScheduler** is a Python-based desktop application that automates university class scheduling. Featuring an intuitive Tkinter GUI, it allows administrators to manage professors, courses, and classrooms, generate conflict-free timetables, and enforce custom constraints—such as ensuring specific courses do not overlap in time or space. The project includes a robust sample dataset with intentional conflicts to rigorously test scheduling performance.

---

## 🚀 Features

* **Data Management**: Add and manage professors, courses, and classrooms, including attributes like availability, conflicts, and room features.
* **Smart Scheduling**: Automatically generate optimized schedules that respect all constraints.
* **Custom Course Constraints**: Enforce non-overlapping rules between specific courses (e.g., CS101 and MATH101).
* **Realistic Sample Dataset**: Includes 20 professors, 40 courses, and 15 classrooms—with overlapping schedules for testing.
* **Persistence**: Save/load data and schedules in JSON format.
* **GUI Interface**: Clean and interactive Tkinter interface for data entry and schedule visualization.

---

## 🛠 Requirements

* **Python**: Version 3.8 or higher (tested with Python 3.12)
* **Libraries**: Only standard Python libraries; no external dependencies
* **OS**: Cross-platform (Windows, macOS, Linux)

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/UniClassScheduler.git
cd UniClassScheduler
```

### 2. Verify Python Installation

Ensure Python 3.8+ is installed:

```bash
python --version
```

If not, download it from [python.org](https://www.python.org).

### 3. Confirm Project Structure

Ensure the project structure looks like this:

```
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
├── README_fa.md
└── README.md
```

---

## 💻 Usage

### 1. Launch the Application

```bash
cd UniClassScheduler
python main.py
```

> On Windows, you may need the full path to Python:
> `C:\Users\YourName\AppData\Local\Programs\Python\Python312\python.exe main.py`

---

### 2. Load Sample Data

To test the scheduling engine with a realistic dataset:

* Click **"Load Sample Data"**
* You’ll see: *"Success: Sample data loaded successfully."*

> The sample includes intentional overlaps—perfect for testing custom constraints like non-overlapping CS101 and MATH101.

---

### 3. Add Custom Data *(Optional)*

* **Add Professor**: Enter name, availability (e.g., Mon 09:00–12:00), and courses.
* **Add Course**: Specify course code, duration, professors, and conflicts.
* **Add Classroom**: Define name, capacity, availability, and features (e.g., projector).

---

### 4. Plan Non-Overlapping Courses

* Click **"Plan Courses"**
* Choose two courses (e.g., CS101 and MATH101)
* Click **"Set Non-Overlapping Constraint"**

> You can also verify constraints after generating the schedule.

---

### 5. Generate Schedule

* Click **"Generate Schedule"**
* The algorithm processes constraints and generates a conflict-free timetable
* You’ll see a confirmation or a list of unscheduled courses

> If a non-overlap constraint was set, you'll see:
> *"CS101 and MATH101 do not overlap."*

---

### 6. View the Schedule

* Click **"View Schedule"**
* A table displays scheduled classes:

```
Day       Time          Course    Professor         Classroom
Monday    09:00–10:30   CS101     Dr. A. Smith      Room 101
Tuesday   10:00–11:30   MATH101   Dr. B. Johnson    Room 102
Wednesday 09:00–11:00   CS201     Dr. A. Smith      Lab 201
...
```

---

### 7. Save Your Work

* Click **"Save Data"**
* A `scheduler_data.json` file will be saved for future use

> Save before exiting to preserve any custom data.

---

### 8. Exit

* Close the main window
* Choose to save when prompted

---

## 🛠 Troubleshooting

### ❌ Error: `No module named 'data.sample_data'`

* **Fix**:

  * Ensure `data/__init__.py` exists
  * Confirm `sample_data.py` is present
  * Delete cache:

    ```bash
    rmdir /s /q data/__pycache__
    ```
  * Test import:

    ```bash
    python -c "from data.sample_data import sample_professors; print('Success')"
    ```

---

### ⚠ Unscheduled Courses

* **Cause**: Dataset too large or conflicting
* **Fix**: Increase `max_iterations` in `utils/scheduler_engine.py`:

```python
def generate_schedule(..., max_iterations: int = 5000)
```

---

### ⚠ Non-Overlap Not Respected

* **Cause**: Constraints too tight
* **Fix**: Review console logs, increase `max_iterations`, or use different course pairs

---

## 📁 Project Structure

```
UniClassScheduler/
├── main.py                 # Entry point
├── models/                 # Data models
├── utils/                  # Scheduling engine
├── gui/                    # GUI components
├── data/                   # Sample data
├── screenshots/            # UI snapshots
├── LICENSE
└── README.md
```
