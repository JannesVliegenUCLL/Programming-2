# Write your code here
def format_time(hours, minutes, seconds):
    if hours <=9:
        hours=f'0{hours}'
    if minutes <=9:   
        minutes= f'0{minutes}'
    if seconds <= 9:
        seconds=f'0{seconds}'
    
    return f'{hours}:{minutes}:{seconds}'
        
