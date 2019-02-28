from operator import itemgetter
from math import ceil

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
    check_range = 200

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


def create_verts(photos_vert, photos):
    # group vertical photos in slides
    Vert = []
    for photo in photos_vert:
        Vert.append((photo.tag_num, photo.id))
    # Vert.sort(key = lambda x: x[0])             #sort slides
    Vert.sort(key=itemgetter(0), reverse=True)

    check_num = ceil(len(photos_vert) / 5)
    if check_num > 20:
        check_num = 20

    Slides = []
    while len(Vert) > 2:
        if check_num > len(Vert)-1:
            check_num =len(Vert) - 1
        pht = Vert[0]
        pht_tags = photos[pht[1]].tags
        Vert.remove(pht)
        maxnum = 0
        for i in range(check_num):
            # print(Vert[-i-1])
            temp = Vert[-i - 1]
            temp_tags = photos[temp[1]].tags
            s = len(pht_tags) + len(temp_tags) - 2 * len(list(set(pht_tags).intersection(temp_tags)))
            if maxnum < s:
                maxnum = s
                maxnumpht = temp
                maxnumpht_tags = temp_tags
        Vert.remove(maxnumpht)
        same_tags = pht_tags
        for tag in maxnumpht_tags:
            if tag not in same_tags:
                same_tags.append(tag)
        curr_slide = Slide(same_tags, pht[1], maxnumpht[1])
        Slides.append(curr_slide)
    if len(Vert) == 2:
        same_tags = photos[Vert[0][1]].tags
        for tag in photos[Vert[1][1]].tags:
            if tag not in same_tags:
                same_tags.append(tag)
        curr_slide = Slide(same_tags, Vert[0][1], Vert[1][1])
        Slides.append(curr_slide)

    return Slides


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
    #print(hori_mean)

    slides = create_verts(photos_vert, photos)
    for i in photos_hor:
        slides.append(Slide(i.tags, i.id))

    tosort = []
    for i in slides:
        tosort.append((len(i.tags),i))

    tosort.sort(key=itemgetter(0), reverse=True)
    sortedSlides = []
    for i in tosort:
        sortedSlides.append(i[1])

    # Sort Slides
    #slides = Sorted slides according to tags

    #print(getProjectedScore(slide1, slide2))
    cons, score = match_consecutive_slides(sortedSlides)
    #for sl in cons:
    #    print(sl)

    print('\n')
    print(len(cons))
    print(score)

    f = open("output.txt","w+")
    f.write(str(len(cons))+"\n")
    for i in cons:
        #s = print(i)
        f.write(str(i) + "\n")


    f.close()
    file.close()



if __name__ == "__main__": main()