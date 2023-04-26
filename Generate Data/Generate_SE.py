import os
import numpy as np
import json
import pdb
from matplotlib import pyplot as plt

# from skimage.morphology import binary_dilation, binary_erosion
from scipy.ndimage import binary_dilation, binary_erosion, binary_hit_or_miss
import random

from ListSelEm import *
from Utils import Process, Change_Colour


def generate_inp_out_catA_Simple(list_se_idx, **param):
    """
    """
    base_img = np.zeros((param['img_size'], param['img_size']), dtype=np.int32)
    sz = np.random.randint(3, 6)
    idx1 = np.random.randint(0, param['img_size'], size=sz)
    idx2 = np.random.randint(0, param['img_size'], size=sz)
    base_img[idx1, idx2] = 1

    # Select a random SE to dilate the base image
    # This way the inputs would have some structure but still remain random.
    for _ in range(2):
        idx = np.random.randint(0, 8)
        base_img = binary_dilation(base_img, list_se_3x3[idx])

    inp_img = np.array(base_img, copy=True)
    out_img = np.array(base_img, copy=True)

    for idx in range(len(list_se_idx)):
        out_img = binary_dilation(out_img, list_se_3x3[list_se_idx[idx]])

    for idx in range(len(list_se_idx)):
        out_img = binary_erosion(out_img, list_se_3x3[list_se_idx[idx]])

    return inp_img, out_img

def generate_one_task_CatA_Simple(**param):
    """
    """
    list_se_idx = np.random.randint(0, 8, 5)
    print(list_se_idx)
    data = []
    k = 0
    while k < param['no_examples_per_task']:
        print('finding')
        inp_img, out_img = generate_inp_out_catA_Simple(list_se_idx, **param)

        # Check if both input and output images are non-trivial
        FLAG = False
        if np.all(inp_img*1 == 1) or np.all(inp_img*1 == 0):
            FLAG = True
        elif np.all(out_img*1 == 1) or np.all(out_img*1 == 0):
            FLAG = True

        if FLAG:
            list_se_idx = np.random.randint(0, 8, 4)
            data = []
            k = -1
        else:
            # If not trivial proceed.
            data.append((inp_img, out_img))
        k += 1

    return data, list_se_idx

def write_dict_json_CatA_Simple(data, fname):
    """
    """
    dict_data = []
    for (inp, out) in data:
        inp = [[int(y) for y in x] for x in inp]
        out = [[int(y) for y in x] for x in out]
        dict_data.append({"input": inp, "output": out})

    with open(fname, "w") as f:
        f.write(json.dumps(dict_data))

def write_solution_CatA_Simple(list_se_idx, fname):
    """
    """
    print(len(list_se_idx))
    with open(fname, 'w') as f:
        for idx in list_se_idx:
            f.write("Dilation SE{}\n".format(idx+1))
        for idx in list_se_idx:
            f.write("Erosion SE{}\n".format(idx+1))

def generate_100_tasks_CatA_Simple(**param):
    """
    """
    size =  param['se_size']
    # np.random.seed(seed)
    # os.makedirs("./Dataset/CatA_Simple_nosolns", exist_ok=True)
    for task_no in range(100):
        print('done')

        data, list_se_idx = generate_one_task_CatA_Simple(**param)
        print('done')
        fname = './Dataset/SE_{:01d}/Task{:03d}.json'.format(size, task_no)
        write_dict_json_CatA_Simple(data, fname)

        fname = './Dataset/SE_{:01d}/Task{:03d}_soln.txt'.format(size, task_no)
        write_solution_CatA_Simple(list_se_idx, fname)

if __name__ == "__main__":
    param = {}
    param['img_size'] = 15

    param['seq_length'] = 4  # Number of primitives would be 2*param['seq_length']
    param['no_examples_per_task'] = 2
    param['no_colors'] = 3

    for i in range(1):
        param['se_size'] = 2*i+3
        generate_100_tasks_CatA_Simple(**param)
