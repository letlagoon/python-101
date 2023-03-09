class Fruits:
    def __init__(self, fruits_list):
        self.fruits_list = fruits_list
    
    def name(self):
        for key, value in self.fruits_list.items():
            print(f"{key} {value} บาท")

    def find_duplicate_values(self):  # สร้างตัวแปรเพื่อเก็บค่าที่ซ้ำกันของ TropicalFood 
        unique_values = set()
        duplicates = []
        for key, value in self.fruits_list.items():
            if value in unique_values:
                duplicates.append(value)
            else:
                unique_values.add(value)
        for key, value in self.fruits_list.items(): # แสดงผลค่าที่ซ้ำกัน โดยแสดงทั้ง key และ value
            if value in duplicates:
                print(f"{key} มูลค่า: {value} บาท")
    
class TropicalFruits(Fruits):  # สร้าง class ลูกโดยสืบทอด class แม่ Fruits
    def __init__(self, fruits_list):
        super().__init__(fruits_list)  # เรียกใช้ constructor ของ class แม่ด้วย super()
    
    def find_duplicate_values(self):  # เขียนเมธอดเพิ่มเติมใน class ลูก
        print("รายชื่อผลไม้ที่มีจำนวนซ้ำกัน:")
        super().find_duplicate_values()  # เรียกใช้เมธอด find_duplicate_values() ของ class แม่ด้วย super()

TropicalFood = TropicalFruits({'Apple':'10','Banana':'10','Orange':'20','Papaya':'50','Lemon':'20'})
TropicalFood.name()
TropicalFood.find_duplicate_values()