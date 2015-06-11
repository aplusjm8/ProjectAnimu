from sys import argv
import os

list=[]

def usage():
    print("Usage: " + argv[0] + " [-s/-e] " + "<animu name>")
          
def main():
    if len(argv) != 3:
        usage()
    elif argv[1] == "-s":
        search()
    elif argv[1] == "-e":
        editepisode()

def search():
    with open('animu.txt', 'r+') as inF:
        for line in inF:
            if argv[2] in line:
                list.append(line)
                print(list)
                if len(list) >= 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("More than one result found for search term '" + argv[2] + "'. Please choose one.")
                    for i in range(len(list)):
                        end = list[i].find("||") - 1
                        print("[" + str(i) + "] " + list[i][0:end])
                elif len(list) == 0:
                    print("No matches found")
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    name = line.find("||") -1
                    ep = line.find("||", name+2)
                    status = line.find("||", ep+2)
                    print(line[0:name] + "\n" + line[name+4:ep-1] + "\n" + line[ep+3:])
                    
def editepisode():
    with open('animu.txt', 'r+') as inF:
        for line in inF:
            if argv[2] in line:
                list.append(line)
                print(list)
                if len(list) >= 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("More than one result found for search term '" + argv[2] + "'. Please choose one.")
                    for i in range(len(list)):
                        end = list[i].find("||") - 1
                        print("[" + str(i) + "] " + list[i][0:end])
                elif len(list) == 0:
                    print("No matches found")
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    name = line.find("||") -1
                    ep = line.find("||", name+2)
                    status = line.find("||", ep+2)
                    print(line[0:name] + "\n" + line[name+4:ep-1] + "\n" + line[ep+3:] + "\n")
                    print("Would you like to edit this record?\n")
                    ans = raw_input("Edit? [Y/N]: ")
                    if ans == "y":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("[1]" + line[0:name] + "\n" + "[2]" + line[name+4:ep-1] + "\n" + "[3]" + line[ep+3:] + "\n")
                        ans2 = raw_input("What would you like to edit, [1], [2] or [3]: ")
                        if ans2 == "1":
                            print(line[0:name])
                        elif ans2 == "2":
                            print(line[name+4:ep-1])
                        elif ans2 == "3":
                            print(line[ep+3:])
                    else:
                        print("Invalid answer.. Exiting..")

main()