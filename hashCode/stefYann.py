class Photo:
    def __init__(self, is_vertical, tags):
        self.is_vertical = is_vertical
        self.tags = tags





def main():
    input_path = 'data.txt'
    pizza = []
    file = open(input_path)
    input_arg = file.readline()
    photo_num = int(input_arg.strip())

    for i in range(photo_num):
        line_list = file.readline().strip().split(" ")
        if line_list[0] == "V":
            is_vertical = True
        else:
            is_vertical = False

        tag_num = int(line_list[1])

        for j in range(tag_num):
            


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