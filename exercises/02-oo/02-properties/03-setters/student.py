class Time:
    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    @hours.setter
    def hours(self, value):
        if value not in range(0,24):
            raise ValueError("Hours must be in range of 0-24")
        self.__hours = value

    @minutes.setter
    def minutes(self, value):
        if value not in range(0,59):
            raise ValueError("Minutes must be between 0-60")
        self.__minutes = value

    @seconds.setter
    def seconds(self, value):
        if value not in range(0,59):
            raise ValueError("Minutes must be in between 0-60")
        self.__seconds=value


