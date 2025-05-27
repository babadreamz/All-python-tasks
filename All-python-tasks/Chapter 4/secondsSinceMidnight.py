def seconds_since_midnight(hour, minute, seconds):
	hour_in_seconds = hour * 60 * 60
	minute_in_seconds = minute * 60
	seconds_in = hour_in_seconds + minute_in_seconds + seconds
	return seconds_in


hrs = int (input('enter the hours: '))
mins = int (input('enter the minutes: '))
secs = int (input('enter the seconds: '))
print(seconds_since_midnight(hrs, mins, secs))