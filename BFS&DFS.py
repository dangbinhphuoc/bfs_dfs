def tonTai(x, arr):
    for i in range(len(arr)):
        if(arr[i] == x):
            return True
    return False


def DFS(do_thi, bat_dau):
    O = [bat_dau]
    C = []
    while(len(O) != 0):
        S = O[0]
        C.append(S)
        O.pop(0)
        for i in range(len(do_thi) - 1, 0, -1):
            if(do_thi[S][i] == 1):
                if(tonTai(i, C) == False):
                    O.insert(0, i)
    return C

def BFS(do_thi, bat_dau):
    O = [bat_dau]
    C = []
    while(len(O) != 0):
        S = O[0]
        C.append(S)
        O.pop(0)
        for i in range(len(do_thi)):
            if(do_thi[S][i] == 1):
                if(tonTai(i, C) == False):
                    O.append(i)
    return C

def xuat(so_thanh_chu, du_lieu):
    for i in range(len(du_lieu)):
        print(so_thanh_chu[du_lieu[i]], end='')
        if(i<len(du_lieu)-1):
            print(' -> ', end='')



         # A  B  C  D  E  F  G  H  I  J  K  L  M  N  O
do_thi = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # A
          [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # B
          [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # C
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],  # D
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # E
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],  # F
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # G
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],  # H
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # I
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # J
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # K
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # L
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # M
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # N
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # O
          ]

so_thanh_chu = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

dfs = DFS(do_thi, 0)
xuat(so_thanh_chu, dfs)

print()
bfs = BFS(do_thi, 0)
xuat(so_thanh_chu, bfs)
