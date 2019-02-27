
def main():
    #input_path = '/users/sammy/days.txt'
    #file = open(input_path, 'r')
    #file.read()    // read whole file
    #file.readline() // read a line one char at a time

    pizza = [[]]
    file = open("data.txt")
    input_args = file.readline()
    rows, cols, min_ingre, max_cells = input_args.strip().split(" ")


    data = file.readlines()
    for i, line in enumerate(data):
        pizza.append([])
        for item in line.split(" "):
            pizza[i].append(item.strip())
        # parse input, assign values to variables
        #player[key.strip()] = value.strip()

    file.close()




if __name__ == "__main__": main()
