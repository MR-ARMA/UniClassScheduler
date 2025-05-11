import tkinter as tk
from tkinter import ttk, messagebox
from typing import List, Optional
from gui.input_frames import ProfessorInputFrame, CourseInputFrame, ClassroomInputFrame
from gui.schedule_view import ScheduleViewer
from models import Professor, Course, Classroom, Schedule
from utils import SchedulerEngine
import json
import logging
import os

class App(tk.Tk):
    """Main application class for the University Class Scheduler."""
    
    def __init__(self):
        super().__init__()
        self.title("University Class Scheduler")
        self.geometry("900x700")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        
        self.professors: List[Professor] = []
        self.courses: List[Course] = []
        self.classrooms: List[Classroom] = []
        self.schedule: Optional[Schedule] = None
        self.non_overlap_courses: Optional[tuple[str, str]] = None  # Store course codes to avoid overlap
        self.data_file = "scheduler_data.json"
        
        self.create_widgets()
        self.load_data()
    
    def create_widgets(self) -> None:
        """Create the main window widgets."""
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(main_frame, text="University Class Scheduler", 
                 font=("Helvetica", 18, "bold")).pack(pady=(0, 30))
        
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        buttons = [
            ("Add Professor", self.open_professor_input),
            ("Add Course", self.open_course_input),
            ("Add Classroom", self.open_classroom_input),
            ("Load Sample Data", self.load_sample_data),
            ("Plan Courses", self.open_plan_courses),
            ("Generate Schedule", self.generate_schedule),
            ("View Schedule", self.view_schedule),
            ("Save Data", self.save_data)
        ]
        
        for idx, (text, command) in enumerate(buttons):
            ttk.Button(button_frame, text=text, command=command).grid(row=idx//2, column=idx%2, 
                                                                    padx=10, pady=5, sticky="ew")
        
        button_frame.columnconfigure((0, 1), weight=1)
    
    def open_professor_input(self) -> None:
        """Open a window for professor input."""
        window = tk.Toplevel(self)
        window.title("Add Professor")
        window.geometry("600x600")
        ProfessorInputFrame(window, self).pack(fill=tk.BOTH, expand=True)
    
    def open_course_input(self) -> None:
        """Open a window for course input."""
        window = tk.Toplevel(self)
        window.title("Add Course")
        window.geometry("600x700")
        frame = CourseInputFrame(window, self)
        frame.pack(fill=tk.BOTH, expand=True)
        frame.update_professor_dropdown()
        frame.update_conflict_dropdown()
    
    def open_classroom_input(self) -> None:
        """Open a window for classroom input."""
        window = tk.Toplevel(self)
        window.title("Add Classroom")
        window.geometry("600x600")
        ClassroomInputFrame(window, self).pack(fill=tk.BOTH, expand=True)
    
    def open_plan_courses(self) -> None:
        """Open a window to plan courses and avoid overlaps."""
        window = tk.Toplevel(self)
        window.title("Plan Courses")
        window.geometry("600x400")
        frame = ttk.Frame(window, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Plan Courses (Avoid Overlap)", 
                 font=("Helvetica", 14, "bold")).pack(pady=(0, 20))
        
        ttk.Label(frame, text="First Course:").pack(anchor="w", padx=5, pady=5)
        course1_var = tk.StringVar()
        course1_dropdown = ttk.Combobox(frame, textvariable=course1_var, 
                                       values=[c.code for c in self.courses], state="readonly")
        course1_dropdown.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(frame, text="Second Course:").pack(anchor="w", padx=5, pady=5)
        course2_var = tk.StringVar()
        course2_dropdown = ttk.Combobox(frame, textvariable=course2_var, 
                                       values=[c.code for c in self.courses], state="readonly")
        course2_dropdown.pack(fill=tk.X, padx=5, pady=5)
        
        def set_non_overlap():
            course1 = course1_var.get()
            course2 = course2_var.get()
            if not course1 or not course2:
                messagebox.showerror("Error", "Please select two courses.")
                return
            if course1 == course2:
                messagebox.showerror("Error", "Please select different courses.")
                return
            self.non_overlap_courses = (course1, course2)
            messagebox.showinfo("Success", f"Set {course1} and {course2} to avoid time/place overlap.")
            window.destroy()
        
        def check_overlap():
            if self.schedule is None:
                messagebox.showerror("Error", "Please generate a schedule first.")
                return
            course1 = course1_var.get()
            course2 = course2_var.get()
            if not course1 or not course2:
                messagebox.showerror("Error", "Please select two courses.")
                return
            engine = SchedulerEngine(self.professors, self.courses, self.classrooms)
            overlap = engine.check_course_overlap(self.schedule, course1, course2)
            if overlap:
                messagebox.showwarning("Overlap Detected", 
                    f"{course1} and {course2} overlap in time or place.")
            else:
                messagebox.showinfo("No Overlap", 
                    f"{course1} and {course2} do not overlap in time or place.")
        
        ttk.Button(frame, text="Set Non-Overlapping Constraint", 
                  command=set_non_overlap).pack(pady=10)
        ttk.Button(frame, text="Check Current Schedule", 
                  command=check_overlap).pack(pady=10)
    
    def add_professor(self, professor: Professor) -> None:
        """Add a professor to the list."""
        self.professors.append(professor)
        logging.info(f"Added professor: {professor.name}")
    
    def add_course(self, course: Course) -> None:
        """Add a course to the list."""
        self.courses.append(course)
        logging.info(f"Added course: {course.code}")
    
    def add_classroom(self, classroom: Classroom) -> None:
        """Add a classroom to the list."""
        self.classrooms.append(classroom)
        logging.info(f"Added classroom: {classroom.name}")
    
    def load_sample_data(self) -> None:
        """Load sample data for testing."""
        try:
            from data.sample_data import sample_professors, sample_courses, sample_classrooms
            self.professors = sample_professors
            self.courses = sample_courses
            self.classrooms = sample_classrooms
            self.non_overlap_courses = None  # Reset non-overlap constraint
            messagebox.showinfo("Success", "Sample data loaded successfully.")
            logging.info("Sample data loaded.")
        except ImportError as e:
            messagebox.showerror("Error", 
                f"Failed to load sample data: {str(e)}. Ensure 'data/sample_data.py' exists and 'data/__init__.py' is present.")
            logging.error(f"Failed to load sample data: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load sample data: {str(e)}")
            logging.error(f"Failed to load sample data: {str(e)}")
    
    def generate_schedule(self) -> None:
        """Generate the class schedule."""
        if not all([self.professors, self.courses, self.classrooms]):
            messagebox.showerror("Error", "Please add professors, courses, and classrooms first.")
            logging.warning("Attempted to generate schedule without complete data.")
            return
        
        try:
            engine = SchedulerEngine(self.professors, self.courses, self.classrooms)
            self.schedule = engine.generate_schedule(non_overlap_courses=self.non_overlap_courses)
            
            scheduled_codes = {entry.course_code for entry in self.schedule.entries}
            all_codes = {course.code for course in self.courses}
            unscheduled = all_codes - scheduled_codes
            
            if unscheduled:
                messagebox.showwarning("Warning", 
                    f"Could not schedule: {', '.join(unscheduled)}")
                logging.warning(f"Unscheduled courses: {', '.join(unscheduled)}")
            else:
                messagebox.showinfo("Success", "Schedule generated successfully.")
                logging.info("Schedule generated successfully.")
            
            if self.non_overlap_courses:
                overlap = engine.check_course_overlap(self.schedule, *self.non_overlap_courses)
                if overlap:
                    messagebox.showwarning("Overlap Warning", 
                        f"Could not prevent overlap between {self.non_overlap_courses[0]} and {self.non_overlap_courses[1]}.")
                else:
                    messagebox.showinfo("Non-Overlap Success", 
                        f"{self.non_overlap_courses[0]} and {self.non_overlap_courses[1]} do not overlap.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate schedule: {str(e)}")
            logging.error(f"Failed to generate schedule: {str(e)}")
    
    def view_schedule(self) -> None:
        """Display the generated schedule."""
        if self.schedule is None:
            messagebox.showerror("Error", "Please generate the schedule first.")
            logging.warning("Attempted to view schedule before generation.")
            return
        
        window = tk.Toplevel(self)
        window.title("Class Schedule")
        window.geometry("1200x700")
        ScheduleViewer(window, self.schedule).pack(fill=tk.BOTH, expand=True)
        logging.info("Opened schedule viewer.")
    
    def save_data(self) -> None:
        """Save the current data to a JSON file."""
        try:
            data = {
                "professors": [p.to_dict() for p in self.professors],
                "courses": [c.to_dict() for c in self.courses],
                "classrooms": [c.to_dict() for c in self.classrooms],
                "schedule": self.schedule.to_dict() if self.schedule else None,
                "non_overlap_courses": self.non_overlap_courses
            }
            with open(self.data_file, "w") as f:
                json.dump(data, f, indent=4)
            messagebox.showinfo("Success", "Data saved successfully.")
            logging.info("Data saved to JSON file.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {str(e)}")
            logging.error(f"Failed to save data: {str(e)}")
    
    def load_data(self) -> None:
        """Load data from a JSON file if it exists."""
        if not os.path.exists(self.data_file):
            return
        
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
            
            self.professors = [Professor.from_dict(p) for p in data.get("professors", [])]
            self.courses = [Course.from_dict(c) for c in data.get("courses", [])]
            self.classrooms = [Classroom.from_dict(c) for c in data.get("classrooms", [])]
            if data.get("schedule"):
                self.schedule = Schedule.from_dict(data["schedule"])
            self.non_overlap_courses = data.get("non_overlap_courses")
            
            logging.info("Data loaded from JSON file.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {str(e)}")
            logging.error(f"Failed to load data: {str(e)}")
    
    def on_closing(self) -> None:
        """Handle application closing."""
        if messagebox.askokcancel("Quit", "Do you want to save your data before quitting?"):
            self.save_data()
        self.destroy()
        logging.info("Application closed.")