# SPECIFICATION:
#
# check_sudoku() determines whether its argument is a valid Sudoku
# grid. It can handle grids that are completely filled in, and also
# grids that hold some empty cells where the player has not yet
# written numbers.
#
# First, your code must do some sanity checking to make sure that its
# argument:
#
# - is a 9x9 list of lists
#
# - contains, in each of its 81 elements, an integer in the range 0..9
#
# If either of these properties does not hold, check_sudoku must
# return None.
#
# If the sanity checks pass, your code should return True if all of
# the following hold, and False otherwise:
#
# - each number in the range 1..9 occurs only once in each row 
#
# - each number in the range 1..9 occurs only once in each column
#
# - each number the range 1..9 occurs only once in each of the nine
#   3x3 sub-grids, or "boxes", that make up the board
#
# This diagram (which depicts a valid Sudoku grid) illustrates how the
# grid is divided into sub-grids:
#
# 5 3 4 | 6 7 8 | 9 1 2
# 6 7 2 | 1 9 5 | 3 4 8
# 1 9 8 | 3 4 2 | 5 6 7 
# ---------------------
# 8 5 9 | 7 6 1 | 4 2 3
# 4 2 6 | 8 5 3 | 7 9 1
# 7 1 3 | 9 2 4 | 8 5 6
# ---------------------
# 9 6 1 | 5 3 7 | 0 0 0
# 2 8 7 | 4 1 9 | 0 0 0
# 3 4 5 | 2 8 6 | 0 0 0
# 
# Please keep in mind that a valid grid (i.e., one for which your
# function returns True) may contain 0 multiple times in a row,
# column, or sub-grid. Here we are using 0 to represent an element of
# the Sudoku grid that the player has not yet filled in.

# check_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# check_sudoku should return True
hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]

import copy

def format_check(g):
    if not isinstance(g, list):
        return False
    if len(g) != 9:
        return False
    for row in g:
        if not isinstance(row, list):
            return False
        if len(row) != 9:
            return False
    return True

def range_check(g):
    for row in g:
        for col in row:
            if type(col) != int:
                return False
            if col < 0 or col > 9:
                return False
    return True

def transpose(g):
    t = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append(g[j][i])
        t.append(row)
    return t

def subblocks(g):
    t = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append(g[3 * (i/3) + j / 3][3 * (i%3) + j % 3])
        t.append(row)
    return t

def uniqness_check(g):
    for row in g:
        counts = [0] * 10
        for col in row:
            counts[col] += 1
        if max(counts[1:]) > 1:
            return False
    return True

def check_sudoku(grid):
    ###Your code here.
    if not (format_check(grid) and range_check(grid)):
        return None
    if not (uniqness_check(grid) and 
            uniqness_check(transpose(grid)) and
            uniqness_check(subblocks(grid))):
        return False
    return True

def check_sudoku2(g):
    """lightweight check_sudoku(), format checking skipped."""

    if not (uniqness_check(g) and 
            uniqness_check(transpose(g)) and
            uniqness_check(subblocks(g))):
        return False
    return True

def find_zeroes(g):
    zeroes = []
    for i in range(9):
        for j in range(9):
            if g[i][j] == 0:
                zeroes.append((i, j)) 
        
    return zeroes

def output(g):
    for row in g:
        print row

def solve_sudoku(g):
    r = check_sudoku(g)
    if r == True:
        return solve_main(g)
    else:
        print "illegal/invalid grid."
        return r

def solve_main(g):
        modified = True
        while modified:
            p = possibilities(g)
            print "we have %s spots to fill." % len(p)
            if len(p) == 0:
                print "no more spots to fill."
                if check_sudoku(g):
                    print "Found solution."
                    output(g)
                    return g
                else:
                    print "Invalid grid."
                    return False
            modified = False
            count = 0
            for (z, l) in p:
                if len(l) == 1:
                    print "spot %s must be %s" % (z, l[0])
                    g[z[0]][z[1]] = l[0]
                    count += 1
                    modified = True
            print "filled %s spots" % count
            if not check_sudoku2(g):
                print "resulted in invalid grid, unsolvable."
                return False
        print "there was no trivial spots to fill..guessing now"
        gresult = try_guesses(g)
        if check_sudoku(gresult):
            return gresult
        else:
            print "couldn't solve this grid."
            return False
        

def try_guesses(g):
    p = possibilities(g)
    p.sort(key=lambda(x): len(x[1]))
    print "guessing spot %s" % str(p[0][0])
    print "choices are %s" % p[0][1]
    for choice in p[0][1]:
        g1 = copy.deepcopy(g)
        g1[p[0][0][0]][p[0][0][1]] = choice
        r = solve_main(g1)
        if check_sudoku(r):
            return r
        elif r == False:
            continue
            

def possibilities(g):
    p = []
    zeroes = find_zeroes(g)
    for zero in zeroes:
        r = [g[zero[0]][j] for j in range(9) 
             if j != zero[1] and g[zero[0]][j] != 0]
        c = [g[i][zero[1]] for i in range(9) 
             if i != zero[0] and g[i][zero[1]] != 0]
        i0 = 3 * (zero[0] / 3)
        j0 = 3 * (zero[1] / 3)        
        b = [g[i0 + i1][j0 + j1] 
             for i1 in range(3) for j1 in range(3) 
             if (i0 + 11, j0 + j1) != zero and
             g[i0 + i1][j0 + j1] != 0]
        l = [n for n in range(1, 10)
             if (n not in r) and (n not in c) and (n not in b)]
        p.append((zero, l))
    return p
        

#print solve_sudoku(ill_formed) # --> None
#print solve_sudoku(valid)      # --> True
#print solve_sudoku(invalid)    # --> False
#print solve_sudoku(easy)       # --> True
print solve_sudoku(hard)       # --> True


subg = [[9,8,7,6,5,4,3,2,1],
        [8,7,6,5,4,3,2,1,9],
        [7,6,5,4,3,2,1,9,8],
        [6,5,4,3,2,1,9,8,7],
        [5,4,3,2,1,9,8,7,6],
        [4,3,2,1,9,8,7,6,5],
        [3,2,1,9,8,7,6,5,4],
        [2,1,9,8,7,6,5,4,3],
        [1,9,8,7,6,5,4,3,2]]

fpgd = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9, 5.5, 0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

fpgd2 = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9, 5., 0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

boolg = [[2,9,0,0, False, 0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

tupl  =[(2,9,0,0,0,0,0,7,0),
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# data = (subg, fpgd, fpgd2, boolg, tupl)
# for sudoku in data:
#     print check_sudoku(sudoku)

# print check_sudoku(None)
# print check_sudoku([])
# print check_sudoku([0])
# print check_sudoku([0] * 9)
# print check_sudoku([[]] * 9)
# print check_sudoku([[str(a) for a in b] for b in valid])
# print check_sudoku([[max(0.0, float(a) - 0.5) for a in b] for b in valid])

# # This last one can still be checkd, but you can call it invalid.
# print check_sudoku([[float(a) for a in b] for b in valid])
