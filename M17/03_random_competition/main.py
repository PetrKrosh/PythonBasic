import random
f_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
s_team = [round(random.uniform(5, 10), 2) for _ in range(20) ]
# t_team = []

# for i in range(len(f_team)):
# 	if f_team[i] > s_team[i]:
# 		t_team.append(f_team[i])
# 	else:
# 		t_team.append(s_team[i])

t_team = [f_team[i] if f_team[i] > s_team[i] else s_team[i] for i in range(len(f_team))]

print('Первая команда: ', f_team)
print('Вторая команда: ', s_team)
print('Победители тура: ', t_team)
