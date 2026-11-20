import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"

REPORTS_DIR.mkdir(exist_ok=True)

print("\n========== NUMPY ANALYSIS ==========")

marks = np.array([
    [85, 90, 78],
    [75, 80, 88],
    [92, 85, 95],
    [60, 70, 65]
])

print("Marks array:")
print(marks)

print("\nArray shape:", marks.shape)

student_averages = np.mean(marks, axis=1)

print("Student averages:", student_averages)

subject_averages = np.mean(marks, axis=0)

print("Subject averages:", subject_averages)

grace_marks = marks + 5

print("\nMarks after adding grace marks:")
print(grace_marks)

weights = np.array([0.5, 0.3, 0.2])

weighted_scores = np.dot(grace_marks, weights)

print("\nWeighted scores:", weighted_scores)

print("\n========== PANDAS ANALYSIS ==========")

employees_file = DATA_DIR / "employees.csv"

df = pd.read_csv(employees_file)

print("\nEmployee Data:")
print(df)

print("\n========== DATAFRAME INFO ==========")

df.info()

print("\n========== DESCRIBE ==========")

print(df.describe())

print("\n========== LOC ==========")

print(df.loc[0:2, ["name", "department", "salary"]])

print("\n========== ILOC ==========")

print(df.iloc[0:3, 0:3])

print("\n========== FILTERING ==========")

high_salary = df[df["salary"] > 50000]

print(high_salary)

print("\n========== DEPARTMENTS DATA ==========")

departments = pd.DataFrame({
    "department": ["Sales", "HR", "IT", "Finance", "Legal"],
    "head": ["Ramesh", "Lakshmi", "Suresh", "Kumar", "Anand"],
    "budget": [500000, 300000, 800000, 400000, 250000]
})

departments_file = DATA_DIR / "departments.csv"

departments.to_csv(departments_file, index=False)

print(departments)

print("\ndepartments.csv created successfully")

print("\n========== DATA CLEANING ==========")

dirty_df = df.copy()

dirty_df.loc[0, "salary"] = np.nan
dirty_df.loc[1, "salary"] = np.nan

dirty_df = pd.concat(
    [dirty_df, dirty_df.iloc[[2]]],
    ignore_index=True
)

print("\nData before cleaning:")
print(dirty_df)

print("\nMissing values before cleaning:")
print(dirty_df.isnull().sum())

print("\nDuplicate rows before cleaning:")
print(dirty_df.duplicated().sum())

clean_df = dirty_df.drop_duplicates().copy()

salary_median = clean_df["salary"].median()

clean_df["salary"] = clean_df["salary"].fillna(salary_median)

clean_df["id"] = clean_df["id"].astype(int)
clean_df["salary"] = clean_df["salary"].astype(int)

print("\nData after cleaning:")
print(clean_df)

print("\nMissing values after cleaning:")
print(clean_df.isnull().sum())

print("\nDuplicate rows after cleaning:")
print(clean_df.duplicated().sum())

print("\nMedian salary used for filling:", salary_median)

print("\nCorrected data types:")
print(clean_df.dtypes)

print("\n========== DEPARTMENT ANALYSIS ==========")

department_summary = clean_df.groupby("department").agg(
    headcount=("name", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
).reset_index()

print(department_summary)

print("\nHeadcount:")

for _, row in department_summary.iterrows():
    print(f'{row["department"]}: {row["headcount"]}')

print("\n========== INNER JOIN ==========")

inner_join = pd.merge(
    clean_df,
    departments,
    on="department",
    how="inner"
)

print(inner_join)


print("\n========== LEFT JOIN ==========")

left_join = pd.merge(
    clean_df,
    departments,
    on="department",
    how="left"
)

print(left_join)


print("\n========== OUTER JOIN ==========")

outer_join = pd.merge(
    clean_df,
    departments,
    on="department",
    how="outer",
    indicator=True
)

print(outer_join)

departments_without_employees = outer_join.loc[
    outer_join["_merge"] == "right_only",
    "department"
].unique()

print("\nDepartments with no employees:")

for department in departments_without_employees:
    print(department)

print("\n========== CHART 1: BAR CHART ==========")

average_by_department = clean_df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))

average_by_department.plot(
    kind="bar",
    label="Average Salary"
)

plt.title("Average Employee Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary (INR)")
plt.legend()
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(REPORTS_DIR / "bar_chart.png")
plt.close()

print("Insight: The department with the highest average salary has the highest average employee earnings.")

print("\n========== CHART 2: HISTOGRAM ==========")

plt.figure(figsize=(8, 5))

plt.hist(
    clean_df["salary"],
    bins=5,
    edgecolor="black",
    label="Employee Salaries"
)

plt.title("Distribution of Employee Salaries")
plt.xlabel("Salary (INR)")
plt.ylabel("Number of Employees")
plt.legend()
plt.tight_layout()

plt.savefig(REPORTS_DIR / "histogram.png")
plt.close()

print("Insight: The histogram shows how employee salaries are distributed across different salary ranges.")

print("\n========== CHART 3: SCATTER PLOT ==========")

plt.figure(figsize=(8, 5))

plt.scatter(
    clean_df["id"],
    clean_df["salary"],
    label="Employees"
)

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary (INR)")
plt.legend()
plt.tight_layout()

plt.savefig(REPORTS_DIR / "scatter_plot.png")
plt.close()

print("Insight: The scatter plot compares individual employee salaries against their employee IDs.")

print("\n========== CHART 4: LINE CHART ==========")

sorted_df = clean_df.sort_values("id")

plt.figure(figsize=(8, 5))

plt.plot(
    sorted_df["id"],
    sorted_df["salary"],
    marker="o",
    label="Employee Salary"
)

plt.title("Employee Salary Trend")
plt.xlabel("Employee ID")
plt.ylabel("Salary (INR)")
plt.legend()
plt.tight_layout()

plt.savefig(REPORTS_DIR / "line_chart.png")
plt.close()

print("Insight: The line chart displays salary variation across employees in employee ID order.")

print("\n========== TASK 3 COMPLETED ==========")

print("Student averages:", student_averages)

print("Headcount: Sales 2 | HR 2 | IT 3 | Finance 1")

print("Outer join: Department with no employees:", 
      ", ".join(departments_without_employees))

print("\nFour charts saved successfully in reports/")

print("\nTask 3 completed successfully!")