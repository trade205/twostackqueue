stackpush = []
stackpop = []

class TwoStackQueue(object):
	def add(num):
		stackpush.append(num)

	def poll(self):
		if len(stackpop) == 0 and len(stackpush) == 0:
			print("queue is empty")
        elif len(stackpop) == 0:
		    while len(stackpush) != 0:
			    stackpop.append(stackpush.pop())
		print(stackpop.pop())

new = TwoStackQueue()
new.poll()