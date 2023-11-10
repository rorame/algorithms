# Бронирование переговорки

# считываем данные из консоли
n = int(input())
time_intervals = []
for i in range(n):
    s, t = map(int, input().split())
    time_intervals.append([s, t])

# сортируем интервалы по времени конца
time_intervals.sort(key=lambda x: x[1])

prev = 0
count = 1

# считаем количество непересекающихся интервалов
for i in range(1, n):
    if time_intervals[prev][1] < time_intervals[i][0]:
        count += 1
        prev = i

print(count)