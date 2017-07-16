
def log(name):
    def decorator(func):
     def wrapper(*args,**kwargs):
        print("打印开始")
        print(name)
        func(*args,**kwargs)
        print("打印结束")
     return wrapper
    return decorator
@log("李青霞")
def Demo():
    print("我的名字是田浩兵")

if __name__=='__main__':
    Demo()

