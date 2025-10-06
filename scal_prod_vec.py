n = int(input())
Q = list(map(int, input().split()))
C = list(map(int, input().split()))
A, B = map(int, input().split())

sum_Q = sum(Q)
sum_QC = sum(q * c for q, c in zip(Q, C))

if B == A:
    dot_product = A * sum_Q
else:
    dot_product = A * sum_Q + (B - A) * sum_QC / 255

print(int(dot_product))