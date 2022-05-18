
startPos = 4730
endPos = 8835
result = 0
for i in range(startPos, endPos + 1):
    if i % 2 != 0:
        result += i
print(result)
