import datetime
start = datetime.datetime.now()
for i in range(1,10000):
    print("test")

end = datetime.datetime.now()

print(end-start)
