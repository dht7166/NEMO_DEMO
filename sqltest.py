from sqlobject import *
from NEMO import *
from tqdm import tqdm
import string
import itertools
from random import random
import numpy as np

sqlhub.processConnection = connectionForURI('sqlite:///home/htran/NEMO_model/reduced.db')

#General settings
x_size,y_size,z_size = (10,10,15)
num_total_streamline = 8000
avg_streamline_per_voxel = 83
avg_voxel_per_streamline = 80

#Generating streamlines and voxels
list_voxel = [ (x,y,z) for x in range(x_size) for y in range(y_size) for z in range(z_size)]
list_of_streamline = []
for name in itertools.product(string.ascii_letters,repeat=4):
    list_of_streamline.append(''.join(name))
    if len(list_of_streamline) == num_total_streamline:
        break

def generate_voxels():
    Voxel.createTable()
    for vox in tqdm(list_voxel):
        new_voxel = Voxel(x = vox[0],y = vox[1],z = vox[2])


def generate_streamlines():
    Streamline.createTable()
    for streamline_name in tqdm(list_of_streamline):
        new_streamline = Streamline(stream_id = streamline_name)

def random_connection(amount_crossed):
    threshold = amount_crossed/num_total_streamline
    result = [random() < threshold for i in range(num_total_streamline)]
    stream = []
    for i in range(num_total_streamline):
        if result[i]:
            stream.append(list_of_streamline[i])
    return stream

def random_connection_streamline(amount_crossed):
    threshold = amount_crossed / (x_size*y_size*z_size)
    result = [random() < threshold for i in range(x_size*y_size*z_size)]
    voxels = []
    for i in range(x_size*y_size*z_size):
        if result[i]:
            voxels.append(list_voxel[i])
    return voxels

# Streamlines and voxels initiation
generate_voxels()
generate_streamlines()


# Generating connections between streamline and voxels
streamline_per_voxel = np.random.normal(avg_streamline_per_voxel,scale=10,size = len(list_voxel))
for i,vox in tqdm(enumerate(list_voxel)):
    number_streamline_passed = int(streamline_per_voxel[i])
    stream = random_connection(number_streamline_passed)
    current_voxel = Voxel.selectBy(x = vox[0],y = vox[1],z = vox[2])[0]
    for streamline in stream:
        current_streamline = Streamline.selectBy(stream_id = streamline)[0]
        current_voxel.addStreamline(current_streamline)
