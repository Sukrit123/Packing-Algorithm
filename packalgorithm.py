class Bin(object):
    """ Container for xs that keeps a running sum """
    def __init__(self):
        self.xs = []
        self.sum = 0

    def append(self, x):
        self.xs.append(x)
        self.sum += x

    def __str__(self):
        """ Printable representation """
        return 'Bin(sum=%d, xs=%s)' % (self.sum, str(self.xs))

def packeralgorithm(val, maximum):
    val = sorted(val, reverse=True)
    listbins = []

    for x in val:
        for bin in listbins:
            if bin.sum + x <= maximum:
                bin.append(x)
                break
        else:
            bin = Bin()
            bin.append(x)
            listbins.append(bin)
    return listbins

if __name__ == '__main__':
    import random

    def packeralgorithmdisplay(lists, maximum):
        """ packeralgorithm a list into listbins and show the result """
        print 'List with sum', sum(lists), 'requires at least', (sum(lists)+maximum-1)/maximum, 'listbins'

        listbins = packeralgorithm(lists, maximum)

        print 'Solution using', len(listbins), 'listbins:'
        for bin in listbins:
            print bin
        print


    lists = [10,9,8,7,6,5,4,3,2,1]
    packeralgorithmdisplay(lists, 11)

    lists = [ random.randint(1, 11) for i in range(100) ]
    packeralgorithmdisplay(lists, 11)
