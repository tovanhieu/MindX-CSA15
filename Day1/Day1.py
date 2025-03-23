class Nhanvat():
    def __init__(self, hair, level) -> None:
        self.hair = hair
        self.level = level
        
    def bienhinh(self):
        print("Bien hinh nhan vat")
    def bay(self):
        print("Nhan vat dang bay")

print("example 1")
Sonlv1 = Nhanvat("Black","Level 1")
print(Sonlv1.hair)
print(Sonlv1.level)
Sonlv1.bienhinh()
# print("\n")
# print("example 2")
# Sonlv2 = Nhanvat()
# Sonlv2.hair = "Yellow"
# Sonlv2.level = "Level 2"
# print(Sonlv2.hair)
# print(Sonlv2.level)
# Sonlv2.bienhinh()
Sonlv2 = Nhanvat("Yellow","Level 2")
print(Sonlv2.hair)
print(Sonlv2.level)
Sonlv2.bienhinh()
Sonlv2.bay()

    