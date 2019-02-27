class Constraints:
    def __init__(self, rows, cols, min_ingre, max_cells):
        self.rows = rows
        self.y = cols
        self.min_ingre = min_ingre
        self.max_cells = max_cells


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #def distance:


class Slice:
    def __init__(self, x1, y1, x2, y2, pizza, constraints):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)

        #self.

    def calc_ingre(self):
        tom_num = 0
        mush_num = 0
        for i in range(min(self.p1.x, self.p2.x), max(self.p1.x, self.p2.x)):
            for j in range(min(self.p1.y, self.p2.y), max(self.p1.y, self.p2.y)):
                if self.pizza[i][j] == "T":
                    tom_num = tom_num + 1
                elif self.pizza[i][j] == "M":
                    mush_num = mush_num + 1

        return tom_num, mush_num

    def calc_total_cells(self):
        return abs(self.p1.x - self.p2.x) * (self.p1.y - self.p2.y)







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

    is_assigned = []
    for line in pizza:
        is_assigned.append([])
        for cell in line:
            is_assigned[]

    Slice.pizza = pizza
    Slice.constraints = Constraints(rows, cols, min_ingre, max_cells)

    #for i in range(1, 6):
        #print(i)


if __name__ == "__main__": main()