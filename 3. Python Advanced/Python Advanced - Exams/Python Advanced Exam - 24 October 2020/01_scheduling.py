jobs = [int(n) for n in input().split(", ")]
index = int(input())

clock_cycles = 0
job = jobs[index]

while job in jobs:
    min_job = min(jobs)
    jobs.remove(min_job)
    clock_cycles += min_job

print(clock_cycles)
