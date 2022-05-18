
startPosFirstword = 70
endPosFirstword = 77

startPosSecondword = 146
endPosSecondword = 156

sample = "hVbrJIS1UVw2DYGk76tYMw5Y1x2AE1nEM1igaCeRzCQVbZGx8ci47w1CG02a6PHwnQZVfvAegypiusGYiw6FCblXkbSuXF5GsbQLkGezosQG6r01JMgvZXxPInJ4wIdQhQlsj1bLMiHVgDbDidalbocinctus0PlKYL7piMZuLyFVA9sskeJBhMWh."

result = f'{sample[startPosFirstword:endPosFirstword +1 ]} {sample[startPosSecondword:endPosSecondword + 1]}'
print(result)
