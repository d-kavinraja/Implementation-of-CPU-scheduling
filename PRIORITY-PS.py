def priority_preemptive(processes, burst_time, priorities):
    n = len(processes)
    remaining_time = list(burst_time)  # Initialize remaining time for each process
    completion_time = [0] * n
    current_time = 0

    while True:
        highest_priority = None
        for i in range(n):
            if remaining_time[i] > 0:
                if highest_priority is None or priorities[i] < priorities[highest_priority]:
                    highest_priority = i

        if highest_priority is None:
            break

        remaining_time[highest_priority] -= 1
        current_time += 1

        if remaining_time[highest_priority] == 0:
            completion_time[highest_priority] = current_time

    waiting_time = [0] * n
    turnaround_time = [0] * n

    for i in range(n):
        turnaround_time[i] = completion_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]

    average_waiting_time = sum(waiting_time) / n
    average_turnaround_time = sum(turnaround_time) / n

    print("Process\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t{burst_time[i]}\t\t{priorities[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"Average Waiting Time: {average_waiting_time}")
    print(f"Average Turnaround Time: {average_turnaround_time}")

# Example usage:
if __name__ == "__main__":
    processes = ['P1', 'P2', 'P3', 'P4']
    burst_time = [5, 9, 3, 7]
    priorities = [2, 1, 3, 4]
    priority_preemptive(processes, burst_time, priorities)
