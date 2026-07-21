# Quesion : Parse, clean, and aggregate department metrics with error handling

csv_data = """name,dept,salary,rating,status
Alice,Sales,50000,4.5,active
Bob,IT,70000,3.8,active
Charlie,Sales,55000,4.9,active
Diana,IT,80000,4.2,inactive
Eve,Sales,45000,3.5,active
Frank,IT,90000,4.7,active
Grace,HR,48000,4.1,active
Hank,HR,52000,3.9,inactive
Ivan,Sales,60000,4.6,active
Jane,IT,75000,3.2,active
Karen,HR,51000,4.3,active
Leo,Sales,48000,2.9,active"""


def parse_csv(raw_data):
    data = []
    lines = raw_data.strip().splitlines()
    if not lines:
        return data

    header = [h.strip() for h in lines[0].split(",")]

    for line_num, line in enumerate(lines[1:], start=2):
        values = line.split(",")

        
        if len(values) != len(header):
            print(f"Warning: Skipping malformed data on line {line_num}")
            continue 

        employee = {}
        for key, value in zip(header, values):
            try:
                if key == "salary":
                    employee[key] = int(value)
                elif key == "rating":
                    employee[key] = float(value)
                else:
                    employee[key] = value.strip()
            except ValueError:
                print(
                    f"Warning: Type conversion failed for column '{key}' on line {line_num}. Using raw value."
                )
                employee[key] = value 

        data.append(employee)

    return data


def clean_data(employees):

    return [
        emp
        for emp in employees
        if emp.get("status") == "active" and emp.get("rating", 0) >= 3.5 
        
    ]


def generate_dept_report(employees):
    """
    Aggregates employee records to generate department-level analytics.
    """
    dept_metrics = {}

    for employee in employees:
        dept = employee["dept"]

        
        if dept not in dept_metrics:
            dept_metrics[dept] = {
                "headcount": 0,
                "total_salary": 0,
                "total_rating": 0.0,
                "top_performer": None,
                "highest_rating": 0.0,
            }

        metrics = dept_metrics[dept]

        
        metrics["headcount"] += 1
        metrics["total_salary"] += employee["salary"]
        metrics["total_rating"] += employee["rating"]

        
        if employee["rating"] > metrics["highest_rating"]:
            metrics["top_performer"] = employee["name"]
            metrics["highest_rating"] = employee["rating"]

    
    for dept, metrics in dept_metrics.items():
        count = metrics["headcount"]
        metrics["avg_salary"] = round(metrics["total_salary"] / count, 2)
        metrics["avg_rating"] = round(metrics["total_rating"] / count, 2)

    return dept_metrics


def print_report(report_data):

    print("=== DEPARTMENT PERFORMANCE REPORT ===")

    for dept, info in report_data.items():
        print(f"\nDept: {dept}")
        print(f"  Headcount     : {info['headcount']}")
        print(f"  Avg Salary    : ${info['avg_salary']:,}")
        print(f"  Avg Rating    : {info['avg_rating']}")
        print(f"  Top Performer : {info['top_performer']} ({info['highest_rating']})")


if __name__ == "__main__": # Main Guarde

    parsed_employees = parse_csv(csv_data)

    cleaned_employees = clean_data(parsed_employees)

    final_report = generate_dept_report(cleaned_employees)

    print_report(final_report)