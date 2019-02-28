

class Photo:
    def __init__(self, is_vertical, tag_num, tags, id):
        self.is_vertical = is_vertical
        self.tag_num = tag_num
        self.tags = tags
        self.id = id

    def __str__(self):
        return str(self.is_vertical)


class Slide:
    def __init__(self, tags, id1, id2=None):
        self.tags, self.id1 = tags, id1
        if id2:
            self.id2 = id2
        else:
            self.id2 = None

    def __str__(self):
        s = str(self.id1)
        if not self.id2:
            return s
        else:
            return s + " " + str(self.id2)


def find_horizontal_mean(photos_hor):
    hori_sum = 0
    for photo in photos_hor:
        hori_sum += photo.tag_num

    return hori_sum / len(photos_hor)


def match_consecutive_slides(slides):
    presentation = []
    total_score = 0
    #check_range = len(slides)
    check_range = 1000

    #while len(presentation) < len(slides):
    presentation.append(slides[0])
    last_slide = slides[0]
    del slides[0]
    while len(slides) > 0:
        max_score = 0
        max_score_i = 0
        for i in range( min(check_range, len(slides)) ):
            score = getProjectedScore(last_slide, slides[i])
            if score > max_score:
                max_score = score
                max_score_i = i

        total_score = total_score + max_score
        presentation.append(slides[max_score_i])
        last_slide = slides[max_score_i]
        del slides[max_score_i]

    return presentation, total_score


def getProjectedScore(slide1, slide2):
    common = len(list(set(slide1.tags).intersection(slide2.tags)))
    return min(common, (len(slide1.tags) - common), (len(slide2.tags)-common))



def main():
    input_path = 'd_pet_pictures.txt'
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


    # Sort Slides
    #slides = Sorted slides according to tags
    slides = []
    for i in photos_hor:
        slides.append(Slide(i.tags, i.id))
    #slide1 = Slide(["cat", "dog", "sun", "aaa"], 0)
    #slide2 = Slide(["dog", "april", "sun", "Aaaa"], 1)


    #print(getProjectedScore(slide1, slide2))
    cons, score = match_consecutive_slides(slides)
    #for sl in cons:
    #    print(sl)

    print('\n')
    print(len(cons))
    print(score)

    file.close()
    #for i in photos:
    #    print(i)




if __name__ == "__main__": main()