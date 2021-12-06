import os

output_dir = 'artic_output_dir'
max_dir_size


if not os.path.isdir(output_dir):
    print ('Directory \'' + output_dir + '\' does not exist. Creating...')
    os.mkdir(output_dir)
else:
    print ('Directory \'' + output_dir + '\' found.')
    print ('Size: ' + os.path)

