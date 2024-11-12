from project import Project

def load_projects(file_name):
    projects = []
    with open(file_name, "r") as file:
        next(file)  # Skip the header line
        for line in file:
            line = line.strip()
            if line:
                name, start_date, priority, cost_estimate, completion_percentage = line.split("\t")
                project = Project(name, start_date, priority, cost_estimate, completion_percentage)
                projects.append(project)
    return projects

def save_projects(file_name, projects):
    with open(file_name, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")

def display_projects(projects):
    incomplete_projects = [project for project in projects if not project.is_completed()]
    completed_projects = [project for project in projects if project.is_completed()]

    print("Incomplete Projects:")
    for project in incomplete_projects:
        print(project)

    print("\nCompleted Projects:")
    for project in completed_projects:
        print(project)

def filter_projects_by_date(projects):
    date_str = input("Enter a start date (dd/mm/yyyy): ")
    try:
        date = datetime.strptime(date_str, "%d/%m/%Y")
    except ValueError:
        print("Invalid date format. Please enter a date in the format dd/mm/yyyy.")
        return

    filtered_projects = [project for project in projects if project.start_date > date]
    filtered_projects.sort(key=lambda project: project.start_date)

    print("Filtered Projects:")
    for project in filtered_projects:
        print(project)

def add_new_project(projects):
    name = input("Enter the project name: ")
    start_date = input("Enter the start date (dd/mm/yyyy): ")
    priority = input("Enter the priority: ")
    cost_estimate = input("Enter the cost estimate: ")
    completion_percentage = input("Enter the completion percentage: ")

    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)
    print("Project added successfully.")

def update_project(projects):
    print("Select a project to update:")
    for index, project in enumerate(projects):
        print(f"{index + 1}. {project}")

    try:
        project_index = int(input("Enter the project number: ")) - 1
        if project_index < 0 or project_index >= len(projects):
            print("Invalid project number.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    project = projects[project_index]

    completion_percentage = input("Enter the new completion percentage (leave blank to retain existing value): ")
    if completion_percentage:
        project.completion_percentage = int(completion_percentage)

    priority = input("Enter the new priority (leave blank to retain existing value): ")
    if priority:
        project.priority = int(priority)

    print("Project updated successfully.")

def main():
    file_name = "projects.txt"
    projects = load_projects(file_name)

    while True:
        print("\nMenu:")
        print("1. Load projects")
        print("2. Save projects")
        print("3. Display projects")
        print("4. Filter projects by date")
        print("5. Add new project")
        print("6. Update project")
        print("0. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            file_name = input("Enter the file name to load projects from: ")
            projects = load_projects(file_name)
        elif choice == "2":
            file_name = input("Enter the file name to save projects to: ")
            save_projects(file_name, projects)
            print("Projects saved successfully.")
        elif choice == "3":
            display_projects(projects)
        elif choice == "4":
            filter_projects_by_date(projects)
        elif choice == "5":
            add_new_project(projects)
        elif choice == "6":
            update_project(projects)
        elif choice == "0":
            save_choice = input("Do you want to save the projects to the default file (projects.txt)? (y/n): ")
            if save_choice.lower() == "y":
                save_projects(file_name, projects)
                print("Projects saved successfully.")
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")

if __name__ == "__main__":
    main()