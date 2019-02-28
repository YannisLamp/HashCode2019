def main():
    input_path = 'data.txt'
    pizza = []
    file = open(input_path)
    input_args = file.readline()
    rows, cols, min_ingre, max_cells = input_args.strip().split(" ")

    data = file.readlines()
    for line in data:
        for item in line.strip().split(" "):
            pizza.append([c for c in item])

    file.close()
    print(pizza)

    #is_assigned = []
    #for line in pizza:
    #    is_assigned.append([])
    #    for cell in line:
    #        is_assigned[]

    Slice.pizza = pizza
    Slice.constraints = Constraints(rows, cols, min_ingre, max_cells)

    #for i in range(1, 6):
        #print(i)


if __name__ == "__main__": main()