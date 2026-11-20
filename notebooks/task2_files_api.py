import csv
import json
import os
import requests

from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"

REPORTS_DIR.mkdir(exist_ok=True)

load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("API_KEY")

if API_KEY:
    print("API_KEY loaded successfully")
else:
    print("API_KEY not found")

employees_file = DATA_DIR / "employees.csv"

with open(employees_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

for emp in employees:
    emp["id"] = int(emp["id"])
    emp["salary"] = int(emp["salary"])

print("Rows read:", len(employees))

employees_json = DATA_DIR / "employees.json"

with open(employees_json, "w", encoding="utf-8") as file:
    json.dump(employees, file, indent=4)

print("employees.json created successfully")

high_earners = [
    emp for emp in employees
    if emp["salary"] > 50000
]

high_earners_file = DATA_DIR / "high_earners.csv"

with open(high_earners_file, "w", newline="", encoding="utf-8") as file:

    fieldnames = ["id", "name", "department", "salary", "city"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(high_earners)

print("High earners:", len(high_earners))

API_URL = "https://jsonplaceholder.typicode.com/users"

print("\n========== API USERS ==========")

try:
    response = requests.get(API_URL, timeout=5)

    response.raise_for_status()

    users = response.json()

    # Display first 3 users
    for user in users[:3]:
        print(
            f'{user.get("id")} - '
            f'{user.get("name")} - '
            f'{user.get("email")}'
        )

except requests.exceptions.Timeout:
    print("Error: API request timed out")

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to API")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

except requests.exceptions.RequestException as e:
    print("Request Error:", e)

print("\n========== 404 ERROR HANDLING ==========")

try:
    response = requests.get(
        API_URL + "/9999",
        timeout=5
    )

    if response.status_code == 404:
        print("/users/9999 -> 404 Not found")
    else:
        response.raise_for_status()
        print("Unexpected response:", response.status_code)

except requests.exceptions.Timeout:
    print("Error: API request timed out")

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to API")

except requests.exceptions.RequestException as e:
    print("Request Error:", e)

parsed_users = []

try:
    if "users" in locals():

        for user in users:

            user_details = {
                "id": user.get("id"),
                "name": user.get("name"),
                "email": user.get("email"),

                # Access nested JSON safely
                "company_name": user.get("company", {}).get("name"),

                "city": user.get("address", {}).get("city")
            }

            parsed_users.append(user_details)

        # Save extracted information
        users_json = DATA_DIR / "users.json"

        with open(users_json, "w", encoding="utf-8") as file:
            json.dump(parsed_users, file, indent=4)

        print("\nusers.json created successfully")

except (TypeError, ValueError) as e:
    print("JSON parsing error:", e)
