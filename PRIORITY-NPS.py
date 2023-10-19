def priority_non_preemptive(processes, burst_time, priorities):
    n = len(processes)
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0

    # Create a list of tuples containing process information
    process_info = [(processes[i], burst_time[i], priorities[i]) for i in range(n)]

    # Sort the processes based on their priorities (lower values indicate higher priority)
    process_info.sort(key=lambda x: x[2])

    # Calculate completion times, waiting times, and turnaround times
    completion_time[0] = process_info[0][1]
    for i in range(1, n):
        completion_time[i] = completion_time[i - 1] + process_info[i][1]
    
    for i in range(n):
        turnaround_time[i] = completion_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]

    # Calculate the average waiting time and average turnaround time
    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    # Print the results
    print("Process\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{process_info[i][0]}\t{process_info[i][1]}\t\t{process_info[i][2]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"Average Waiting Time: {average_waiting_time}")
    print(f"Average Turnaround Time: {average_turnaround_time}")

# Example usage:
if __name__ == "__main__":
    processes = ['P1', 'P2', 'P3', 'P4']
    burst_time = [8, 6, 1, 9]
    priorities = [2, 1, 3, 4]
    priority_non_preemptive(processes, burst_time, priorities)