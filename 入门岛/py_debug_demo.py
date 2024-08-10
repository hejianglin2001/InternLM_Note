def add_numbers(a,b,c):
    sum = 0#这里其实覆盖了python自带的sum方法。
    sum +=a
    sum +=b
    sum +=c
    print("The sum is ",sum) 

if __name__ =='__main__':
    x,y,z = 1,2,3
    result = add_numbers(x,y,z)#图中代码这里写成1,2,3了
    print("The result of sum is ",result)