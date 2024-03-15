import time
import threading


def get_data(i, text):
    time.sleep(1)
    with open(f"data_{i}.txt", "w") as f:
        f.write(text)

start= time.time()

for i in range(1, 101):
    thread= threading.Thread(target=get_data, args=[i, f"Text{i}"])
    thread.start()
    thread.join

end= time.time()

print("time Elapsed: "+ str(end-start))