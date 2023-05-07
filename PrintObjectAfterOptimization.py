class PrintObject:
    def __str__(self):
        return ', '.join(sport[0].replace('_' + self.__class__.__name__, '').lstrip('_') + ": " + str(sport[1]) for sport in vars(self).items())