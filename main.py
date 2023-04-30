import time, random, keyboard


while True:
    random_int = random.randint(0000, 9999)
    print(random_int)
    time.sleep(0.85)
    if keyboard.is_pressed('a'):
        print("Program stopped by user")
        break