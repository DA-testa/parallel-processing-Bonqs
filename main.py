def parallel_processing(num_threads, num_jobs, job_times):
    output = []
    threads = [0] * num_threads

    for i, job_time in enumerate(job_times):
        thread_index = threads.index(min(threads))
        output.append((thread_index, threads[thread_index]))
        threads[thread_index] += job_time

    return output

def main():
    num_threads = int(input())
    num_jobs = int(input())
    job_times = list(map(int, input().split()))

    results = parallel_processing(num_threads, num_jobs, job_times)

    for thread_index, start_time in results:
        print(f"Job assigned to thread {thread_index} at time {start_time} seconds")

if __name__ == "__main__":
    main()
