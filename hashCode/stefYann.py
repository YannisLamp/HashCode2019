class Photo:
    def __init__(self, is_vertical, tag_num, tags, id):
        self.is_vertical = is_vertical
        self.tag_num = tag_num
        self.tags = tags
        self.id = id

    def __str__(self):
        return str(self.is_vertical)


def find_horizontal_mean(photos_hor):
    hori_sum = 0
    for photo in photos_hor:
        hori_sum += photo.tag_num

    return hori_sum / len(photos_hor)






def main():
    input_path = 'a_example.txt'
    file = open(input_path)
    input_arg = file.readline()
    photo_num = int(input_arg.strip())

    photos = []
    photos_vert = []
    photos_hor = []
    for i in range(photo_num):  # i is id
        line_list = file.readline().strip().split(" ")
        tag_num = int(line_list[1])
        tags = [line_list[j] for j in range(2, tag_num + 2)]

        if line_list[0] == "V":
            is_vertical = True
        else:
            is_vertical = False

        curr_photo = Photo(is_vertical, tag_num, tags, i)
        photos.append(curr_photo)
        if line_list[0] == "V":
            photos_vert.append(curr_photo)
        else:
            photos_hor.append(curr_photo)


    hori_mean = find_horizontal_mean(photos_hor)
    print(hori_mean)

    file.close()
    for i in photos:
        print(i)




if __name__ == "__main__": main()