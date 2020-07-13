# Hackerearth - Basic Programming - Input/Output - Basics of Input/Output - Cost of Balloons

print("Hello there!")

t = int(input())
for testcase in range(t):
    cost1, cost2 = 0 , 0
    #cost2 = 0
    g_cost,p_cost = input().split()
    g_cost = int(g_cost)
    p_cost = int(p_cost)
    n = int(input())
    for participant in range(n):
        first, second = input().split()
        first = int(first)
        second = int(second)
        cost1 += first*g_cost + second*p_cost
        cost2 += first*p_cost + second*g_cost
    print(min(cost1,cost2))
        
    
