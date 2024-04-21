# Asyncio - Commanding CTUSS (Czech Technical University Space Station)

## Background Story:
Welcome aboard the CTUSS (Czech Technical University Space Station), where you are the newly appointed commander responsible for overseeing the daily operations and assigning tasks to the crew members. As the commander, you play a crucial role in ensuring the smooth functioning of the space station and the well-being of the crew.

Your task is to simulate the role of the spaceship commander by assigning various tasks to the crew members and tracking their progress. Each crew member has their own expertise and responsibilities, ranging from scientific research to maintenance and emergency response.


## Assignment description

You will be given list of tasks which needs to be finished. Each task is described as a tuple of responsible person, task name and amount of time required for the task to be finished.

```python
tasks = [
    ("Engineer", "System Monitoring", 3),
    ("Communications Officer", "Communication Management", 2),
]
```

As a commander you are supposed to order your crew to take care of these tasks and then await the confirmation from them that their respective task was finished. The entire communication must be collected and then provided at the end of the work day. All the logs need to follow up this structure:

Command log always starts with

```
COMMAND LOG START
```

Commander ordering a crew member to do some task. Format: `Commander: Issuing task '{task_name}' to {crew_member}`. For task `("Engineer", "System Monitoring", 3)` log will be as follows:

```
Commander: Issuing task 'System Monitoring' to Engineer
```

Crew member informing commander about finished task. Format: `{crew_member}: Task '{task_name}' completed`. For task `("Engineer", "System Monitoring", 3)` log will be as follows:
```
Engineer: Task 'System Monitoring' completed
```

Command log always ends with

```
COMMAND LOG END
```

For the mentioned set of tasks, the whole communication log will look like this:

```
COMMAND LOG START
Commander: Issuing task 'System Monitoring' to Engineer
Commander: Issuing task 'Communication Management' to Communications Officer
Communications Officer: Task 'Communication Management' completed
Engineer: Task 'System Monitoring' completed
COMMAND LOG END
```

Make sure that the output log is shown as described. Each task should run for the predefined amount of time and whole crew should work in parallel. Your solution will be checked mainly for two criteria:

1. log output follows the predefined structure
2. crew tasks are processed in parallel -> the time for finishing all the tasks is almost the same as time of the longest task 

Start from the template [ctuss_commander.py](./ctuss_commander.py). There is a function `commander_assigns_jobs` which will be called during the tests. In needs to return the command log and finish in the correct time. You are supposed fill in your solution into the template. Feel free to add your own functions and classes but don't break the predefined own.

## Important info

- `commander_assigns_jobs` is started as `asyncio.run()` and you will need to use `asyncio` to fulfill this task successfully
- use `asyncio.sleep()` to mock up the time of the work for each task
- there will be always only a single task for each crew member.
- don't import any other libraries otherwise you will be automatically assigned with 0 points
