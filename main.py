def simulate_parallel_processing(num_threads, num_jobs, job_times):
    output = []
    threads = [0] * num_threads
    current_job = 0
    current_time = 0
    while current_job < num_jobs:
        for i in range(num_threads):
            if threads[i] == 0:
                threads[i] = job_times[current_job]
                output.append((i, current_time))
                current_job += 1
                if current_job == num_jobs:
                    break

        for i in range(num_threads):
            if threads[i] > 0:
                threads[i] -= 1

        current_time += 1

    return output


def main():
    num_threads, num_jobs = map(int, input().split())

    job_times = list(map(int, input().split()))

    result = simulate_parallel_processing(num_threads, num_jobs, job_times)

    for thread_num, start_time in result:
        print(thread_num, start_time)


if __name__ == "__main__":
    main()
