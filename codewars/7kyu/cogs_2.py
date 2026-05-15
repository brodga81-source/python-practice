#Cogs 2
#Codewars
#https://www.codewars.com/kata/59e72bdcfc3c4974190000d9/train/python
def cog_RPM(cogs, n):
    speeds = [0] * len(cogs)
    speeds[n] = 1
    for i in range(n, len(cogs)-1):
        speeds[i + 1] = -speeds[i] * cogs[i] / cogs[i + 1]

