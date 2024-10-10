import threading
import time
def generate_combinations(starting_barcode, num_digits, thread_count, output_file):
    def worker(start, end, result_list):
        for i in range(start, end):
            barcode = list(starting_barcode)
            increment = i
            for j in range(len(barcode) - num_digits, len(barcode)):
                barcode[j] = str((int(barcode[j]) + increment) % 10)
                increment //= 10
            result_list.append(''.join(barcode))

    threads = []
    results = [[] for _ in range(thread_count)]
    segment_size = (10 ** num_digits) // thread_count

    for i in range(thread_count):
        start = i * segment_size
        end = start + segment_size
        t = threading.Thread(target=worker, args=(start, end, results[i]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    with open(output_file, 'w') as f:
        for result in results:
            f.write('\n'.join(result) + '\n')

if __name__ == '__main__':
    starting_barcode = '915059319022437000000'
    num_digits = 6  # Number of digits to increment
    thread_count = 128
    output_file = 'barcode_combinations.txt'
    t1 = time.time()
    generate_combinations(starting_barcode, num_digits, thread_count, output_file)
    t2 = time.time()

    print("Time taken:", t2 - t1, "seconds")
