import datetime
now = datetime.datetime.now()
print ("It is {0}:{1}:{2}".format(now.hour, now.minute, now.second))

print(now.hour)

due_time = datetime.time(7, 0, 0)
print(due_time)
