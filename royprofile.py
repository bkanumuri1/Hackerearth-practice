# Hackerearth - Basic Programming - Input/Output - Basics of Input/Output - Roy and Profile Picture

L = int(input())
N = int(input())
for photos in range(N):
    W,H = input().split()
    W = int(W)
    H = int(H)
    if W<L or H<L :
        print("UPLOAD ANOTHER")
    elif W ==H :
        print("ACCEPTED")
    else:
        print("CROP IT")
