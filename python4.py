


# Example
processes = [
    Process("P1", arrival_time=0, burst_time=7, priority=3),
    Process("P2", arrival_time=1, burst_time=4, priority=5),
    Process("P3", arrival_time=2, burst_time=2, priority=1),
    Process("P4", arrival_time=3, burst_time=5, priority=2),
]

order = dynamic_priority_scheduler(processes, aging_rate=1)

print("Execution order:")
print(" -> ".join(order))

print("\nProcess statistics:")
for p in processes:
    print(
        f"{p.pid}: "
        f"Completion={p.completion_time}, "
        f"Waiting={p.waiting_time}"
    )




