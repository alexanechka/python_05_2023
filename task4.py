# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

number = int(input("Сколько журавликов сделали ребята? "))

# s = (n + n) + 2 * (n + n)
# s = 2 * n + 4 * n
# s = 6 * n

n = number // 6

print("Петя и Сережа сделали по ", n, ", а Катя сделала ", n * 4, " журавликов")
