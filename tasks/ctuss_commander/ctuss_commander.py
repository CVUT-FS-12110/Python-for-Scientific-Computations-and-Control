import asyncio
import time


""" vvvv YOUR CODE STARTS HERE vvvv """

# Add other functions, classes ... as you need


async def commander_assigns_jobs(tasks):

    # Fill in the function

    """ ^^^^ YOUR CODE ENDS HERE ^^^^ """
    return command_log


if __name__ == "__main__":
    # List of tasks assigned by the spaceship commander
    tasks = [
        ("Engineer", "System Monitoring", 3),
        ("Communications Officer", "Communication Management", 2),
    ]

    print("Scenario 1 - Started")
    s = time.perf_counter()
    assert asyncio.run(commander_assigns_jobs(tasks)) == "COMMAND LOG START\nCommander: Issuing task 'System Monitoring' to Engineer\nCommander: Issuing task 'Communication Management' to Communications Officer\nCommunications Officer: Task 'Communication Management' completed\nEngineer: Task 'System Monitoring' completed\nCOMMAND LOG END"
    elapsed = time.perf_counter() - s
    print("Scenario 1 - Log Correct")
    assert 2.5 < elapsed < 3.5
    print("Scenario 1 - Time is Correct")
    print("Scenario 1 - Successfully finished")

    tasks = [
        ("Engineer", "System Monitoring", 3),
        ("Environmental Specialist", "Environmental Control", 11),
        ("Scientist", "Experiment Conduction", 5),
        ("Astronaut", "Spacewalk Assistance", 7),
        ("Medic", "Emergency Response", 9),
        ("Navigator", "Navigation and Guidance", 10),
        ("Technician", "Maintenance and Repair", 4),
        ("Communications Officer", "Communication Management", 2),
        ("Researcher", "Data Analysis", 8),
        ("Logistics Officer", "Resource Management", 6),
    ]

    print("Scenario 2 - Started")
    s = time.perf_counter()
    assert asyncio.run(commander_assigns_jobs(tasks)) == "COMMAND LOG START\nCommander: Issuing task 'System Monitoring' to Engineer\nCommander: Issuing task 'Environmental Control' to Environmental Specialist\nCommander: Issuing task 'Experiment Conduction' to Scientist\nCommander: Issuing task 'Spacewalk Assistance' to Astronaut\nCommander: Issuing task 'Emergency Response' to Medic\nCommander: Issuing task 'Navigation and Guidance' to Navigator\nCommander: Issuing task 'Maintenance and Repair' to Technician\nCommander: Issuing task 'Communication Management' to Communications Officer\nCommander: Issuing task 'Data Analysis' to Researcher\nCommander: Issuing task 'Resource Management' to Logistics Officer\nCommunications Officer: Task 'Communication Management' completed\nEngineer: Task 'System Monitoring' completed\nTechnician: Task 'Maintenance and Repair' completed\nScientist: Task 'Experiment Conduction' completed\nLogistics Officer: Task 'Resource Management' completed\nAstronaut: Task 'Spacewalk Assistance' completed\nResearcher: Task 'Data Analysis' completed\nMedic: Task 'Emergency Response' completed\nNavigator: Task 'Navigation and Guidance' completed\nEnvironmental Specialist: Task 'Environmental Control' completed\nCOMMAND LOG END"
    elapsed = time.perf_counter() - s
    print("Scenario 2 - Log Correct")
    assert 10.5 < elapsed < 11.5
    print("Scenario 2 - Time is Correct")
    print("Scenario 2 - Successfully finished")
