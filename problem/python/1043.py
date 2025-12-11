n, m = map(int, input().split())
truth = list(map(int, input().split()))
truth_num = truth[0]
truth_people = set(truth[1:]) if truth_num > 0 else set()

parties = []
for _ in range(m):
    party = list(map(int, input().split()))
    parties.append(set(party[1:]))

for _ in range(m):
    for party in parties:
        if party & truth_people:
            truth_people = truth_people | party

count = 0
for party in parties:
    if not party & truth_people:
        count += 1

print(count)
