#parse and print using pretty print

import sys
import re
from prettytable import PrettyTable

def read_file():
    
    #check that a file name is given in the command line
    if len(sys.argv) < 2:
        print("Error: Enter a file name")
        sys.exit(1)

    all_events = []

    for filename in sys.argv[1:]:
        #open the file (or attempt to)
        try:
            with open(filename, 'r') as file:
                process(file)
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    

def process(file):
    
    for line in file:
        line = line.strip()
        new_line = ''
        prev = ' '
        for my_char in line:
            if prev == ' ':
                new_line += my_char
            elif prev == '(':
                new_line += my_char
            elif my_char != ' ':
                new_line += my_char.lower()
            else:
                new_line += ' '
            prev = my_char
        print(new_line)
    return
   

if __name__ == "__main__":
    read_file()

