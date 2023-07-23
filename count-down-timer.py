import time

my_time = int(input("Enter a time in seconds: "))

for x in (range(my_time, 0, -1)):
    print(x)
    time.sleep(1)

print("TIMES UP!")
