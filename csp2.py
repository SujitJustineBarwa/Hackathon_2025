import random

def min_conflicts(employees, seats, preferences, max_iterations=100):
    # Step 1: Random Initial Assignment based on Preferences
    assignment = {e: random.choice(preferences[e]) for e in employees}

    for _ in range(max_iterations):
        # Step 2: Detect Conflicts (Multiple Employees Assigned to Same Seat)
        conflicts = []
        seat_count = {s: [] for s in seats}
        
        for e, s in assignment.items():
            seat_count[s].append(e)

        # Identify conflicting employees (who share a seat)
        for s, emp_list in seat_count.items():
            if len(emp_list) > 1:
                conflicts.extend(emp_list)

        # If no conflicts, return solution
        if not conflicts:
            print(assignment)
            print()
            return assignment

        # Step 3: Resolve Conflict for a Random Conflicting Employee
        employee = random.choice(conflicts)
        possible_seats = preferences[employee]

        # Find the seat with the least conflicts
        min_conflict_seat = min(possible_seats, key=lambda s: len(seat_count[s]))
        
        # Reassign the employee to the new seat
        assignment[employee] = min_conflict_seat

    return None  # No valid assignment found within max_iterations

# Employees and seats
employees = ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9"]
seats = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9"]

# Seat preferences (some prefer corner seats: S1, S3, S7, S9)
preferences = {
    "E1": ["S1", "S2"],  # Prefers corner seat S1
    "E2": ["S2", "S3"],  
    "E3": ["S3", "S6"],  # Prefers corner seat S3
    "E4": ["S4", "S5"],  
    "E5": ["S5", "S6"],  
    "E6": ["S6", "S9"],  # Prefers corner seat S9
    "E7": ["S7", "S8"],  # Prefers corner seat S7
    "E8": ["S8", "S5"],  
    "E9": ["S9", "S4"],  # Prefers corner seat S9
}

# Reinforce corner seat preferences
corner_seats = ["S1", "S3", "S7", "S9"]
corner_pref_employees = ["E1", "E3", "E6", "E7", "E9"]

for emp in corner_pref_employees:
    preferences[emp] = [s for s in corner_seats if s in preferences[emp]] + preferences[emp]

# Run Min-Conflicts CSP
solution = min_conflicts(employees, seats, preferences)

# Output the seat assignments
if solution:
    print("Final Seat Assignments:")
    for emp, seat in solution.items():
        print(f"{emp} -> {seat}")
else:
    print("No valid assignment found.")
