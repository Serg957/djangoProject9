# Использование %:
# Переменные: количество участников первой команды (team1_num).
team1_num = 5
print('В команде Мастера кода участников: %d !' % team1_num)
# Переменные: количество участников в обеих командах (team1_num, team2_num).
team2_num = 6
print('В команде Волшебники данных участников: %d !' % team2_num)
print('Итого сегодня в командах участников: %d и %d !' % (team1_num, team2_num))
# Использование format():
# Переменные: количество задач решённых командой 2 (score_2).
score1 = 40
score2 = 42
print('Команда Мастера кода решила задач: {0} !'.format(score1))
print('Команда Волшебники данных решила задач: {0} !'.format(score2))
# Переменные: время за которое команда 2 решила задачи (team1_time).
team1_time = 1552.512
team2_time = 2153.31451
print('Мастера кода решили задачи за {0} с !'.format(team1_time))
print('Волшебники данных решили задачи за {0} с !'.format(team2_time))
# Использование f-строк:
# Переменные: количество решённых задач по командам: score_1, score_2
print(f'Команды решили {score1} и {score2} задач.')
# Переменные: исход соревнования (challenge_result).
if team1_time < team2_time and score1 > score2 or score1 == score2:
    challenge_result = 'Победа команды Мастера кода!'
elif team2_time < team1_time and score1 < score2 or score1 == score2:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print(f'Результат битвы: {challenge_result}')
# Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
tasks_total = score1 + score2
time_avg = round((team1_time + team2_time) / tasks_total, 1)
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу')

