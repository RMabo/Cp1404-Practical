from project import Project
import datetime

PROJECTS_FILE = "projects.txt"
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    """Project management program."""
    print(MENU)
    projects = []
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            projects = load_projects()
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid menu choice")

        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you for using custom-built project management software.")


def load_projects():
    """load projects from file."""
    try:
        projects = []
        with open(PROJECTS_FILE, "r") as file:  # open file
            lines = file.readlines()
            for line in lines[1:]:  # skip header line (first line)
                values = line.strip().split(',')
                name, start_date, priority, cost_estimate, completion_percentage = values  # unpack values
                projects.append([name, start_date, int(priority), float(cost_estimate), int(completion_percentage)])
        return projects
    except FileNotFoundError:
        print("No project file found.")
        return []


def save_projects(projects):
    """Save projects to file."""
    with open(PROJECTS_FILE, "w") as file:
        for project in projects:
            file.write(','.join(map(str, project)) + '\n')


def display_projects(projects):
    """Display projects."""
    print("Incomplete projects:")
    for i, project in enumerate(projects):
        if project[4] < 100:
            print(
                f"  {project[0]}, start: {project[1]}, priority {project[2]}, estimate: ${project[3]:.2f}, completion: {project[4]}%")
    print("Completed projects:")
    for i, project in enumerate(projects):
        if project[4] == 100:
            print(
                f" {project[0]}, start: {project[1]}, priority {project[2]}, estimate: ${project[3]:.2f}, completion: {project[4]}%")
    print(f"{get_number_of_completed_projects(projects)} projects are complete.")
    print(f"{len(projects) - get_number_of_completed_projects(projects)} projects are incomplete.")


def filter_projects(projects):
    """Filter projects."""
    try:
        start_date = datetime.datetime.strptime(input("Show projects that start after date (dd/mm/yy): "),
                                                "%d/%m/%Y")  # convert string to datetime object
        for project in projects:
            project_start_date = datetime.datetime.strptime(project[1], "%d/%m/%Y")  # convert string to datetime object
            if project_start_date >= start_date:
                print(
                    f"{project[0]}, start: {project[1]}, priority {project[2]}, estimate: ${project[3]:.2f}, completion: {project[4]}%")
    except ValueError:
        print("Invalid date.")


def add_project(projects):
    """Add project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = int(input("Percent complete: "))
    projects.append([name, start_date, priority, cost_estimate, completion_percentage])


def update_project(projects):
    """Update project."""
    for i, project in enumerate(projects):  # enumerate returns index and value
        print(
            f"{i} {project[0]}, start: {project[1]}, priority {project[2]}, estimate: ${project[3]:.2f}, completion: {project[4]}%")
    project_index = int(input("Project choice: "))
    if 0 <= project_index < len(projects):  # check if project_index is valid
        project = projects[project_index]
        print(
            f"{project[0]}, start: {project[1]}, priority {project[2]}, estimate: ${project[3]:.2f}, completion: {project[4]}%")
        new_completion_percentage = int(input("New Percentage: "))
        new_priority = input("New Priority: ")
        if new_priority:
            project[2] = int(new_priority)
        project[4] = new_completion_percentage  # update completion percentage
    else:
        print("Invalid project number.")


def sort_projects(projects):
    """Sort projects."""
    projects.sort(key=lambda x: x[1])  # sort by start date
    projects.sort(key=lambda x: x[2])  # sort by priority


def get_number_of_completed_projects(projects):
    """Get number of completed projects."""
    number_of_completed_projects = 0  # initialise counter
    for project in projects:  # iterate through projects
        if project[4] == 100:  # check if project is complete
            number_of_completed_projects += 1  # increment counter
    return number_of_completed_projects


main()
