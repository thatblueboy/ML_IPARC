import Generate_Seq, Generate_Size

param = {}
param['img_size'] = 15
param['se_size'] = 3 
param['no_examples_per_task'] = 2
param['no_colors'] = 3
for i in range(9):
    sequence_length = i+2
    param['seq_length'] = sequence_length
    Generate_Seq.generate_100_tasks_CatA_Simple(**param)

param = {}
param['se_size'] = 3  # Size of the structuring element
param['seq_length'] = 4  # Number of primitives would be 2*param['seq_length']
param['no_examples_per_task'] = 2
param['no_colors'] = 3
for i in range(8):
    param['img_size'] = 9+2*i
    Generate_Size.generate_100_tasks_CatA_Simple(**param)