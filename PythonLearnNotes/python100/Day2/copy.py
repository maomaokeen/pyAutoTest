import copy

alist=[1,2,3,['a','b']]

def copy():#直接赋值,默认浅拷贝传递对象的引用而已,原始列表改变，被赋值的b也会做相同的改变
    b=alist
    print(b)#[1, 2, 3, ['a', 'b']]
    alist.append('5')
    print(alist)#[1, 2, 3, ['a', 'b'], 5]
    print(b)#[1, 2, 3, ['a', 'b'], 5]

def copy2():#copy浅拷贝，没有拷贝子对象，所以原始数据改变，子对象会改变
    c = copy.copy(alist)
    print(alist);print(c)#[1, 2, 3, ['a', 'b']]        [1, 2, 3, ['a', 'b']]
    alist.append(5)
    print(alist)#[1, 2, 3, ['a', 'b'], 5]
    print(c)#[1, 2, 3, ['a', 'b']]
    alist[3]#['a', 'b']
    alist[3].append('cccc')
    #里面的子对象被改变了
    print(alist)#[1, 2, 3, ['a', 'b', 'cccc'], 5]
    print(c)#[1, 2, 3, ['a', 'b', 'cccc']]

def deepcopy():#深拷贝，包含对象里面的自对象的拷贝，所以原始对象的改变不会造成深拷贝里任何子元素的改变
    d = copy.deepcopy(alist)
    print(alist)#[1, 2, 3, ['a', 'b']]
    print(d)#[1, 2, 3, ['a', 'b']]始终没有改变
    alist.append(5)
    print(alist)  # [1, 2, 3, ['a', 'b'], 5]
    print(d)  # [1, 2, 3, ['a', 'b']]始终没有改变
    alist[3]#['a', 'b']
    alist[3].append("ccccc")
    print(alist)  # [1, 2, 3, ['a', 'b', 'ccccc'], 5]
    print(d)  # [1, 2, 3, ['a', 'b']]始终没有改变

if __name__=='__main__':
    copy()
    copy2()
    deepcopy()
