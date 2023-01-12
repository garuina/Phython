class Car:

    # 생성자
    def __init__(self, brand, color, price):
        # 속성
        self.__brand = brand
        self.__color = color
        self.__price = price

    # 기능
    def speedUp(self):
         print('%s 속도 올리기...' % self.brand)

    def speedDown(self):
        print('%s 속도 내리기...' % self.brand)


    def show(self):
        print('차량명 : ', self.brand)
        print('차량명 : ', self.color)
        print('차량명 : ', self.price)



    