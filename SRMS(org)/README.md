# School Result Management System (SRMS)

The School Result Management System (SRMS) is a desktop application developed using Python and Tkinter. It helps manage courses, students, results, and reports efficiently. The system also includes a login mechanism for secure access.

## Features

- 📚 **Course Management**
- 👨‍🎓 **Student Management**
- 📝 **Result Management**
- 📊 **Report Generation**
- 🔒 **User Authentication**
- ⏰ **Real-time Clock Display**
- ⚡ **Fast Login Feature**
- 👨‍👩‍👧‍👦 **Student-Parent Interaction**
- 📅 **Daily Report of Exams**
- 🏫 **Admin and Student Sections**

## Workspace Setup

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/srms.git
    cd srms
    ```

2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have the following directory structure:
    ```
    srms/
    ├── images/
    │   ├── bg.png
    │   └── logo_p.png
    ├── course.py
    ├── student.py
    ├── result.py
    ├── report.py
    ├── login.py
    ├── dashboard.py
    ├── requirements.txt
    └── [README.md](http://_vscodecontentref_/1)
    ```

### Running the Application

1. Navigate to the project directory:
    ```bash
    cd srms
    ```

2. Run the application:
    ```bash
    python dashboard.py
    ```

## Code Details

### Main File: `dashboard.py`

This file contains the main class `RMS` which initializes the Tkinter window and sets up the UI components such as buttons, labels, and frames. It also includes methods for updating the clock, updating details from the database, and handling button actions.

### Other Modules

- `course.py`: Contains the `CourseClass` for managing courses.
- `student.py`: Contains the `studentClass` for managing students.
- `result.py`: Contains the `resultClass` for managing results.
- `report.py`: Contains the `reportClass` for generating reports.
- `login.py`: Contains the `login_system` for user authentication.

## Frontend

The frontend of the application is built using Tkinter, a standard GUI library for Python. It includes various widgets such as:

- **Labels**: For displaying text and images.
- **Buttons**: For user interactions.
- **LabelFrame**: For grouping related widgets.
- **Toplevel**: For creating new windows.

## Backend

The backend of the application is powered by SQLite, a lightweight database engine. It handles:

- **Database Connections**: Using `sqlite3` module.
- **Data Retrieval and Updates**: Through SQL queries.
- **Error Handling**: Using try-except blocks to manage exceptions.

## Contributor 
 Sandesh Bhatta 
## Contact

For any technical issues or queries, please contact us at 9741685837.