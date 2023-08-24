N, M = map(int, input().split())

field = [[list(input())] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if field[i][j] == "R":
            red_position = (i, j)
        if field[i][j] == "B":
            blue_position = (i, j)

class B13459():
    def __init__(self, field, red_position: tuple, blue_position: tuple):
        self.field = field
        self.red, self.blue = red_position, blue_position

    def tilt(self):
        def right(rx, ry, bx, by, time_left):
            if not time_left:
                return False, False
            time_left-=1
            red, blue = False, False
            while field[rx+1][ry] != "#":
                if field[rx][ry] == "O":

                rx+=1
            while field[bx+1][by] != "#":
                if field[bx][by] == "O":
                bx+=1
            up(rx, ry, bx, by, time_left-1)
            down(rx, ry, bx, by, time_left-1)
            left(rx, ry, bx, by, time_left-1)

        def left(rx, ry, bx, by, time_left):
            if not time_left:
                return True, True
            time_left -= 1

            result_red, result_blue = True, True
            while field[rx-1][ry] != "#":
                if field[rx][ry] == "O":
                    result_red = False
                    rx -= 1
            while field[bx -1][by] != "#":
                if field[bx][by] == "O":
                    result_blue = False
                    bx -= 1
            up(rx, ry, bx, by, time_left-1)
            down(rx, ry, bx, by, time_left-1)
            right(rx, ry, bx, by, time_left-1)
        def up(rx, ry, bx, by, time_left):
            if not time_left:
                return True, True
            time_left -= 1

            result_red, result_blue = True, True
            while field[rx][ry+1] != "#":
                if field[rx][ry] == "O":
                    result_red = False
                    ry += 1
            while field[bx][by+1] != "#":
                if field[bx][by] == "O":
                    result_blue = False
                    by += 1
            down(rx, ry, bx, by, time_left - 1)
            left(rx, ry, bx, by, time_left - 1)
            right(rx, ry, bx, by, time_left - 1)
        def down(rx, ry, bx, by, time_left):
            if not time_left:
                return True, True
            time_left -= 1

            result_red, result_blue = True, True
            while field[rx][ry-1] != "#":
                if field[rx][ry] == "O":
                    result_red = False
                    ry -= 1
            while field[bx][by-1] != "#":
                if field[bx][by] == "O":
                    result_blue = False
                    by -= 1
            up(rx, ry, bx, by, time_left - 1)
            left(rx, ry, bx, by, time_left - 1)
            right(rx, ry, bx, by, time_left - 1)

        right(self.red, self.blue, 10)
        left(self.red, self.blue, 10)
        up(self.red, self.blue, 10)
        down(self.red, self.blue, 10)

if __name__ == "__main__":
    b13459 = B13459(field, red_position, blue_position)
    ret = False
    for i in range(10):
        red, blue = b13459.tilt()
        if blue == 0:
            continue
        if red == 1:
            ret = True
            break
    print(int(ret))