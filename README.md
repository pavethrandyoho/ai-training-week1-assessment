# Week 1 Assessment – Python & Data Engineering

## Project Overview

This repository contains my Week 1 Python and Data Engineering assessment. It covers Python fundamentals, object-oriented programming, file handling, REST API integration, NumPy, Pandas, data cleaning, data visualization, Git, and Jupyter Notebook.

## Project Structure

```text
week1-assessment/
│
├── data/
│   ├── employees.csv
│   ├── employees.json
│   ├── high_earners.csv
│   ├── departments.csv
│   └── users.json
│
├── notebooks/
│   └── task4_analysis.ipynb
│
├── reports/
│   ├── bar_chart.png
│   ├── histogram.png
│   ├── scatter_plot.png
│   └── line_chart.png
│
├── src/
│   ├── analysis.py
│   └── task4_analysis.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or later
- Git
- Visual Studio Code
- Jupyter Notebook

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/week1-assessment.git
cd week1-assessment
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows (Git Bash):**

```bash
source venv/Scripts/activate
```

**Windows (Command Prompt):**

```cmd
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
API_KEY=my_secret_demo_key
```

The `.env` file is excluded from Git using `.gitignore`.

### 6. Run the Python analysis

```bash
python src/analysis.py
```

### 7. Open the Jupyter Notebook

```bash
jupyter notebook
```

Open `notebooks/task4_analysis.ipynb` and run the notebook cells.

## Assessment Tasks

### Task 1 – Python Fundamentals

- Implemented Python functions using `*args` and `**kwargs`.
- Created Employee and Manager classes using inheritance.
- Implemented custom salary validation exceptions.
- Used list comprehensions, `map()`, `filter()`, and lambda functions.
- Demonstrated `break`, `continue`, and exception handling.

### Task 2 – File Handling and APIs

- Read employee data from CSV files.
- Converted CSV data into JSON.
- Exported employees earning more than ₹50,000 into a separate CSV file.
- Used environment variables with `python-dotenv`.
- Retrieved user information from a REST API using Requests.
- Handled API errors and saved API responses as JSON.

### Task 3 – NumPy, Pandas and Data Visualization

- Created and analyzed NumPy arrays.
- Calculated student and subject averages.
- Applied broadcasting and weighted scores using `np.dot()`.
- Explored employee data using Pandas.
- Cleaned missing values and duplicate records.
- Performed department-level grouping and aggregation.
- Used inner, left, and outer joins.
- Created bar, histogram, scatter, and line charts.

### Task 4 – Git, Terminal and Jupyter Notebook

- Created and organized the project using terminal commands.
- Used `mkdir`, `mv`, `cp`, and `grep`.
- Created and worked on the `feature/analysis` Git branch.
- Maintained multiple commits with descriptive messages.
- Created a Jupyter Notebook with Markdown headings.
- Used `%timeit` for performance measurement.
- Exported the notebook to Python using `nbconvert`.
- Created and resolved a README merge conflict.
- Opened and merged a Pull Request into `main`.

## Findings

1. The employee dataset contains 8 employee records across 4 departments.
2. The IT department has the highest employee count, with 3 employees.
3. Five employees have salaries greater than ₹50,000.
4. The Legal department has no employees in the supplied dataset.
5. Salary analysis and visualizations reveal differences in salary distribution across departments.

## Output Files

The project generates the following outputs:

- `data/employees.json` – Employee data in JSON format.
- `data/high_earners.csv` – Employees earning more than ₹50,000.
- `data/users.json` – User information retrieved from the API.
- `reports/bar_chart.png` – Average salary by department.
- `reports/histogram.png` – Employee salary distribution.
- `reports/scatter_plot.png` – Employee ID versus salary.
- `reports/line_chart.png` – Salary trend by employee ID.

## Git Workflow

The project uses the following Git workflow:

- `main` – Main project branch.
- `feature/analysis` – Branch used for analysis and assessment development.

Changes were committed in small steps with descriptive commit messages, reviewed through a Pull Request, and merged into the `main` branch.

## Author

Week 1 Python & Data Engineering Assessment