def main_function():
    print("Hello welcome to investing")

def user_input():
    # create dictionary to store info
    list = {}
    while(True):
        print('Enter your ticker symbol and amount:')
        x = input()
        if(input == 'Exit'):
            break
        else:
            val = x.split(" ")
            list[val[0]] = val[1]

# dividend

# growth
# time until millionaire estimate