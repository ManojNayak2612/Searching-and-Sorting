class Search:
    def binary_search(self, a , low , high,x)->int:
        if high >=low:
            mid = (low + high)//2
            if a[mid] == x:
                return mid;
            elif a[mid] > x:
                return self.binary_search(a , low , mid - 1 , x)
            else:
                return self.binary_search(a , mid + 1 , high ,x)
        return -1
    def linear_search(self, a, x)->int:
        for i in a:
            if i == x:
                return i
        return -1
if __name__ == '__main__':
    search = Search()
    a = [1,2,3,4,5,6]
    x=search.binary_search(a,0,5,7)
    y = search.linear_search(a,3)
    if x == -1:
        print("Not Found")
    else:
        print("value of index is",x)
    if y == -1:
        print("Not Found")
    else:
        print("value of index is",y)
