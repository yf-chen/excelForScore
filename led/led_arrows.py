n = 5  # 矩阵大小 5*5
for time in range(0, n):
    for x in range(0, time):
        for y in range(0, time):
            print(x, y)
            if x == time - 1 or y == time - 1:
                led.plot(x, y)
                led.plot(y, x)
            else:
                led.unplot(x, y)
                led.unplot(y, x)
    basic.pause(1000)
