
startPosFirstword = 22
endPosFirstword = 27

startPosSecondword = 97
endPosSecondword = 102

sample = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."

result = f'{sample[startPosFirstword:endPosFirstword +1 ]} {sample[startPosSecondword:endPosSecondword + 1]}'
print(result)
