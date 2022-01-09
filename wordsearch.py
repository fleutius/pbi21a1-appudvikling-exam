import time
import bisect

words = ["Jens","Peter","Anders","Frank","Fiddo","Karsten","Mark","Eddie","Gorm","Christian","Didrik"]
x = "Peter"

def search_in(x):
    begin = time.perf_counter_ns()
    if x in words:
        print("korrekt")
    else: print("nej")
    end = time.perf_counter_ns()
    print(f"Programmet tog {end - begin} nanosekunder")


def bi_find(x):
    a = sorted(words)
    begin = time.perf_counter_ns()
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        print(f"{x} Findes på index: {i}")
    else: 
        print(x, "er fraværende")
    end = time.perf_counter_ns()
    print(f"Programmet tog {end - begin} nanosekunder")


search_in(x)
bi_find(x)
