t1 = (["A", "B"], 1, 2, 3)
t2 = (4, )
# 元組雖然不可以添加，但可以合併
t3 = t1 + t2
print(t3)
print(t1 is t3)  # => False，合併後當然為不同的引用
print(id(t1), id(t3))
print("------------------------------")

# 但元組內的可變對象能改變
print(id(t1[0]))
t1[0].append("C")
# t1[0] = 2  報錯，因為最初級元素不可改變
print(t1)
print(id(t1[0]))


"""
結論：
一、元組為不可變對象，且保存的是對象引用，但不可變的只有最外層的對象引用。
二、若最外層的對象引用為可變對象，雖然它本身標識不可被改變，但對象引用中之元素能被改變。
"""
