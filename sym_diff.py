_ , m = input(), input().split(" ")
_ , n = input(), input().split(" ")

ans = []

m_list = list(map(int, m))
n_list = list(map(int, n))

m_set = set(m_list)
n_set = set(n_list)

for x in m_set.difference(n_set):
    ans.append(x)
for x in n_set.difference(m_set):
    ans.append(x)

ans.sort()
for x in ans:
    print(x)



