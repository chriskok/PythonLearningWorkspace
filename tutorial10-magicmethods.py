class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "{}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    def __add__(self, other_time):
        new_time = Time()

        # Add the seconds and correct if sum > 60
        if (self.second + other_time.second) >= 60:
            self.minute += 1
            new_time.second = (self.second + other_time.second) - 60
        else:
            new_time.second = self.second + other_time.second

        # Add the minutes and correct if sum > 60
        if (self.minute + other_time.minute) >= 60:
            self.hour += 1
            new_time.minute = (self.minute + other_time.minute) - 60
        else:
            new_time.minute = self.minute + other_time.minute

        # Add the hours and correct if sum > 24
        if (self.hour + other_time.hour) >= 24:
            new_time.hour = (self.hour + other_time.hour) - 24
        else:
            new_time.hour = self.hour + other_time.hour

        return new_time


def main():
    time1 = Time(1, 20, 30)
    print(time1)
    time2 = Time(24,41,30)
    print(time1 + time2)  # uses __add__


main()

# MANY MORE MAGIC METHODS:
# +	    object.__add__(self, other)
# -	    object.__sub__(self, other)
# *	    object.__mul__(self, other)
# //	object.__floordiv__(self, other)
# /	    object.__truediv__(self, other)
# %	    object.__mod__(self, other)
# **	object.__pow__(self, other[, modulo])
# <<	object.__lshift__(self, other)
# >>	object.__rshift__(self, other)
# &	    object.__and__(self, other)
# ^	    object.__xor__(self, other)
# |	    object.__or__(self, other)


