import time
i=0
while True:
    i+=1
    with open("1.txt", "a") as myfile:
        myfile.write("07:51:52 Game over\n08:50:54 Input coin; total: 1\n08:50:54 Game started")
    with open("2.txt", "a") as myfile:
        myfile.write("07:51:52 Game over\n08:50:54 Input coin; total: 1\n08:50:54 Game started")
    with open("3.txt", "a") as myfile:
        myfile.write("07:51:52 Game over\n08:50:54 Input coin; total: 1\n08:50:54 Game started")
    with open("4.txt", "a") as myfile:
        myfile.write("07:51:52 Game over\n08:50:54 Input coin; total: 1\n08:50:54 Game started")
    with open("5.txt", "a") as myfile:
        myfile.write("07:51:52 Game over\n08:50:54 Input coin; total: 1\n08:50:54 Game started")
    with open("6.txt", "a") as myfile:
        myfile.write("07:51:52 Game over\n08:50:54 Input coin; total: 1\n08:50:54 Game started")
    print("ok"+str(i))
    time.sleep(60)