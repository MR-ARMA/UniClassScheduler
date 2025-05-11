import tkinter as tk
from tkinter import ttk
from typing import List
from models import Schedule, ScheduleEntry

class ScheduleViewer(ttk.Frame):
    """Frame for viewing the generated schedule."""
    
    def __init__(self, parent: tk.Widget, schedule: Schedule):
        super().__init__(parent, padding="20")
        self.schedule = schedule
        self.create_widgets()
    
    def create_widgets(self) -> None:
        """Create the schedule viewer widgets."""
        ttk.Label(self, text="Generated Schedule", 
                 font=("Helvetica", 16, "bold")).pack(pady=(0, 20))
        
        filter_frame = ttk.Frame(self)
        filter_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(filter_frame, text="Filter by Day:").pack(side=tk.LEFT, padx=5)
        self.day_filter = tk.StringVar(value="All")
        days = ["All", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        ttk.Combobox(filter_frame, textvariable=self.day_filter, values=days, state="readonly").pack(side=tk.LEFT, padx=5)
        ttk.Button(filter_frame, text="Apply Filter", command=self.update_tree).pack(side=tk.LEFT, padx=5)
        
        columns = ("Day", "Time", "Course", "Professor", "Classroom")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=20)
        
        for col in columns:
            self.tree.heading(col, text=col, command=lambda c=col: self.sort_tree(c))
            self.tree.column(col, width=200, anchor="center")
        
        self.update_tree()
        
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10), pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=10)
    
    def update_tree(self) -> None:
        """Update the Treeview with filtered schedule entries."""
        self.tree.delete(*self.tree.get_children())
        day_filter = self.day_filter.get()
        
        entries = self.schedule.entries
        if day_filter != "All":
            entries = [e for e in entries if e.day == day_filter]
        
        days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        sorted_entries = sorted(
            entries,
            key=lambda e: (days_order.index(e.day) if e.day in days_order else 999, e.start_time)
        )
        
        for entry in sorted_entries:
            time_str = f"{entry.start_time}-{entry.end_time}"
            values = (entry.day, time_str, entry.course_code, entry.professor_name, entry.classroom_name)
            self.tree.insert("", tk.END, values=values)
    
    def sort_tree(self, col: str) -> None:
        """Sort the Treeview by the specified column."""
        items = [(self.tree.set(k, col), k) for k in self.tree.get_children()]
        items.sort()
        for index, (val, k) in enumerate(items):
            self.tree.move(k, '', index)