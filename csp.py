import random
from constraint import Problem

def min_conflicts(employees, seats, preferences, max_iterations=100):
    # Initial random assignment
    assignment = {e: random.choice(preferences[e]) for e in employees}

    for _ in range(max_iterations):
        # Check for conflicts (employees sharing a seat)
        conflicts = []
        seat_count = {s: [] for s in seats}
        
        for e, s in assignment.items():
            seat_count[s].append(e)
        print(seat_count)

        # Identify conflicting employees
        for s, emp_list in seat_count.items():
            if len(emp_list) > 1:
                conflicts.extend(emp_list)

        if not conflicts:
            return assignment  # Solution found
        
        # Select a random conflicting employee and reassign them
        employee = random.choice(conflicts)
        min_conflict_seat = min(preferences[employee], key=lambda s: len(seat_count[s]))
        assignment[employee] = min_conflict_seat

    return None  # No solution found

# Employees and seat preferences
employees = ["Alice", "Bob", "Charlie"]
seats = ["S1", "S2", "S3", "S4"]
preferences = {
    "Alice": ["S1", "S2"],
    "Bob": ["S2", "S3"],
    "Charlie": ["S3", "S4"]
}

# Run the Min-Conflicts Algorithm
solution = min_conflicts(employees, seats, preferences)
print(solution if solution else "No valid assignment found.")
