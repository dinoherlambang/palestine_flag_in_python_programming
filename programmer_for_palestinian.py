# heart symbols for each color in the flag
red = '❤️'
black = '🖤'
white = '🤍'
green = '💚'

# The Palestine flag logic
for y in range(11):
    if y < 4:
        print(red * (2*y+1) + black * (21-1*y))
    elif y == 4:
        print(red * (2*y+1) + white * (21-1*y))
    elif y == 5:        
        print(red * (2*y+1) + white * (21-1*(10-y)))
    elif y == 6:        
        print(red * (11-2*(y-5)) + white * (21-1*(10-y)))
    else:
        print(red * (11-2*(y-5)) + green * (21-1*(10-y)))
################### we never forget! ####################
########### we stand with people of Palestine ###########
# https://github.com/dinoherlambang/palestine_flag_in_python_programming.git
