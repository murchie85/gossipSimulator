import time
import sys

def med_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)

#  this will print a messages for a given time.
#  it counts down a timer to keep printing message
def printNotification(message, messageTime):
	if message == "":
		return('free',messageTime)

	if messageTime >= 0:
		print(message)
		messageTime -=1
		return('running',messageTime)

	if messageTime < 0:
		return('free',messageTime)