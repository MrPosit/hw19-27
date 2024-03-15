from multiprocessing import Pool
import time
import random


def save_data(i):
    with open (f"data{i}.txt", "w") as file:
        file.write(str(i))



start= time.time()
if __name__ == "__main__": 
    with Pool(processes=10) as pool:
        pool.map(save_data, [random.randint(1,1001) for i in range(1,1001)])
    
end= time.time()

print("time Elapsed multiprocessing: "+ str(end-start))