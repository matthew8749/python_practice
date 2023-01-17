#import troch

# 定義類別
class Car():
    color = ""
    brand = ""
    # 定義初始化副程式
    def __init__(self, c, b):
        self.color = c
        self.brand = b
        print("新車建構完成,"+self.milage(0))

    def milage(self, km):
        return "里程數為"+str(km)+"公里"

# 使用類別
if __name__ == "__main__":
    # 建立物件，把類別放到變數裡，變成物件，並執行初始化副程式(加入初始值時不用加self)
    porsche = Car("白", "保時捷")      #物件是 變數被定義成一種類別，括弧內為這個類別中自己定義的性值/特性/特徵
    # 印出 新車建構完成,里程數為0公里
    print(porsche.milage(1000))
    # 印出 里程數為1000公里

##########################################
##                                  _   ##
##  ___ _   _  ___ ___ ___  ___  __| |  ##
## / __| | | |/ __/ __/ _ \/ _ \/ _` |  ##
## \__ \ |_| | (_| (_|  __/  __/ (_| |  ##
## |___/\__,_|\___\___\___|\___|\__,_|  ##
##                                      ##
##########################################


# 定義類別，此類別在本範例中當成父類別
class Car():
    color = ""
    brand = ""

    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
        print("新車建構完成,"+self.milage(0))

    def milage(self, km):
        return "里程數為"+str(km)+"公里"

# 定義類別，此類別為子類別，以上面的類別最為父類別來繼承，以上面類別為基礎做擴充改寫
class Taxi(Car):
    # 新增一個屬性，司機 driver
    driver = ""

    #定義初始化副程式，將使用super()，繼承父類別的初始化副程式
    def __init__(self, color, brand, driver):
        # super()可以直接將父類別的初始化副程式保留下來
        # 下面這行可以視為保留父類別原有的初始化副程式程式區塊
        super(Taxi, self).__init__(color, brand)
        # 以下是繼承後新增的程式碼
        self.driver = d

    # 新增一個方法，傳回牌照種類，副程式licensePlate
    def licensePlate(self):
        return "營業用牌照"

if __name__ == "__main__":
    uber = Taxi("白", "保時捷", "韓總雞")
    # 印出 新車建構完成,里程數為0公里
    print(uber.milage(1000))
    # 印出 里程數為1000公里
    print(uber.driver)
    # 印出 韓總雞
    print(uber.licensePlate())
    # 印出 營業用牌照