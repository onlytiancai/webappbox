# -*- coding: utf-8 -*-

from datetime import datetime

end = datetime(year=2012, month=12, day=22)


def countdown():
    return (end - datetime.now()).days

if __name__ == '__main__':
    print '离世界末日还有%s天' % countdown()
