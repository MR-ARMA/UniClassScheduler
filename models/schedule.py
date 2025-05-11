from typing import List, Dict

class ScheduleEntry:
    """Represents a single scheduled class in the timetable."""
    
    def __init__(self, course_code: str, professor_name: str, classroom_name: str, 
                 day: str, start_time: str, end_time: str):
        """Initialize a ScheduleEntry instance."""
        self.course_code = course_code
        self.professor_name = professor_name
        self.classroom_name = classroom_name
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
    
    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "course_code": self.course_code,
            "professor_name": self.professor_name,
            "classroom_name": self.classroom_name,
            "day": self.day,
            "start_time": self.start_time,
            "end_time": self.end_time
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'ScheduleEntry':
        """Create a ScheduleEntry from a dictionary."""
        return cls(
            course_code=data["course_code"],
            professor_name=data["professor_name"],
            classroom_name=data["classroom_name"],
            day=data["day"],
            start_time=data["start_time"],
            end_time=data["end_time"]
        )
    
    def __str__(self) -> str:
        """String representation of the ScheduleEntry."""
        return (f"{self.course_code} - {self.day}, {self.start_time}-{self.end_time}, "
                f"Room: {self.classroom_name}, Prof: {self.professor_name}")

class Schedule:
    """Represents the complete class schedule."""
    
    def __init__(self):
        """Initialize a Schedule instance."""
        self.entries: List[ScheduleEntry] = []
    
    def add_entry(self, entry: ScheduleEntry) -> None:
        """Add a ScheduleEntry to the schedule."""
        self.entries.append(entry)
    
    def get_entries_by_day(self, day: str) -> List[ScheduleEntry]:
        """Get all entries for a specific day."""
        return [entry for entry in self.entries if entry.day == day]
    
    def has_conflict(self, new_entry: ScheduleEntry) -> bool:
        """Check if adding the new entry would cause a conflict."""
        for entry in self.entries:
            if (entry.day == new_entry.day and 
                entry.classroom_name == new_entry.classroom_name and
                not (new_entry.end_time <= entry.start_time or 
                     new_entry.start_time >= entry.end_time)):
                return True
            if (entry.day == new_entry.day and 
                entry.professor_name == new_entry.professor_name and
                not (new_entry.end_time <= entry.start_time or 
                     new_entry.start_time >= entry.end_time)):
                return True
        return False
    
    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {"entries": [entry.to_dict() for entry in self.entries]}
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Schedule':
        """Create a Schedule from a dictionary."""
        schedule = cls()
        for entry_data in data["entries"]:
            schedule.add_entry(ScheduleEntry.from_dict(entry_data))
        return schedule