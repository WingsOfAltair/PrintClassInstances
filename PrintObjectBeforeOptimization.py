class PrintObject:
    def __str__(self):
        attrs = vars(self)
        tempList = list()
        for sport in attrs.items():
            tempList.append(sport[0].replace('_' + self.__class__.__name__, '').lstrip('_') + ": " + str(sport[1]))
        sportResult = tempList
        return ', '.join(sportResult)