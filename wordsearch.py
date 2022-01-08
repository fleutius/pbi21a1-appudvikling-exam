import time




def search_in():
    begin = time.time()
    with open("wordlist.txt") as f:
        
        if "lup" in f.read():
            print("korrekt")
        else: print("nej")
        end = time.time()
        print(f"Programmet tog {end - begin}")

search_in()