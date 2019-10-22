import numpy as np
from sqlobject import *

class Voxel(SQLObject):
    x = IntCol()
    y = IntCol()
    z = IntCol()
    streamlines = RelatedJoin('Streamline')


class Streamline(SQLObject):
    stream_id = StringCol(alternateID = True, length = 5)
    voxels = RelatedJoin('Voxel')