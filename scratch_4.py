import pickle
# ## create file object
# pickling_on = open("testing.data","wb") ## create new binary file
# ## write data into file
# pickle.dump(12.5, pickling_on)
# ## close file
# pickling_on.close()

## read pickled file
## create file object
pickle_off = open("ParkingLog_Feb-11-19.data", "rb")
## read
print(pickle.load(pickle_off))

# number = pickle.load(pickle_off)
# print(number)
## close
pickle_off.close()

