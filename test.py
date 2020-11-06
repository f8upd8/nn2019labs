### TEST ###

from dataset import readDataSet
from utility import imageToData, arrayLikeGet, saveMonoImage

ar = imageToData('data/Ideal/1.png', 1, 0)
saveMonoImage('test.png', 0, (16, 16), ar)