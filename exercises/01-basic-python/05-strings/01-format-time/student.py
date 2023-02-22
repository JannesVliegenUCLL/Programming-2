# Write your code here
def format_time(hours, minutes, seconds):
    if len(hours) == 1:
        hours=f'0{hours}'
    if len(minutes) == 1:
