import tkinter as tk
from tkinter import ttk, messagebox
import datetime
from typing import Optional
from models import Professor, Course, Classroom

class BaseInputFrame(ttk.Frame):
    """Base class for input frames with common functionality."""
    
    def __init__(self, parent: tk.Widget, controller: 'App'):
        super().__init__(parent, padding="20")
        self.controller = controller
        self.create_widgets()
    
    def create_widgets(self) -> None:
        """Create the widgets for this frame."""
        pass
    
    def validate_time_format(self, time_str: str) -> bool:
        """Validate time format (HH:MM)."""
        try:
            datetime.datetime.strptime(time_str, "%H:%M")
            return True
        except ValueError:
            return False
    
    def show_error(self, message: str) -> None:
        """Show an error message."""
        messagebox.showerror("Error", message)

class ProfessorInputFrame(BaseInputFrame):
    """Frame for inputting professor information."""
    
    def create_widgets(self) -> None:
        ttk.Label(self, text="Professor Information", 
                 font=("Helvetica", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        ttk.Label(self, text="Name:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.name_var = tk.StringVar()
        name_entry = ttk.Entry(self, textvariable=self.name_var, width=30)
        name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        name_entry.focus()
        
        ttk.Label(self, text="Available Times:", font=("Helvetica", 10, "bold")).grid(
            row=2, column=0, padx=5, pady=(10, 5), sticky="w")
        
        times_frame = ttk.LabelFrame(self, text="Add Time Slot", padding="10")
        times_frame.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(times_frame, text="Day:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.day_var = tk.StringVar()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        ttk.Combobox(times_frame, textvariable=self.day_var, values=days, width=15, state="readonly").grid(
            row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(times_frame, text="Start Time (HH:MM):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.start_time_var = tk.StringVar()
        ttk.Entry(times_frame, textvariable=self.start_time_var, width=10).grid(
            row=1, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(times_frame, text="End Time (HH:MM):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.end_time_var = tk.StringVar()
        ttk.Entry(times_frame, textvariable=self.end_time_var, width=10).grid(
            row=2, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(times_frame, text="Add Time", command=self.add_time).grid(
            row=3, column=0, columnspan=2, pady=10)
        
        ttk.Label(self, text="Added Time Slots:").grid(row=3, column=0, padx=5, pady=(10, 5), sticky="w")
        self.times_listbox = tk.Listbox(self, width=40, height=5)
        self.times_listbox.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(self, text="Remove Selected Time", command=self.remove_time).grid(
            row=4, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(self, text="Courses:", font=("Helvetica", 10, "bold")).grid(
            row=5, column=0, padx=5, pady=(10, 5), sticky="w")
        
        courses_frame = ttk.LabelFrame(self, text="Add Course", padding="10")
        courses_frame.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(courses_frame, text="Course Code:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.course_var = tk.StringVar()
        ttk.Entry(courses_frame, textvariable=self.course_var, width=15).grid(
            row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(courses_frame, text="Add Course", command=self.add_course).grid(
            row=1, column=0, columnspan=2, pady=10)
        
        self.courses_listbox = tk.Listbox(self, width=40, height=5)
        self.courses_listbox.grid(row=6, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(self, text="Remove Selected Course", command=self.remove_course).grid(
            row=7, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(self, text="Save Professor", command=self.save_professor, style="Accent.TButton").grid(
            row=8, column=0, columnspan=2, pady=(20, 0))
        
        self.available_times: List[Tuple[str, str, str]] = []
        self.courses: List[str] = []
    
    def add_time(self) -> None:
        """Add a time slot to the available times list."""
        day = self.day_var.get()
        start_time = self.start_time_var.get().strip()
        end_time = self.end_time_var.get().strip()
        
        if not day:
            self.show_error("Please select a day.")
            return
        if not self.validate_time_format(start_time) or not self.validate_time_format(end_time):
            self.show_error("Times must be in HH:MM format.")
            return
        
        time_slot = (day, start_time, end_time)
        if time_slot not in self.available_times:
            self.available_times.append(time_slot)
            self.times_listbox.insert(tk.END, f"{day}: {start_time} - {end_time}")
        
        self.day_var.set("")
        self.start_time_var.set("")
        self.end_time_var.set("")
    
    def remove_time(self) -> None:
        """Remove the selected time slot."""
        selection = self.times_listbox.curselection()
        if selection:
            index = selection[0]
            self.times_listbox.delete(index)
            self.available_times.pop(index)
    
    def add_course(self) -> None:
        """Add a course to the professor's courses list."""
        course_code = self.course_var.get().strip().upper()
        if not course_code:
            self.show_error("Please enter a course code.")
            return
        if course_code not in self.courses:
            self.courses.append(course_code)
            self.courses_listbox.insert(tk.END, course_code)
        self.course_var.set("")
    
    def remove_course(self) -> None:
        """Remove the selected course."""
        selection = self.courses_listbox.curselection()
        if selection:
            index = selection[0]
            self.courses_listbox.delete(index)
            self.courses.pop(index)
    
    def save_professor(self) -> None:
        """Save the professor information."""
        name = self.name_var.get().strip()
        if not name:
            self.show_error("Please enter a professor name.")
            return
        if not self.available_times:
            self.show_error("Please add at least one available time slot.")
            return
        if not self.courses:
            self.show_error("Please add at least one course.")
            return
        
        professor = Professor(name, self.available_times, self.courses)
        self.controller.add_professor(professor)
        self.clear_form()
        messagebox.showinfo("Success", f"Professor {name} added successfully.")
    
    def clear_form(self) -> None:
        """Clear all form fields."""
        self.name_var.set("")
        self.day_var.set("")
        self.start_time_var.set("")
        self.end_time_var.set("")
        self.course_var.set("")
        self.available_times = []
        self.courses = []
        self.times_listbox.delete(0, tk.END)
        self.courses_listbox.delete(0, tk.END)

class CourseInputFrame(BaseInputFrame):
    """Frame for inputting course information."""
    
    def create_widgets(self) -> None:
        ttk.Label(self, text="Course Information", 
                 font=("Helvetica", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        ttk.Label(self, text="Course Name:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.name_var = tk.StringVar()
        name_entry = ttk.Entry(self, textvariable=self.name_var, width=30)
        name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        name_entry.focus()
        
        ttk.Label(self, text="Course Code:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.code_var = tk.StringVar()
        ttk.Entry(self, textvariable=self.code_var, width=15).grid(
            row=2, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(self, text="Duration (minutes):").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.duration_var = tk.StringVar(value="90")
        ttk.Entry(self, textvariable=self.duration_var, width=10).grid(
            row=3, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(self, text="Eligible Professors:", font=("Helvetica", 10, "bold")).grid(
            row=4, column=0, padx=5, pady=(10, 5), sticky="w")
        
        profs_frame = ttk.LabelFrame(self, text="Add Professor", padding="10")
        profs_frame.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(profs_frame, text="Professor:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.professor_var = tk.StringVar()
        self.professor_dropdown = ttk.Combobox(profs_frame, textvariable=self.professor_var, width=20, state="readonly")
        self.professor_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(profs_frame, text="Add Professor", command=self.add_professor).grid(
            row=1, column=0, columnspan=2, pady=10)
        
        self.professors_listbox = tk.Listbox(self, width=40, height=5)
        self.professors_listbox.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(self, text="Remove Selected Professor", command=self.remove_professor).grid(
            row=6, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(self, text="Conflicting Courses:", font=("Helvetica", 10, "bold")).grid(
            row=7, column=0, padx=5, pady=(10, 5), sticky="w")
        
        conflicts_frame = ttk.LabelFrame(self, text="Add Conflict", padding="10")
        conflicts_frame.grid(row=7, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(conflicts_frame, text="Course:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.conflict_var = tk.StringVar()
        self.conflict_dropdown = ttk.Combobox(conflicts_frame, textvariable=self.conflict_var, width=20, state="readonly")
        self.conflict_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(conflicts_frame, text="Add Conflict", command=self.add_conflict).grid(
            row=1, column=0, columnspan=2, pady=10)
        
        self.conflicts_listbox = tk.Listbox(self, width=40, height=5)
        self.conflicts_listbox.grid(row=8, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(self, text="Remove Selected Conflict", command=self.remove_conflict).grid(
            row=9, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(self, text="Save Course", command=self.save_course, style="Accent.TButton").grid(
            row=10, column=0, columnspan=2, pady=(20, 0))
        
        self.professors: List[str] = []
        self.conflicts: List[str] = []
    
    def update_professor_dropdown(self) -> None:
        """Update the professor dropdown with available professors."""
        professor_names = [p.name for p in self.controller.professors]
        self.professor_dropdown['values'] = professor_names
    
    def update_conflict_dropdown(self) -> None:
        """Update the conflict dropdown with available courses."""
        course_codes = [c.code for c in self.controller.courses]
        self.conflict_dropdown['values'] = course_codes
    
    def add_professor(self) -> None:
        """Add a professor to the eligible professors list."""
        professor_name = self.professor_var.get().strip()
        if not professor_name:
            self.show_error("Please select a professor.")
            return
        if professor_name not in self.professors:
            self.professors.append(professor_name)
            self.professors_listbox.insert(tk.END, professor_name)
        self.professor_var.set("")
    
    def remove_professor(self) -> None:
        """Remove the selected professor."""
        selection = self.professors_listbox.curselection()
        if selection:
            index = selection[0]
            self.professors_listbox.delete(index)
            self.professors.pop(index)
    
    def add_conflict(self) -> None:
        """Add a course to the conflicts list."""
        course_code = self.conflict_var.get().strip()
        if not course_code:
            self.show_error("Please select a course.")
            return
        if course_code not in self.conflicts:
            self.conflicts.append(course_code)
            self.conflicts_listbox.insert(tk.END, course_code)
        self.conflict_var.set("")
    
    def remove_conflict(self) -> None:
        """Remove the selected conflict."""
        selection = self.conflicts_listbox.curselection()
        if selection:
            index = selection[0]
            self.conflicts_listbox.delete(index)
            self.conflicts.pop(index)
    
    def save_course(self) -> None:
        """Save the course information."""
        name = self.name_var.get().strip()
        code = self.code_var.get().strip().upper()
        try:
            duration = int(self.duration_var.get())
            if duration <= 0:
                raise ValueError("Duration must be positive.")
        except ValueError:
            self.show_error("Duration must be a positive integer.")
            return
        
        if not name:
            self.show_error("Please enter a course name.")
            return
        if not code:
            self.show_error("Please enter a course code.")
            return
        if not self.professors:
            self.show_error("Please add at least one eligible professor.")
            return
        
        course = Course(name, code, duration, self.professors, self.conflicts)
        self.controller.add_course(course)
        self.clear_form()
        messagebox.showinfo("Success", f"Course {code} added successfully.")
    
    def clear_form(self) -> None:
        """Clear all form fields."""
        self.name_var.set("")
        self.code_var.set("")
        self.duration_var.set("90")
        self.professor_var.set("")
        self.conflict_var.set("")
        self.professors = []
        self.conflicts = []
        self.professors_listbox.delete(0, tk.END)
        self.conflicts_listbox.delete(0, tk.END)

class ClassroomInputFrame(BaseInputFrame):
    """Frame for inputting classroom information."""
    
    def create_widgets(self) -> None:
        ttk.Label(self, text="Classroom Information", 
                 font=("Helvetica", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        ttk.Label(self, text="Classroom Name/Number:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.name_var = tk.StringVar()
        name_entry = ttk.Entry(self, textvariable=self.name_var, width=20)
        name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        name_entry.focus()
        
        ttk.Label(self, text="Capacity:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.capacity_var = tk.StringVar(value="30")
        ttk.Entry(self, textvariable=self.capacity_var, width=10).grid(
            row=2, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(self, text="Available Times:", font=("Helvetica", 10, "bold")).grid(
            row=3, column=0, padx=5, pady=(10, 5), sticky="w")
        
        times_frame = ttk.LabelFrame(self, text="Add Time Slot", padding="10")
        times_frame.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(times_frame, text="Day:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.day_var = tk.StringVar()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        ttk.Combobox(times_frame, textvariable=self.day_var, values=days, width=15, state="readonly").grid(
            row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(times_frame, text="Start Time (HH:MM):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.start_time_var = tk.StringVar()
        ttk.Entry(times_frame, textvariable=self.start_time_var, width=10).grid(
            row=1, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(times_frame, text="End Time (HH:MM):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.end_time_var = tk.StringVar()
        ttk.Entry(times_frame, textvariable=self.end_time_var, width=10).grid(
            row=2, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(times_frame, text="Add Time", command=self.add_time).grid(
            row=3, column=0, columnspan=2, pady=10)
        
        ttk.Label(self, text="Added Time Slots:").grid(row=4, column=0, padx=5, pady=(10, 5), sticky="w")
        self.times_listbox = tk.Listbox(self, width=40, height=5)
        self.times_listbox.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(self, text="Remove Selected Time", command=self.remove_time).grid(
            row=5, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(self, text="Features/Equipment:", font=("Helvetica", 10, "bold")).grid(
            row=6, column=0, padx=5, pady=(10, 5), sticky="w")
        
        features_frame = ttk.LabelFrame(self, text="Add Feature", padding="10")
        features_frame.grid(row=6, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(features_frame, text="Feature:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.feature_var = tk.StringVar()
        ttk.Entry(features_frame, textvariable=self.feature_var, width=20).grid(
            row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(features_frame, text="Add Feature", command=self.add_feature).grid(
            row=1, column=0, columnspan=2, pady=10)
        
        self.features_listbox = tk.Listbox(self, width=40, height=5)
        self.features_listbox.grid(row=7, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(self, text="Remove Selected Feature", command=self.remove_feature).grid(
            row=8, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(self, text="Save Classroom", command=self.save_classroom, style="Accent.TButton").grid(
            row=9, column=0, columnspan=2, pady=(20, 0))
        
        self.available_times: List[Tuple[str, str, str]] = []
        self.features: List[str] = []
    
    def add_time(self) -> None:
        """Add a time slot to the available times list."""
        day = self.day_var.get()
        start_time = self.start_time_var.get().strip()
        end_time = self.end_time_var.get().strip()
        
        if not day:
            self.show_error("Please select a day.")
            return
        if not self.validate_time_format(start_time) or not self.validate_time_format(end_time):
            self.show_error("Times must be in HH:MM format.")
            return
        
        time_slot = (day, start_time, end_time)
        if time_slot not in self.available_times:
            self.available_times.append(time_slot)
            self.times_listbox.insert(tk.END, f"{day}: {start_time} - {end_time}")
        
        self.day_var.set("")
        self.start_time_var.set("")
        self.end_time_var.set("")
    
    def remove_time(self) -> None:
        """Remove the selected time slot."""
        selection = self.times_listbox.curselection()
        if selection:
            index = selection[0]
            self.times_listbox.delete(index)
            self.available_times.pop(index)
    
    def add_feature(self) -> None:
        """Add a feature to the classroom's features list."""
        feature = self.feature_var.get().strip()
        if not feature:
            self.show_error("Please enter a feature.")
            return
        if feature not in self.features:
            self.features.append(feature)
            self.features_listbox.insert(tk.END, feature)
        self.feature_var.set("")
    
    def remove_feature(self) -> None:
        """Remove the selected feature."""
        selection = self.features_listbox.curselection()
        if selection:
            index = selection[0]
            self.features_listbox.delete(index)
            self.features.pop(index)
    
    def save_classroom(self) -> None:
        """Save the classroom information."""
        name = self.name_var.get().strip()
        try:
            capacity = int(self.capacity_var.get())
            if capacity <= 0:
                raise ValueError("Capacity must be positive.")
        except ValueError:
            self.show_error("Capacity must be a positive integer.")
            return
        
        if not name:
            self.show_error("Please enter a classroom name/number.")
            return
        if not self.available_times:
            self.show_error("Please add at least one available time slot.")
            return
        
        classroom = Classroom(name, capacity, self.available_times, self.features)
        self.controller.add_classroom(classroom)
        self.clear_form()
        messagebox.showinfo("Success", f"Classroom {name} added successfully.")
    
    def clear_form(self) -> None:
        """Clear all form fields."""
        self.name_var.set("")
        self.capacity_var.set("30")
        self.day_var.set("")
        self.start_time_var.set("")
        self.end_time_var.set("")
        self.feature_var.set("")
        self.available_times = []
        self.features = []
        self.times_listbox.delete(0, tk.END)
        self.features_listbox.delete(0, tk.END)