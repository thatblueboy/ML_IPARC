import Generate_SE, Generate_Seq, Generate_Size

param = {}
param['img_size'] = 15
param['seq_length'] = 4 
param['no_examples_per_task'] = 2
param['no_colors'] = 3
for i in range(1):
    param['se_size'] = 2*i+3
    Generate_SE.generate_100_tasks_CatA_Simple(**param)

param = {}
param['img_size'] = 15
param['se_size'] = 3 
param['no_examples_per_task'] = 2
param['no_colors'] = 3
for i in range(5):
    sequence_length = 2*(i+1)
    param['seq_length'] = sequence_length
    Generate_Seq.generate_100_tasks_CatA_Simple(**param)

param = {}
param['se_size'] = 3  # Size of the structuring element
param['seq_length'] = 4  # Number of primitives would be 2*param['seq_length']
param['no_examples_per_task'] = 2
param['no_colors'] = 3
for i in range(4):
    param['img_size'] = (5*(i+2))
    Generate_Size.generate_100_tasks_CatA_Simple(**param)