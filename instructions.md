# Your Task
You are given a cybersecurity escape room project named:
Escape Room - Security Challenge: Path Traversal + Command Injection Chain
Your task is to create a simple command-line based escape room using Python. Your project should integrate two intentionally-vulnerable challenges Path Traversal and Command Injection. These challenges shall be chained so that information from the first challenge is required to beat the second challenge.
# Project Requirements
1. Create a Python based command-line escape room.
2. Integrate a Path Traversal challenge.
3. There should be a hidden file, location, password or clue which can be found using the first challenge.
4. The hidden clue should be used to navigate to the Command Injection challenge.
5. Integrate a Command Injection challenge.
6. There should be a final flag or reward after completing the challenge chain.
7. The project should run in an isolated Docker container or virtual machine.
The basic challenge flow should be:

Start Challenge → Path Traversal → Hidden Clue → Command Injection → Final Flag → Escape
# Evaluation
After creating the project, your escape room shall be evaluated using the given test cases.
The evaluation process will classify each test as:
            `Pass`
            `Fail`
The tests should validate:
1. The Path Traversal challenge is working.
2. The hidden clue can be found.
3. The hidden clue leads to the next challenge.
4. The Command Injection challenge is working.
5. The final flag can be obtained.
6. The game can be restarted correctly.
7. Unexpected input has no effect on the game outside the intended challenge.

# Required Output

Your project should produce or have:
Python source code
Challenge files
Docker/VM configuration
Test cases
Test results
Basic project documentation

The test results should clearly indicate if each test has passed or failed.

# Completion Criteria

Your project is complete when:

The escape room can be played from the terminal.
The Path Traversal challenge is working.
The hidden clue can be obtained.
The Command Injection challenge can be reached using the clue.
The final flag can be obtained.
The game can be restarted.
The project is running inside the isolated environment.
The required tests have been completed.