class Photo:
    def __init__(self, is_vertical, tag_num, tags):
        self.is_vertical = is_vertical
        self.tags = tags





def main():
    input_path = 'a_example.txt'
    file = open(input_path)
    input_arg = file.readline()
    photo_num = int(input_arg.strip())

    photos_vert = []
    photos_hor = []
    for i in range(photo_num):
        line_list = file.readline().strip().split(" ")
        tag_num = int(line_list[1])
        tags = [line_list[j] for j in range(2, tag_num + 2)]

        if line_list[0] == "V":
            is_vertical = True
            photos_vert.append(Photo(is_vertical, tag_num, tags))
        else:
            is_vertical = False
            photos_hor.append(Photo(is_vertical, tag_num, tags))


    file.close()

    #is_assigned = []
    #for line in pizza:
    #    is_assigned.append([])
    #    for cell in line:
    #        is_assigned[]

    #Slice.pizza = pizza
    #Slice.constraints = Constraints(rows, cols, min_ingre, max_cells)

    #for i in range(1, 6):
        #print(i)


if __name__ == "__main__": main()