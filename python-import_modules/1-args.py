import sys 

def main():
    argv = sys.argv[1:]  #Exclude the script name from the arguments
    num_args = len(argv)

    if num_args == 0:
        print("Number of arguments: 0.")
    else:
        print("Number of arguments:", num_args, ":", end="\n\n") 
        for i, arg in enumerate(argv, start=1):
            print("Argument {}:".format(i), arg)

if __name__ == "__main__":   
    main()           
    