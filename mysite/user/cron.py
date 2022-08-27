from record.models import Room, Detail
from ml import test2

global pre
global pre_room
pre = 1

def checker(pre):
    result = test2.starting()
    
    if not result:
        if not pre:
            return
        if pre:
            pre = 0
            return pre_room.update()
    else:
        if not pre:
            pre = 1
            room = Detail()
            pre_room = Detail
            return
        else:
            return