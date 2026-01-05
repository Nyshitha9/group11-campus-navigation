# Campus Navigation System

**CO7095 – Software Measurement and Quality Assurance (2025–26)**  
**Backend Software Project (Python)**

---

## 1. Project Overview

This project implements a **Campus Navigation System** that allows users to manage campus locations and paths, validate campus connectivity, and compute routes such as shortest, fastest, and alternative routes.

The system is **backend-only**, uses a **text-based interface**, and stores data using **serialized JSON files**, strictly following the module requirements. No GUI or database is used, as these do not provide additional marks and would require extra testing effort.

The project applies **Agile Scrum**, **software quality assurance**, and **testing techniques** taught in **CO7095**, including:

- Black-Box Testing  
- White-Box Testing  
- Symbolic Execution  
- Concolic Testing  
- Test Coverage Measurement  

---

## 2. Technologies Used

- **Programming Language:** Python 3.x (mandatory)  
- **IDE:** PyCharm (mandatory)  
- **Version Control:** GitHub  
- **Storage:** JSON files  
- **Testing Framework:** `unittest`  
- **Coverage Tool:** `coverage.py`  

---

## 3. Project Structure

```text
campus-navigation/
│
├── core/
│   ├── map_manager.py
│   ├── path_manager.py
│   ├── route_engine.py
│   ├── validator.py
│   ├── preferences.py
│   ├── file_handler.py
│   ├── version_control.py
│   ├── categories.py
│   ├── utils.py
│   └── logger.py
│
├── data/
│   ├── map.json
│   ├── preferences.json
│   ├── system.log
│   └── versions/
│
│
├── main.py
├── README.md
└── requirements.txt

Do not rename folders or files. Naming conventions are strictly checked during marking.

4. How to Uncompress and Open in Percy Gee Lab

Copy the submitted .zip file to the lab computer

Right-click → Extract Here

Open PyCharm

Click File → Open

Select the extracted project folder

Allow PyCharm to index the project

If the project cannot be opened in PyCharm, marks will be lost.
```
## 5. How to Run the Application

Open the PyCharm terminal (or Command Prompt):

python main.py


### A menu-driven text interface will appear allowing:

Location management

Path management

Route computation

Preferences handling

ASCII map visualization

## 6. Black-Box Testing

Black-box tests are implemented using specification-based and random-based techniques.

Techniques Implemented

Equivalence Partitioning

Boundary Value Analysis

Category Partition

## Random Testing



Each test file clearly documents:

Function under test

Testing technique used

Expected vs actual result



6. Research Component: Symbolic Execution & Concolic Testing

As required by the module, symbolic execution and concolic testing are applied to all core functions.

Implemented Tests

Symbolic path exploration for Validator.validate_speed

Concolic testing with concrete + symbolic inputs

Run Symbolic Tests
python -m unittest <student_id>.test.whitebox.symbolic

Run Concolic Tests
python -m unittest <student_id>.test.whitebox.concolic


Symbolic execution trees, path conditions, and derived test inputs are explained in Section A (Research Component) of the report.

7. Test Coverage Measurement
Step 1: Install Coverage Tool
pip install coverage

Step 2: Run Coverage
coverage run -m unittest discover

Step 3: View Coverage Report
coverage report

Optional: HTML Coverage
coverage html


Average coverage ≥ 85%, satisfying the marking rubric.

8. Configuration Management & Versioning

Map versions are backed up automatically

Backup files stored in:

data/versions/


GitHub branches are linked to user stories

Evidence of configuration management is provided in the report

9. Logging

All user actions are logged to:

data/system.log


This supports traceability and software quality auditing.

10. Agile Scrum Evidence

Minimum 3 sprints

Equal user story distribution

Planning Poker estimation

Burndown charts, velocity, PERT, COCOMO I & II, EVM

GitHub Projects board used for tracking

11. Rubric Compliance Summary

Python only
No GUI or database
All functions tested
Black-box & white-box separation
Symbolic & concolic testing included
≥ 85% test coverage
Runs on Percy Gee lab computers
Detailed README provided

12. Authors

Member 1 –  259051722

Member 2 – 259039989

Member 3 – 259038057

Member 4 – 259010889
