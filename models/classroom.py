from typing import List, Tuple, Optional, Dict

class Classroom:
    """Represents a classroom where courses can be held."""
    
    def __init__(self, name: str, capacity: int = 30, 
                 available_times: Optional[List[Tuple[str, str, str]]] = None, 
                 features: Optional[List[str]] = None):
        """
        Initialize a Classroom instance.

        Args:
            name (str): The classroom name/number.
            capacity (int, optional): Maximum capacity. Defaults to 30.
            available_times (List[Tuple[str, str, str]], optional): List of available time slots.
            features (List[str], optional): List of features/equipment.

        Raises:
            ValueError: If inputs are invalid.
        """
        if not name:
            raise ValueError("Classroom name must be non-empty.")
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        self.name = name
        self.capacity = capacity
        self.available_times = available_times if available_times is not None else []
        self.features = features if features is not None else []
        self.scheduled_times: Dict[str, List[Tuple[str, str, str]]] = {}
    
    def add_available_time(self, day: str, start_time: str, end_time: str) -> None:
        """Add a time slot when the classroom is available."""
        self.available_times.append((day, start_time, end_time))
    
    def add_feature(self, feature: str) -> None:
        """Add a feature/equipment to the classroom."""
        if feature not in self.features:
            self.features.append(feature)
    
    def is_available(self, day: str, start_time: str, end_time: str) -> bool:
        """Check if the classroom is available at the specified time."""
        time_available = False
        for avail_day, avail_start, avail_end in self.available_times:
            if (avail_day == day and 
                avail_start <= start_time and 
                avail_end >= end_time):
                time_available = True
                break
        
        if not time_available:
            return False
        
        if day in self.scheduled_times:
            for sched_start, sched_end, _ in self.scheduled_times[day]:
                if not (end_time <= sched_start or start_time >= sched_end):
                    return False
        
        return True
    
    def schedule_class(self, day: str, start_time: str, end_time: str, course_code: str) -> bool:
        """Schedule a course in this classroom."""
        if not self.is_available(day, start_time, end_time):
            return False
        
        if day not in self.scheduled_times:
            self.scheduled_times[day] = []
        
        self.scheduled_times[day].append((start_time, end_time, course_code))
        self.scheduled_times[day].sort()
        return True
    
    def get_schedule(self) -> Dict[str, List[Tuple[str, str, str]]]:
        """Get the schedule for this classroom."""
        return self.scheduled_times
    
    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "name": self.name,
            "capacity": self.capacity,
            "available_times": self.available_times,
            "features": self.features,
            "scheduled_times": self.scheduled_times
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Classroom':
        """Create a Classroom from a dictionary."""
        classroom = cls(
            name=data["name"],
            capacity=data["capacity"],
            available_times=data["available_times"],
            features=data["features"]
        )
        classroom.scheduled_times = data.get("scheduled_times", {})
        return classroom
    
    def __str__(self) -> str:
        """String representation of the Classroom."""
        return f"Classroom: {self.name} (Capacity: {self.capacity})"