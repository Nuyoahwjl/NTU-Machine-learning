import keyword
print("Hello,World!")
print(keyword.kwlist) # 输出关键字列表


# 同一行显示多条语句
import sys; x = 'runoob'; sys.stdout.write(x + '\n') # 输出到屏幕


# 多个变量赋值
a,b,c,d,e=20,5.5,True,4+3j,complex(1,4)
# 查询变量所指对象类型
print(type(a),type(b),type(c),type(d),type(e))
print(a,b,c,d,e) # 输出变量值
print(isinstance(a,int)) # 判断变量类型


# 删除对象引用
del a
# print(a) # 报错


# 数值运算
print(2+2) # 加法
print(2-2) # 减法
print(2*2) # 乘法
print(2/2) # 除法
print(2//2) # 整除
print(2%2) # 取余
print(2**2) # 幂


# 字符串(元素类型相同,元素不可改变)
str='Runoob'
print(str) # 输出字符串
print(str[0:-1]) # 输出第一个到倒数第二个的所有字符
print(str[0]) # 输出字符串第一个字符
print(str[2:5]) # 输出从第三个开始到第五个的字符
print(str[2:]) # 输出从第三个开始后的所有字符
print(str[1:5:2]) # 输出从第二个开始到第五个且每隔两个的字符
print(str*2) # 输出字符串两次
print(str+'你好') # 连接字符串


# 列表(元素类型可以不相同,元素可以改变)
list=[1,2.5,3+4j,"rr",5]
print(list) # 输出列表
print(list[0]) # 输出列表第一个元素
print(list[1:3]) # 输出第二个到第三个元素
print(list[2:]) # 输出从第三个开始的所有元素
print(list*2) # 输出列表两次
print(list+[6,7,8]) # 连接列表
list.append('Baidu') # 添加元素
print(list)
del list[2] # 删除元素
print(list)
list.remove('rr') # 删除元素
print(list)
print(len([1, 2, 3]))
print([1, 2, 3]+[4, 5, 6])
print(['Hi!']*4)
print(3 in [1, 2, 3])
for x in [1, 2, 3]: print(x, end=" ")
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])
import operator
a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a,b))
print("operator.eq(c,b): ", operator.eq(c,b))
def reverseWords(input):
    inputWords=input.split(" ") # 通过空格将字符串分隔为列表
    inputWords=inputWords[-1::-1] 
    # 第一个参数为-1：表示从最后一个元素开始
    # 第二个参数为空：表示移动到列表末尾
    # 第三个参数为-1：表示逆向
    output=' '.join(inputWords)
    return output
if __name__=="__main__":
    input='I like runoob'
    rw=reverseWords(input)
    print(rw)
# 列表函数&方法
# len(list) 列表元素个数
# max(list) 返回列表元素最大值
# min(list) 返回列表元素最小值
# list(seq) 将元组转换为列表
# list.append(obj) 在列表末尾添加新的对象
# list.count(obj) 统计某个元素在列表中出现的次数
# list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值(用新列表扩展原来的列表)
# list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
# list.insert(index, obj) 将对象插入列表
# list.pop(obj=list[-1]) 移除列表中的一个元素(默认最后一个元素),并且返回该元素的值
# list.remove(obj) 移除列表中某个值的第一个匹配项
# list.reverse() 反向列表中元素
# list.sort([func]) 对原列表进行排序
# list.clear() 清空列表
# list.copy() 复制列表


# 元组(元素类型可以不相同,元素不可改变)
tuple=(1,2.5,3+4j,"rr",5)
print(tuple) # 输出元组
print(tuple[0]) # 输出元组第一个元素
print(tuple[1:3]) # 输出第二个到第三个元素
print(tuple[2:]) # 输出从第三个开始的所有元素
print(tuple*2) # 输出元组两次
print(tuple+(6,7,8)) # 连接元组
tuple=() # 空元组
tuple=(50,) # 元组只包含一个元素时,需要在元素后面添加逗号，否则括号会被当作运算符使用


# 集合(无序、可变、不重复)
student={'Tom','Jim','Mary','Tom','Jack','Rose'}
print(student) # 输出集合,重复的元素被自动去掉
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')
#可用set函数创建集合
a=set('abracadabra')
b=set('alacazam')
print(a) # 输出集合a
print(a-b) # a和b的差集
print(a|b) # a和b的并集
print(a&b) # a和b的交集
print(a^b) # a和b中不同时存在的元素
fruits = set(['apple', 'banana', 'orange', 'apple'])
print(fruits) # 输出集合，重复的元素被自动去掉


# 字典(元素类型可以不相同,元素可以改变,无序,通过键来访问)
dict={} # 创建空字典
dict['one']="1-菜鸟教程"
dict[2]="2-菜鸟工具"
tinydict={'name':'runoob','code':1,'site':'www.runoob.com'}
print(dict['one']) # 输出键为'one'的值
print(dict[2]) # 输出键为2的值
print(tinydict) # 输出完整字典
print(tinydict.keys()) # 输出所有键
print(tinydict.values()) # 输出所有值
# 构造函数dict()直接从键值对元组列表中构建字典
# dict=dict([('Runoob',1),('Google',2),('Taobao',3)]) 
# dict1={x:x**2 for x in (2,4,6)} # 字典推导式
# dict2=dict(Runoob=1,Google=2,Taobao=3) # 关键字参数


# bytes(不可变类型,0-255之间的整数)
a=bytes(3)
print(a) # 输出b'\x00\x00\x00'
b=bytes([1,2,3])
print(b) # 输出b'\x01\x02\x03'
c=bytes('runoob','utf-8')
print(c) # 输出b'runoob'
d=b"hello"
e=x[1:3]
f=e+b"world"
print(f) # 输出b'elloworld'
x=b"hello"
if x[0]==ord('h'): # ord()函数返回对应的 ASCII 数值
    print("x[0]是h")


for i in range(10):
    print(i) #print默认输出换行符
for i in range(10):
    print(i,end=",")


# 推导式
# 列表推导式
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper() for name in names if len(name)>3]
print(new_names)
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)
# 字典推导式
listdemo = ['Google','Runoob', 'Taobao']
newdict = {key:len(key) for key in listdemo}
print(newdict)
dic = {x: x**2 for x in (2, 4, 6)}
print(dic)
# 集合推导式
setnew = {i**2 for i in (1,2,3)}
print(setnew)
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
# 元组推导式,返回的结果是一个生成器对象
tuple_ = (x for x in range(10))
print(tuple_) # 输出生成器对象
print(tuple(tuple_)) # 输出元组


# 迭代器,字符串,列表或元组对象都可用于创建迭代器
list=[1,2,3,4]
it=iter(list) # 创建迭代器对象
print(next(it)) # 输出迭代器的下一个元素
print(next(it))
for x in it:
    print(x,end=" ")
# 把一个类作为一个迭代器使用需要在类中实现
# 两个方法 __iter__() 与 __next__()
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    x = self.a
    self.a += 1
    return x
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# 生成器
# 使用了 yield 的函数被称为生成器（generator）
# 当在生成器函数中使用 yield 语句时，函数的执行将会暂停，并将 yield 后面的表达式作为当前迭代的值返回。
# 然后，每次调用生成器的 next() 方法或使用 for 循环进行迭代时，函数会从上次暂停的地方继续执行，直到再次遇到 yield 语句
# 生成器是一个返回迭代器的函数,只能用于迭代操作
def fibonacci(n): # 生成器函数
    a,b,counter=0,1,0
    while True:
        if counter>n:
            return
        yield a
        a,b=b,a+b
        counter+=1
f=fibonacci(10) # f是一个迭代器,由生成器返回生成
# for x in f:
#     print(x,end=" ")
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()

# python 函数的参数传递：
# a=10,la=[1,2,3,4]
# 不可变类型：类似 C++ 的值传递，如整数、字符串、元组。
# 如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。
# 如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
# 可变类型：类似 C++ 的引用传递，如 列表，字典。
# 如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响
def change(a):
    print(id(a))   # 指向的是同一个对象
    a=10
    print(id(a))   # 一个新对象
a=1
print(id(a))
change(a)

# 加了星号 * 的参数会以元组(tuple)的形式导入
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
printinfo( 70, 60, 50 )
# 加了两个星号 ** 的参数会以字典的形式导入
def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
printinfo(1, a=2,b=3)

a=[str(round(355/113, i)) for i in range(1, 6)]
print(a)
b=[round(355/113, i) for i in range(1, 6)]
print(b)



matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)