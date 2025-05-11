from typing import List, Optional

class Course:
    """Represents a course that can be scheduled."""
    
    def __init__(self, name: str, code: str, duration: int = 90, 
                 professors: Optional[List[str]] = None, conflicts: Optional[List[str]] = None):
        """
        Initialize a Course instance.

        Args:
            name (str): The course name.
            code (str): Course code (e.g., CS101).
            duration (int, optional): Duration in minutes. Defaults to 90.
            professors (List[str], optional): List of professor names.
            conflicts (List[str], optional): List of conflicting course codes.

        Raises:
            ValueError: If inputs are invalid.
        """
        if not name or not code:
            raise ValueError("Course name and code must be non-empty strings.")
        if duration <= 0:
            raise ValueError("Duration must be positive.")
        self.name = name
        self.code = code
        self.duration = duration
        self.professors = professors if professors is not None else []
        self.conflicts = conflicts if conflicts is not None else []
    
    def add_professor(self, professor_name: str) -> None:
        """Add a professor who can teach this course."""
        if professor_name not in self.professors:
            self.professors.append(professor_name)
    
    def add_conflict(self, course_code: str) -> None:
        """Add a course that cannot be scheduled simultaneously."""
        if course_code not in self.conflicts:
            self.conflicts.append(course_code)
    
    def has_conflict_with(self, course_code: str) -> bool:
        """Check if this course conflicts with another course."""
        return course_code in self.conflicts
    
    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "name": self.name,
            "code": self.code,
            "duration": self.duration,
            "professors": self.professors,
            "conflicts": self.conflicts
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Course':
        """Create a Course from a dictionary."""
        return cls(
            name=data["name"],
            code=data["code"],
            duration=data["duration"],
            professors=data["professors"],
            conflicts=data["conflicts"]
        )
    
    def __str__(self) -> str:
        """String representation of the Course."""
        return f"{self.code}: {self.name}"