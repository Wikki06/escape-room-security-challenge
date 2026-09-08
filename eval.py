import subprocess
import time
import csv
import os
import sys
TARGET = "/app/challenge/challenge.py"
FLAG = "FLAG{c4psul3_3sc4p3_r00m_c0mpl3t3d}"
def test():
    print("Escape room evaluation started")
    starting_time = time.time()
    solved_file="/app/challenge/.solved"
    if os.path.exists(solved_file):
        print("[+] Test Passed.")
        return True, "Challenge solved", 0.0
    else:
        print("[-] Test Failed. Challenge has not been solved.")
        return False, "Challenge not solved", 0.0
def traverse():
    result = subprocess.run(["python3", TARGET, "--read-file", "../../tmp/escape_room/clue.txt"],capture_output=True,text=True)
    return result.returncode == 0 and "CLUE_COMMAND=" in result.stdout
def command_injection():
    result = subprocess.run(["python3", TARGET, "--exec-clue", "hello; cat /app/flag.txt"],capture_output=True,text=True)
    return result.returncode == 0 and FLAG in result.stdout
def clue_find():
    result = subprocess.run(["python3", TARGET, "--read-file", "../../tmp/escape_room/clue.txt"],capture_output=True,text=True)
    return result.returncode == 0 and result.stdout.strip() == "CLUE_COMMAND=system_flag_dump"
def staging():
    result = subprocess.run(["python3", TARGET, "--exec-clue", "hello"],capture_output=True,text=True)
    return result.returncode == 0 and result.stdout.strip() == "hello"
def restart():
    result = subprocess.run(["python3", TARGET],capture_output=True,text=True)
    return result.returncode != 0
def unexpected_input():
    result = subprocess.run(["python3", TARGET, "--invalid", "test"],capture_output=True,text=True)
    return result.returncode == 0 and result.stdout.strip() == ""
def report_generation(results, duration):
    with open("results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Test_Name", "Status", "Execution_Time", "Notes"])
        for name, passed, notes in results:
            status = "PASS" if passed else "FAIL"
            writer.writerow([name, status, duration, notes])
    passed_count = sum(1 for _, passed, _ in results)
    total_count = len(results)
    if passed_count == total_count:
        summary_status = "PASS"
    else:
        summary_status = "FAIL"
    with open("summary.txt", "w") as f:
        f.write("Summary of the escape room evaluation\n")
        f.write(f"Final Result: {summary_status}\n")
        f.write(f"Tests Passed: {passed_count}/{total_count}\n")
        f.write(f"Execution Time: {duration} seconds\n")
    print("[+] Evaluation results are saved in results.csv and summary.txt")
if __name__ == "__main__":
    starting_time = time.time()
    results = []
    solved_passed, solved_notes, _ = test()
    results.append(("Final Flag / Solved State", solved_passed, solved_notes))
    path_passed = traverse()
    if path_passed:
        notes="Hidden file accessed"
    else:
        notes="Path traversal failed"
    results.append(("Path Traversal", path_passed, notes))
    clue_passed = clue_find()
    if clue_passed:
        notes="Correct clue found"
    else:
        notes="Clue not found"
    results.append(("Hidden Clue", clue_passed, notes))
    next_stage_passed = staging()
    if next_stage_passed:
        notes="Next stage reached"
    else:
        notes="Next stage failed"
    results.append(("Clue Leads to Next Stage", next_stage_passed, notes))
    injection_passed = command_injection()
    if injection_passed:
        notes="Injection successful"
    else:
        notes="Injection failed"
    results.append(("Command Injection", injection_passed, notes))
    restart_passed = restart()
    if restart_passed:
        notes="Invalid start rejected"
    else:
        notes="Unexpected behavior"
    results.append(("Restart/Input Handling", restart_passed, notes))
    unexpected_passed = unexpected_input()
    if unexpected_passed:
        notes="Unexpected input handled"
    else:
        notes="Unexpected input issue"
    results.append(("Unexpected Input", unexpected_passed, notes))
    for name, passed, notes in results:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}: {notes}")
    duration = round(time.time() - starting_time, 4)
    report_generation(results, duration)
    if all(passed for _, passed, _ in results):
        sys.exit(0)
    else:
        sys.exit(1)