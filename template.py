import os 


dirs = [
    os.path.join('data','raw'),
    os.path.join('data','processed'),
    'notebooks', 
    'saved_models',
    'src'
]

file_ = [
    'dvc.yaml',
    'params.yaml',
    '.gitignore',
    os.path.join('src','__init__.py')
]   

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)    # exist_ok=True: if the directory already exists, it will not raise an error    
    with open(os.path.join(dir_,'.gitkeep'),'w') as f:
        pass

for file in file_:
    with open(file,'w') as f:
        pass    