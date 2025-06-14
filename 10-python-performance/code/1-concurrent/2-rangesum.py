import time 
import concurrent.futures
WORKERS=4

def sum_list(thelist:list):
	s = 0
	for x in thelist:
		s += x**3//10
	return s

LISTSIZE = 10000000

def sequential():
    start = time.perf_counter()
    big_sum=sum_list(range(0,LISTSIZE))
    print(f"Sequential: sum={big_sum}, time={time.perf_counter()-start} sec")

def threads():
    start = time.perf_counter()
    parts = [
         range(0,LISTSIZE//4), 
         range(LISTSIZE//4,LISTSIZE//2), 
         range(LISTSIZE//2,3*LISTSIZE//4), 
         range(3*LISTSIZE//4,LISTSIZE)
         ]
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as executor:
        partial_results = executor.map(sum_list, parts)
        pr = list(partial_results)
        big_sum = sum(pr)
    print(f"{WORKERS} threads: partial_results={pr}, sum={big_sum}, time={time.perf_counter()-start} sec")

def processes():
    start = time.perf_counter()
    parts = [
         range(0,LISTSIZE//4), 
         range(LISTSIZE//4,LISTSIZE//2), 
         range(LISTSIZE//2,3*LISTSIZE//4), 
         range(3*LISTSIZE//4,LISTSIZE)
         ]
    with concurrent.futures.ProcessPoolExecutor(max_workers=WORKERS) as executor:
        partial_results = executor.map(sum_list, parts)
        pr = list(partial_results)
        big_sum = sum(pr)
    print(f"{WORKERS} processes: partial_results={pr}, sum={big_sum}, time={time.perf_counter()-start} sec")


if __name__ == '__main__':
    sequential()
    threads()
    processes()
