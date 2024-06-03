mult = -42
sumer = -11

for i in range(0, abs(mult)):
    for j in range(0, abs(mult)):
        if i + j == abs(sumer) and i * j == abs(mult):
            print([i, j])