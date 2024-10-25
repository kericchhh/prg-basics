def time_string(hours, minutes, format):
    result = ''
    if minutes < 10 :
        final_minutes = f'0{minutes}'
    else :
        final_minutes = str(minutes)
    if format == '24':
        result = f'{hours}:{final_minutes}'
    elif format == '12':
        if hours > 12 : 
            result = f'{hours - 12}:{final_minutes} pm'
        else:
            result = f'{hours}:{final_minutes} am'
    else:
        result = f'Wrong Format'
    return result
print(f'The time for 15,38,24 is {time_string(15,38,'24')}')
print(f'The time for 0,5,24 is {time_string(0,5,'24')}')
print(f'The time for 11,12,12 is {time_string(12,15,'12')}')
print(f'The time for 1,55,24 is {time_string(1,55,'24')}')