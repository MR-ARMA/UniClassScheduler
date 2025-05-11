from models import Professor, Course, Classroom

sample_professors = [
    Professor(
        name="Dr. Alice Smith",
        available_times=[
            ("Monday", "09:00", "12:00"),
            ("Wednesday", "09:00", "12:00"),
            ("Friday", "14:00", "17:00")
        ],
        courses=["CS101", "CS201", "CS301", "CS401"]
    ),
    Professor(
        name="Dr. Bob Johnson",
        available_times=[
            ("Tuesday", "10:00", "13:00"),
            ("Thursday", "10:00", "13:00"),
            ("Friday", "09:00", "12:00")
        ],
        courses=["MATH101", "MATH201", "MATH301", "CS201"]
    ),
    Professor(
        name="Dr. Carol White",
        available_times=[
            ("Monday", "13:00", "16:00"),
            ("Wednesday", "13:00", "16:00"),
            ("Thursday", "14:00", "17:00")
        ],
        courses=["PHYS101", "PHYS201", "PHYS301"]
    ),
    Professor(
        name="Dr. David Lee",
        available_times=[
            ("Monday", "09:00", "11:00"),  # Overlap with Alice Smith
            ("Tuesday", "14:00", "17:00"),
            ("Friday", "10:00", "13:00")
        ],
        courses=["CHEM101", "CHEM201", "CS301"]
    ),
    Professor(
        name="Dr. Emma Brown",
        available_times=[
            ("Wednesday", "09:00", "12:00"),
            ("Thursday", "09:00", "12:00"),
            ("Friday", "13:00", "16:00")
        ],
        courses=["ENG101", "ENG201", "ENG301"]
    ),
    Professor(
        name="Dr. Frank Wilson",
        available_times=[
            ("Monday", "10:00", "13:00"),
            ("Tuesday", "10:00", "13:00"),
            ("Thursday", "14:00", "17:00")
        ],
        courses=["CS102", "CS202", "CS302"]
    ),
    Professor(
        name="Dr. Grace Taylor",
        available_times=[
            ("Monday", "13:00", "16:00"),
            ("Wednesday", "10:00", "13:00"),
            ("Friday", "09:00", "12:00")
        ],
        courses=["MATH102", "MATH202", "MATH302"]
    ),
    Professor(
        name="Dr. Henry Davis",
        available_times=[
            ("Tuesday", "09:00", "12:00"),
            ("Thursday", "13:00", "16:00"),
            ("Friday", "14:00", "17:00")
        ],
        courses=["PHYS102", "PHYS202", "PHYS302"]
    ),
    Professor(
        name="Dr. Isabella Martinez",
        available_times=[
            ("Monday", "09:00", "12:00"),  # Overlap with Alice Smith, David Lee
            ("Wednesday", "14:00", "17:00"),
            ("Friday", "10:00", "13:00")
        ],
        courses=["CHEM102", "CHEM202", "CHEM302"]
    ),
    Professor(
        name="Dr. James Anderson",
        available_times=[
            ("Tuesday", "13:00", "16:00"),
            ("Thursday", "09:00", "12:00"),
            ("Friday", "13:00", "16:00")
        ],
        courses=["ENG102", "ENG202", "ENG302"]
    ),
    Professor(
        name="Dr. Karen Thomas",
        available_times=[
            ("Monday", "14:00", "17:00"),
            ("Wednesday", "09:00", "12:00"),
            ("Friday", "09:00", "12:00")
        ],
        courses=["CS103", "CS203", "CS303"]
    ),
    Professor(
        name="Dr. Liam Garcia",
        available_times=[
            ("Tuesday", "10:00", "13:00"),
            ("Thursday", "14:00", "17:00"),
            ("Friday", "10:00", "13:00")
        ],
        courses=["MATH103", "MATH203", "MATH303"]
    ),
    Professor(
        name="Dr. Mia Rodriguez",
        available_times=[
            ("Monday", "13:00", "16:00"),
            ("Wednesday", "13:00", "16:00"),
            ("Friday", "14:00", "17:00")
        ],
        courses=["PHYS103", "PHYS203", "PHYS303"]
    ),
    Professor(
        name="Dr. Noah Hernandez",
        available_times=[
            ("Tuesday", "09:00", "12:00"),
            ("Thursday", "09:00", "12:00"),
            ("Friday", "13:00", "16:00")
        ],
        courses=["CHEM103", "CHEM203", "CHEM303"]
    ),
    Professor(
        name="Dr. Olivia Lopez",
        available_times=[
            ("Monday", "10:00", "13:00"),
            ("Wednesday", "10:00", "13:00"),
            ("Friday", "09:00", "12:00")
        ],
        courses=["ENG103", "ENG203", "ENG303"]
    ),
    Professor(
        name="Dr. Paul Walker",
        available_times=[
            ("Tuesday", "14:00", "17:00"),
            ("Thursday", "13:00", "16:00"),
            ("Friday", "10:00", "13:00")
        ],
        courses=["CS104", "CS204", "CS304"]
    ),
    Professor(
        name="Dr. Quinn Adams",
        available_times=[
            ("Monday", "09:00", "12:00"),  # Overlap with Alice Smith, Isabella Martinez
            ("Wednesday", "14:00", "17:00"),
            ("Friday", "14:00", "17:00")
        ],
        courses=["MATH104", "MATH204", "MATH304"]
    ),
    Professor(
        name="Dr. Rachel Young",
        available_times=[
            ("Tuesday", "10:00", "13:00"),
            ("Thursday", "10:00", "13:00"),
            ("Friday", "09:00", "12:00")
        ],
        courses=["PHYS104", "PHYS204", "PHYS304"]
    ),
    Professor(
        name="Dr. Samuel King",
        available_times=[
            ("Monday", "13:00", "16:00"),
            ("Wednesday", "09:00", "12:00"),
            ("Friday", "13:00", "16:00")
        ],
        courses=["CHEM104", "CHEM204", "CHEM304"]
    ),
    Professor(
        name="Dr. Tara Scott",
        available_times=[
            ("Tuesday", "09:00", "12:00"),
            ("Thursday", "14:00", "17:00"),
            ("Friday", "10:00", "13:00")
        ],
        courses=["ENG104", "ENG204", "ENG304"]
    )
]

sample_courses = [
    Course(
        name="Introduction to Programming",
        code="CS101",
        duration=90,
        professors=["Dr. Alice Smith"],
        conflicts=["MATH101", "CHEM101"]  # Overlap potential
    ),
    Course(
        name="Data Structures",
        code="CS201",
        duration=120,
        professors=["Dr. Alice Smith", "Dr. Bob Johnson"],
        conflicts=["PHYS101"]
    ),
    Course(
        name="Algorithms",
        code="CS301",
        duration=90,
        professors=["Dr. Alice Smith", "Dr. David Lee"],
        conflicts=["ENG101"]
    ),
    Course(
        name="Operating Systems",
        code="CS401",
        duration=90,
        professors=["Dr. Alice Smith"],
        conflicts=["MATH201"]
    ),
    Course(
        name="Calculus I",
        code="MATH101",
        duration=90,
        professors=["Dr. Bob Johnson"],
        conflicts=["CS101", "PHYS101"]  # Overlap with CS101
    ),
    Course(
        name="Linear Algebra",
        code="MATH201",
        duration=90,
        professors=["Dr. Bob Johnson"],
        conflicts=["CS401"]
    ),
    Course(
        name="Differential Equations",
        code="MATH301",
        duration=90,
        professors=["Dr. Bob Johnson"],
        conflicts=["CHEM201"]
    ),
    Course(
        name="Mechanics",
        code="PHYS101",
        duration=120,
        professors=["Dr. Carol White"],
        conflicts=["CS201", "MATH101"]
    ),
    Course(
        name="Electromagnetism",
        code="PHYS201",
        duration=90,
        professors=["Dr. Carol White"],
        conflicts=["ENG201"]
    ),
    Course(
        name="Quantum Physics",
        code="PHYS301",
        duration=90,
        professors=["Dr. Carol White"],
        conflicts=["CS301"]
    ),
    Course(
        name="General Chemistry",
        code="CHEM101",
        duration=90,
        professors=["Dr. David Lee"],
        conflicts=["CS101"]
    ),
    Course(
        name="Organic Chemistry",
        code="CHEM201",
        duration=120,
        professors=["Dr. David Lee"],
        conflicts=["MATH301"]
    ),
    Course(
        name="Analytical Chemistry",
        code="CHEM301",
        duration=90,
        professors=["Dr. David Lee"],
        conflicts=["ENG301"]
    ),
    Course(
        name="Introduction to Literature",
        code="ENG101",
        duration=90,
        professors=["Dr. Emma Brown"],
        conflicts=["CS301"]
    ),
    Course(
        name="Creative Writing",
        code="ENG201",
        duration=90,
        professors=["Dr. Emma Brown"],
        conflicts=["PHYS201"]
    ),
    Course(
        name="Literary Theory",
        code="ENG301",
        duration=90,
        professors=["Dr. Emma Brown"],
        conflicts=["CHEM301"]
    ),
    Course(
        name="Programming II",
        code="CS102",
        duration=90,
        professors=["Dr. Frank Wilson"],
        conflicts=["MATH102"]
    ),
    Course(
        name="Database Systems",
        code="CS202",
        duration=120,
        professors=["Dr. Frank Wilson"],
        conflicts=["PHYS102"]
    ),
    Course(
        name="Software Engineering",
        code="CS302",
        duration=90,
        professors=["Dr. Frank Wilson"],
        conflicts=["ENG102"]
    ),
    Course(
        name="Calculus II",
        code="MATH102",
        duration=90,
        professors=["Dr. Grace Taylor"],
        conflicts=["CS102"]
    ),
    Course(
        name="Probability",
        code="MATH202",
        duration=90,
        professors=["Dr. Grace Taylor"],
        conflicts=["CHEM102"]
    ),
    Course(
        name="Number Theory",
        code="MATH302",
        duration=90,
        professors=["Dr. Grace Taylor"],
        conflicts=["PHYS102"]
    ),
    Course(
        name="Thermodynamics",
        code="PHYS102",
        duration=120,
        professors=["Dr. Henry Davis"],
        conflicts=["CS202", "MATH302"]
    ),
    Course(
        name="Optics",
        code="PHYS202",
        duration=90,
        professors=["Dr. Henry Davis"],
        conflicts=["ENG202"]
    ),
    Course(
        name="Relativity",
        code="PHYS302",
        duration=90,
        professors=["Dr. Henry Davis"],
        conflicts=["CHEM102"]
    ),
    Course(
        name="Inorganic Chemistry",
        code="CHEM102",
        duration=90,
        professors=["Dr. Isabella Martinez"],
        conflicts=["MATH202", "PHYS302"]
    ),
    Course(
        name="Biochemistry",
        code="CHEM202",
        duration=120,
        professors=["Dr. Isabella Martinez"],
        conflicts=["ENG202"]
    ),
    Course(
        name="Physical Chemistry",
        code="CHEM302",
        duration=90,
        professors=["Dr. Isabella Martinez"],
        conflicts=["CS103"]
    ),
    Course(
        name="American Literature",
        code="ENG102",
        duration=90,
        professors=["Dr. James Anderson"],
        conflicts=["CS302"]
    ),
    Course(
        name="Poetry",
        code="ENG202",
        duration=90,
        professors=["Dr. James Anderson"],
        conflicts=["PHYS202", "CHEM202"]
    ),
    Course(
        name="Drama",
        code="ENG302",
        duration=90,
        professors=["Dr. James Anderson"],
        conflicts=["MATH103"]
    ),
    Course(
        name="Computer Networks",
        code="CS103",
        duration=90,
        professors=["Dr. Karen Thomas"],
        conflicts=["CHEM302"]
    ),
    Course(
        name="Artificial Intelligence",
        code="CS203",
        duration=120,
        professors=["Dr. Karen Thomas"],
        conflicts=["PHYS103"]
    ),
    Course(
        name="Machine Learning",
        code="CS303",
        duration=90,
        professors=["Dr. Karen Thomas"],
        conflicts=["ENG103"]
    ),
    Course(
        name="Statistics",
        code="MATH103",
        duration=90,
        professors=["Dr. Liam Garcia"],
        conflicts=["ENG302"]
    ),
    Course(
        name="Algebra",
        code="MATH203",
        duration=90,
        professors=["Dr. Liam Garcia"],
        conflicts=["CHEM103"]
    ),
    Course(
        name="Topology",
        code="MATH303",
        duration=90,
        professors=["Dr. Liam Garcia"],
        conflicts=["PHYS103"]
    ),
    Course(
        name="Astrophysics",
        code="PHYS103",
        duration=120,
        professors=["Dr. Mia Rodriguez"],
        conflicts=["CS203", "MATH303"]
    ),
    Course(
        name="Particle Physics",
        code="PHYS203",
        duration=90,
        professors=["Dr. Mia Rodriguez"],
        conflicts=["ENG203"]
    ),
    Course(
        name="Solid State Physics",
        code="PHYS303",
        duration=90,
        professors=["Dr. Mia Rodriguez"],
        conflicts=["CHEM103"]
    )
]

sample_classrooms = [
    Classroom(
        name="Room 101",
        capacity=40,
        available_times=[
            ("Monday", "08:00", "12:00"),  # Limited morning slot
            ("Tuesday", "08:00", "18:00"),
            ("Wednesday", "08:00", "18:00"),
            ("Thursday", "08:00", "18:00"),
            ("Friday", "08:00", "18:00")
        ],
        features=["Projector", "Whiteboard"]
    ),
    Classroom(
        name="Room 102",
        capacity=30,
        available_times=[
            ("Monday", "13:00", "18:00"),  # Afternoon only
            ("Tuesday", "08:00", "18:00"),
            ("Wednesday", "08:00", "18:00"),
            ("Thursday", "08:00", "18:00"),
            ("Friday", "08:00", "18:00")
        ],
        features=["Whiteboard", "Smartboard"]
    ),
    Classroom(
        name="Lab 201",
        capacity=25,
        available_times=[
            ("Wednesday", "09:00", "17:00"),  # Limited days
            ("Friday", "09:00", "17:00")
        ],
        features=["Computers", "Projector"]
    ),
    Classroom(
        name="Room 103",
        capacity=50,
        available_times=[
            ("Monday", "09:00", "17:00"),
            ("Tuesday", "09:00", "17:00"),
            ("Thursday", "09:00", "17:00")
        ],
        features=["Projector", "Speakers"]
    ),
    Classroom(
        name="Room 104",
        capacity=35,
        available_times=[
            ("Monday", "08:00", "18:00"),
            ("Wednesday", "08:00", "18:00"),
            ("Friday", "08:00", "18:00")
        ],
        features=["Whiteboard", "Projector"]
    ),
    Classroom(
        name="Lab 202",
        capacity=20,
        available_times=[
            ("Tuesday", "10:00", "16:00"),
            ("Thursday", "10:00", "16:00")
        ],
        features=["Computers", "Lab Equipment"]
    ),
    Classroom(
        name="Room 201",
        capacity=45,
        available_times=[
            ("Monday", "08:00", "18:00"),
            ("Tuesday", "08:00", "18:00"),
            ("Wednesday", "08:00", "18:00")
        ],
        features=["Smartboard", "Whiteboard"]
    ),
    Classroom(
        name="Room 202",
        capacity=30,
        available_times=[
            ("Thursday", "09:00", "17:00"),
            ("Friday", "09:00", "17:00")
        ],
        features=["Projector", "Whiteboard"]
    ),
    Classroom(
        name="Room 203",
        capacity=40,
        available_times=[
            ("Monday", "10:00", "16:00"),
            ("Tuesday", "10:00", "16:00"),
            ("Friday", "10:00", "16:00")
        ],
        features=["Speakers", "Whiteboard"]
    ),
    Classroom(
        name="Lab 301",
        capacity=25,
        available_times=[
            ("Monday", "09:00", "13:00"),  # Overlap with Room 101
            ("Wednesday", "09:00", "13:00")
        ],
        features=["Computers", "Projector"]
    ),
    Classroom(
        name="Room 204",
        capacity=35,
        available_times=[
            ("Tuesday", "08:00", "18:00"),
            ("Thursday", "08:00", "18:00"),
            ("Friday", "08:00", "18:00")
        ],
        features=["Projector", "Whiteboard"]
    ),
    Classroom(
        name="Room 205",
        capacity=50,
        available_times=[
            ("Monday", "13:00", "18:00"),
            ("Wednesday", "13:00", "18:00")
        ],
        features=["Smartboard", "Speakers"]
    ),
    Classroom(
        name="Room 301",
        capacity=40,
        available_times=[
            ("Tuesday", "09:00", "17:00"),
            ("Thursday", "09:00", "17:00")
        ],
        features=["Whiteboard", "Projector"]
    ),
    Classroom(
        name="Room 302",
        capacity=30,
        available_times=[
            ("Monday", "08:00", "18:00"),
            ("Friday", "08:00", "18:00")
        ],
        features=["Whiteboard", "Smartboard"]
    ),
    Classroom(
        name="Lab 302",
        capacity=20,
        available_times=[
            ("Wednesday", "10:00", "16:00"),
            ("Friday", "10:00", "16:00")
        ],
        features=["Computers", "Lab Equipment"]
    )
]