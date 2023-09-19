class Sort:
    def Bubble_Sort(self,a)->list:
        #i is for iteration
        swap = True
        for i in range(len(a)):
            #j is for comparison
            for j in range(0,len(a)-i-1):
                if a[j]>a[j+1]:
                    a[j],a[j+1] = a[j+1],a[j]
                    swap = True
            if swap == False:
                break
        return a
    def Selection_Sort(self,a)->list:
        for i in range(len(a)):
            min = i
            for j in range(i+1,len(a)):
                if a[j]<a[min]:
                    min = j
            a[i] , a[min] = a[min] , a[i]
        return a
    def Insertion_Sort(self,a)->list:
        for i in range(1,len(a)):
            min = a[i]
            j = i - 1
            while j >= 0 and min < a[j] :
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = min
        return a
    def Merge_Sort(self,a)->list:
        if len(a) > 1:
            r = len(a)//2
            low = a[:r]
            high = a[r:]
            self.Merge_Sort(low)
            self.Merge_Sort(high)
            i = j = k = 0
            while i < len(low) and j < len(high):
                if low[i] < high[j]:
                    a[k] = low[i]
                    i += 1
                else:
                    a[k] = high[j]
                    j += 1
                k += 1
        return a
    #The Most Efficient Sorting Algorithm
    def Quick_Sort(self, a) -> list:
        def partition(a, low, high) -> int:
            pivot = a[low]
            start = low + 1
            end = high
            while True:
                while start <= end and a[start] <= pivot:
                    start += 1
                while start <= end and a[end] >= pivot:
                    end -= 1
                if start <= end:
                    a[start], a[end] = a[end], a[start]
                else:
                    break
            a[low], a[end] = a[end], a[low]
            return end

        def Quick(a, low, high):
            if low < high:
                x = partition(a, low, high)
                Quick(a, low, x - 1)
                Quick(a, x + 1, high)

        low = 0
        high = len(a) - 1
        Quick(a, low, high)
        return a
if __name__ == '__main__':
    sort = Sort()
    A = [2,1,3,8,4,6]
    I = sort.Insertion_Sort(A)
    M = sort.Merge_Sort(A)
    S = sort.Selection_Sort(A)
    B = sort.Bubble_Sort(A)
    Q = sort.Quick_Sort(A)
    print(I,M,S,B,Q)
