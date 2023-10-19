def sjf_non_preemptive(processes, burst_time):
    n = len(processes)

    # Sort processes based on their burst times
    for i in range(n):
        for j in range(0, n - i - 1):
            if burst_time[j] > burst_time[j + 1]:
                processes[j], processes[j + 1] = processes[j + 1], processes[j]
                burst_time[j], burst_time[j + 1] = burst_time[j + 1], burst_time[j]

    # Calculate waiting time for each process
    waiting_time = [0] * n
    waiting_time[0] = 0

    for i in range(1, n):
        waiting_time[i] = burst_time[i - 1] + waiting_time[i - 1]

    # Calculate turnaround time for each process
    turnaround_time = [0] * n
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_time[i]

    # Calculate the average waiting time and average turnaround time
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)
    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    # Print the results
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"Average Waiting Time: {average_waiting_time}")
    print(f"Average Turnaround Time: {average_turnaround_time}")


# Example usage:
if __name__ == "__main__":
    processes = ['P1', 'P2', 'P3', 'P4', 'P5']
    burst_time = [6, 8, 7, 3, 2]
    sjf_non_preemptive(processes, burst_time)

