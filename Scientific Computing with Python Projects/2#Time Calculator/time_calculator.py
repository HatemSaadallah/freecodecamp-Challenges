class Date:
	def __init__(self, start, duration):
		self.start = start
		self.duration = duration
		self.minute = 0
		self.second = 0
	def getHour(self):
		for numbers in self.start:
			if numbers == ':':
				self.hour = self.start[:self.start.index(numbers)]
				return self.start[:self.start.index(numbers)]

	def getMinute(self):
		for numbers in self.start:
			if numbers == ':':
				self.minute = self.start[self.start.index(numbers):self.start.index(numbers)+3]
				return self.start[self.start.index(numbers)+1:self.start.index(numbers)+3]

	def convert24(self):
		if "PM" in self.start:
			return str(int(self.getHour())+12) + ":" + self.getMinute()
	def convert12(self, date):
		return str(int(date.getHour())-12) + ":" + date.getMinute()

	

def add_time(start, duration, day=None):



	new_time = None



	return new_time

add_time("12:30 PM", "2:12")

newDate = Date("5:40 PM", "2:12")
print(newDate.getHour())
print(newDate.getMinute())

print(newDate.convert24())

