# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
class WeightCalculatorOne(object):
    def __call__(self, event):
        return 1

    def __repr__(self):
        return '{}()'.format(self.__class__.__name__)
##__________________________________________________________________||
