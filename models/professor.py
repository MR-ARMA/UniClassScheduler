from typing import List, Tuple, Optional

class Professor:
    """Represents a professor who can teach courses."""
    
    def __init__(self, name: str, available_times: Optional[List[Tuple[str, str, str]]] = None, 
                 courses: Optional[List[str]] = None):
        """
        Initialize a Professor instance.

        Args:
            name (str): The professor's name.
            available_times (List[Tuple[str, str, str]], optional): List of (day, start_time, end_time) tuples.
            courses (List[str], optional): List of course codes.

        Raises:
            ValueError: If name is empty or invalid.
        """
        if not name or not isinstance(name, str):
            raise ValueError("Professor name must be a non-empty string.")
        self.name = name
        self.available_times = available_times if available_times is not None else []
        self.courses = courses if courses is not None else []
    
    def add_available_time(self, day: str, start_time: str, end_time: str) -> None:
        """Add a time slot to the professor's availability."""
        self.available_times.append((day, start_time, end_time))
    
    def add_course(self, course_name: str) -> None:
        """Add a course the professor can teach."""
        if course_name not in self.courses:
            self.courses.append(course_name)
    
    def is_available(self, day: str, start_time: str, end_time: str) -> bool:
        """Check if the professor is available at the specified time."""
        for avail_day, avail_start, avail_end in self.available_times:
            if (avail_day == day and 
                avail_start <= start_time and 
                avail_end >= end_time):
                return True
        return False
    
    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "name": self.name,
            "available_times": self.available_times,
            "courses": self.courses
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Professor':
        """Create a Professor from a dictionary."""
        return cls(
            name=data["name"],
            available_times=data["available_times"],
            courses=data["courses"]
        )
    
    def __str__(self) -> str:
        """String representation of the Professor."""
        return f"Professor: {self.name}"