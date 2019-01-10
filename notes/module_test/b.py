import a

print("top-level : b.py")

a.func()

if _name_ == "_main_":
    print("b.py를 직접실행")
else:
    print("b.py를 import 시켜서 실행")