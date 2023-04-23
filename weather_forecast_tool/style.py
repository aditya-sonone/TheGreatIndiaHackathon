import pyfiglet as pfg

#function to print heading
def heading():
    print('''
 __          __           _    _                   ______                                  _      _____  _       _____ 
 \ \        / /          | |  | |                 |  ____|                                | |    / ____|| |     |_   _|
  \ \  /\  / /___   __ _ | |_ | |__    ___  _ __  | |__  ___   _ __  ___   ___  __ _  ___ | |_  | |     | |       | |  
   \ \/  \/ // _ \ / _` || __|| '_ \  / _ \| '__| |  __|/ _ \ | '__|/ _ \ / __|/ _` |/ __|| __| | |     | |       | |  
    \  /\  /|  __/| (_| || |_ | | | ||  __/| |    | |  | (_) || |  |  __/| (__| (_| |\__ \| |_  | |____ | |____  _| |_ 
     \/  \/  \___| \__,_| \__||_| |_| \___||_|    |_|   \___/ |_|   \___| \___|\__,_||___/ \__|  \_____||______||_____|
                                                                                                                       
                                                                                                                       
''')

#function to format temperature
def temperature(temp):
    a=str(temp)+" 'c"
    print(pfg.figlet_format(a, font="slant"))

#function to write city
def city(city_name):
    print(pfg.figlet_format(city_name.capitalize(), font="slant"))

