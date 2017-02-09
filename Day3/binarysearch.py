class BinarySearch(list):
    length = 0

    def __init__(self, a, b):
        super(BinarySearch, self).__init__()
        self.length = a
        num = b
        while num <= a * b:
            self.append(num)
            num += b

    def search(self, num):
        count = 0

        l = self

        while len(l) > 1:
            count += 1
            half = len(l) / 2
            # print '{0} loop half is: {1} num is {2} and half num is: {3} '.format(str(count), num, half, l[half])
            if num == l[half]:
                #print l
                l = []
            elif num > l[half - 1]:
                l = l[half:len(l) - 1]
                #print l
            else:
                l = l[0:half]
                #print l
        try:
            index = self.index(num)
        except ValueError:
            index = - 1
        return {'count': count, 'index': index}

