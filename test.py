# from bot import GeminiBot

# my_bot = GeminiBot("api key","你是一隻豬")

# print(my_bot.system_instruction)

# print(my_bot.ping())

import random

class 學生:
    def __init__(self, 班級: str, 姓名: str, 分數: int, 生命: int):
        self.班級 = 班級
        self.姓名 = 姓名
        self.分數 = 分數
        self.生命 = 生命

    def 考試(self) -> bool:
        self.生命 -= 5

        分數變化 = random.randint(-5, 5)
        self.分數 += 分數變化

        return 分數變化


我 = 學生("一一七","藍翊庭",100,100)
print(我.姓名) # 藍翊庭

for i in range(10):
    我.考試()

print(我.分數,我.生命) # 108 50

class 作弊學生(學生): # 繼承了 學生 的基礎類別
    def __init__(self, 班級, 姓名, 分數, 生命):
        super().__init__(班級, 姓名, 分數, 生命) # 先呼叫原本的初始化
        self.標籤 = "壞學生" # 再給他一個壞學生標籤

    def 考試(self) -> int: # 修改 考試 這個方法
        作弊被抓 = random.random() > 0.9
        if 作弊被抓:
            self.生命 -= 50
            self.分數 -= 50
            return -50
        else :
            分數變化 = random.randint(0, 10)
            self.分數 += 分數變化
            return 分數變化


他 = 作弊學生("一一七","藍二庭",100,100)
print(他.姓名) # 藍二庭

for i in range(10):
    他.考試()

print(他.分數,他.生命) # 165 100