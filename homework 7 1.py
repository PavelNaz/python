class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        for row in self.list:
            for x in row:
                print(f"{x:6}", end="")
            print()
        return ('\n'.join(map(str, self.list)))

    def __add__(self, other):
        for x in range(len(self.list)):
            for y in range(len(other.list[x])):
                self.list[x][y] = self.list[x][y] + other.list[x][y]
        return Matrix.__str__(self)

matrix_1 = Matrix([[-1, 0, 1], [-9, 0, 3], [10, 31, -14], [21, 31, -43], [13, 14, -13]])
matrix_2 = Matrix([[-2, 0, 2], [-7, 0, 5], [20, 22, -32], [24, 45, -64], [12, 12, -17]])
print(matrix_1.__add__(matrix_2))