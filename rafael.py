from math import floor

def get_slice(y1, x1, y2, x2, pizza):
    return [cell[x1:x2+1] for cell in pizza[y1:y2+1]]

def main():
    #input_path = '/users/sammy/days.txt'
    #file = open(input_path, 'r')
    #file.read()    // read whole file
    #file.readline() // read a line one char at a time

    pizza = []
    file = open("data.txt")
    input_args = file.readline()
    rows, cols, min_ingre, max_cells = input_args.strip().split(" ")
    nrows=int(rows)
    ncols=int(cols)
    nmin_ingre=int(min_ingre)
    nmax_cells=int(max_cells)

    data = file.readlines()
    for line in data:
        for item in line.strip().split(" "):
            #pizza[i].append(item.strip())
            pizza.append([c for c in item])

        # parse input, assign values to variables
        #player[key.strip()] = value.strip()

    file.close()
    Tom_num=0
    Mush_num=0
    for line in pizza:
        Tom_num+=line.count('T')
        Mush_num+=line.count('M')

    max_slices=floor(min(Tom_num,Mush_num)/int(min_ingre))

    for line in pizza:
        print (line)

    print("\n");print("\n")

    slice=get_slice(0,2,2,2,pizza)
    for line in slice:
        print (line)



if __name__ == "__main__": main()
