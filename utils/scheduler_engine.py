import random
import datetime
from typing import List, Dict, Optional, Tuple
from models import Professor, Course, Classroom, Schedule, ScheduleEntry
import logging

class SchedulerEngine:
    """Scheduling engine for assigning courses to professors and classrooms."""
    
    def __init__(self, professors: List[Professor], courses: List[Course], classrooms: List[Classroom]):
        """
        Initialize the scheduler engine.

        Args:
            professors (List[Professor]): List of professors.
            courses (List[Course]): List of courses.
            classrooms (List[Classroom]): List of classrooms.
        """
        self.professors = professors
        self.courses = courses
        self.classrooms = classrooms
        self.schedule = Schedule()
        
        self.professors_dict: Dict[str, Professor] = {p.name: p for p in professors}
        self.courses_dict: Dict[str, Course] = {c.code: c for c in courses}
        self.classrooms_dict: Dict[str, Classroom] = {c.name: c for c in classrooms}
        self.time_slots: List[Tuple[str, str, str]] = []
        self._generate_time_slots()
        
        logging.info("Scheduler engine initialized.")
    
    def _generate_time_slots(self, start_hour: int = 8, end_hour: int = 18, slot_duration: int = 30) -> None:
        """Generate time slots for scheduling."""
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        for day in days:
            current_time = datetime.datetime(2023, 1, 1, start_hour, 0)
            end_time = datetime.datetime(2023, 1, 1, end_hour, 0)
            while current_time < end_time:
                start_str = current_time.strftime("%H:%M")
                current_time += datetime.timedelta(minutes=slot_duration)
                end_str = current_time.strftime("%H:%M")
                self.time_slots.append((day, start_str, end_str))
    
    def _calculate_end_time(self, start_time: str, duration: int) -> str:
        """Calculate end time based on start time and duration."""
        hours, minutes = map(int, start_time.split(':'))
        start_datetime = datetime.datetime(2023, 1, 1, hours, minutes)
        end_datetime = start_datetime + datetime.timedelta(minutes=duration)
        return end_datetime.strftime("%H:%M")
    
    def _check_professor_availability(self, professor: Professor, day: str, start_time: str, end_time: str) -> bool:
        """Check if a professor is available at the specified time."""
        return professor.is_available(day, start_time, end_time)
    
    def _check_classroom_availability(self, classroom: Classroom, day: str, start_time: str, end_time: str) -> bool:
        """Check if a classroom is available at the specified time."""
        return classroom.is_available(day, start_time, end_time)
    
    def _check_course_conflicts(self, course_code: str, day: str, start_time: str, end_time: str) -> bool:
        """Check if scheduling a course would create conflicts."""
        course = self.courses_dict[course_code]
        for entry in self.schedule.entries:
            if entry.day != day:
                continue
            if not (end_time <= entry.start_time or start_time >= entry.end_time):
                if (course.has_conflict_with(entry.course_code) or 
                    self.courses_dict[entry.course_code].has_conflict_with(course_code)):
                    return False
        return True
    
    def check_course_overlap(self, schedule: Schedule, course1_code: str, course2_code: str) -> bool:
        """Check if two courses overlap in time or place in the given schedule."""
        course1_entries = [e for e in schedule.entries if e.course_code == course1_code]
        course2_entries = [e for e in schedule.entries if e.course_code == course2_code]
        
        for e1 in course1_entries:
            for e2 in course2_entries:
                if e1.day == e2.day:
                    if not (e1.end_time <= e2.start_time or e1.start_time >= e2.end_time):
                        return True  # Time overlap
                    if e1.classroom_name == e2.classroom_name:
                        return True  # Place overlap
        return False
    
    def generate_schedule(self, non_overlap_courses: Optional[Tuple[str, str]] = None, 
                         max_iterations: int = 1000) -> Schedule:
        """Generate a class schedule, optionally ensuring two courses don't overlap."""
        self.schedule = Schedule()
        courses_to_schedule = list(self.courses)
        random.shuffle(courses_to_schedule)
        
        iterations = 0
        while courses_to_schedule and iterations < max_iterations:
            iterations += 1
            course = courses_to_schedule[0]
            suitable_professors = [p for p in self.professors if p.name in course.professors]
            
            if not suitable_professors:
                courses_to_schedule.pop(0)
                logging.warning(f"No professor available for course: {course.code}")
                continue
            
            scheduled = False
            random.shuffle(suitable_professors)
            for professor in suitable_professors:
                if scheduled:
                    break
                random.shuffle(self.time_slots)
                for day, start_time, _ in self.time_slots:
                    if scheduled:
                        break
                    end_time = self._calculate_end_time(start_time, course.duration)
                    if not self._check_professor_availability(professor, day, start_time, end_time):
                        continue
                    if not self._check_course_conflicts(course.code, day, start_time, end_time):
                        continue
                    random.shuffle(self.classrooms)
                    for classroom in self.classrooms:
                        if not self._check_classroom_availability(classroom, day, start_time, end_time):
                            continue
                        entry = ScheduleEntry(
                            course_code=course.code,
                            professor_name=professor.name,
                            classroom_name=classroom.name,
                            day=day,
                            start_time=start_time,
                            end_time=end_time
                        )
                        if self.schedule.has_conflict(entry):
                            continue
                        # Check non-overlap constraint
                        if non_overlap_courses and course.code in non_overlap_courses:
                            temp_schedule = Schedule()
                            for e in self.schedule.entries:
                                temp_schedule.add_entry(e)
                            temp_schedule.add_entry(entry)
                            other_course = non_overlap_courses[0] if course.code == non_overlap_courses[1] else non_overlap_courses[1]
                            if self.check_course_overlap(temp_schedule, course.code, other_course):
                                continue
                        self.schedule.add_entry(entry)
                        classroom.schedule_class(day, start_time, end_time, course.code)
                        scheduled = True
                        break
            
            if scheduled:
                courses_to_schedule.pop(0)
            else:
                course = courses_to_schedule.pop(0)
                courses_to_schedule.append(course)
        
        logging.info(f"Schedule generation completed in {iterations} iterations.")
        return self.schedule