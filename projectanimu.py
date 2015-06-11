from sys import argv
import os

list=[]

def usage():
    print("Usage: " + argv[0] + " [-s/-e] " + "<animu name>")
          
def main():
    if len(argv) != 3:
        usage()
    elif argv[1] == "-s":
        with open('animu.txt', 'r') as inF:
            for line in inF:
                if argv[2] in line:
                    list.append(line)
            print(list)
            if len(list) >= 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("More than one result found for search term '" + argv[2] + "'. Please choose one.")
                for i in range(len(list)):
                    print("[" + str(i) + "] " + list[i])
                    
                

print argv[2]
os.system('cls' if os.name == 'nt' else 'clear')
main()