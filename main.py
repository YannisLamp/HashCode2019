
def main():
    #input_path = '/users/sammy/days.txt'
    #file = open(input_path, 'r')
    #file.read()    // read whole file
    #file.readline() // read a line one char at a time

    player = {}
    f = open("data.txt")
    data = f.readlines()
    for line in data:
        # parse input, assign values to variables
        key, value = line.split(":")
        player[key.strip()] = value.strip()
    f.close()








if __name__ == "__main__": main()
