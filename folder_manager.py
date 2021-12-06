import os
import shutil

output_dir = 'artic_output_dir'
max_dir_size = 1024


def get_directory_size(directory):
    """
    Returns the `directory` size in bytes.
    Copied from `https://www.thepythoncode.com/article/get-directory-size-in-bytes-using-python`
    """
    total = 0
    try:
        # print("[+] Getting the size of", directory)
        for entry in os.scandir(directory):
            if entry.is_file():
                # if it's a file, use stat() function
                total += entry.stat().st_size
            elif entry.is_dir():
                # if it's a directory, recursively call this function
                total += get_directory_size(entry.path)
    except NotADirectoryError:
        # if `directory` isn't a directory, get the file size then
        return os.path.getsize(directory)
    except PermissionError:
        # if for whatever reason we can't open the folder, return 0
        return 0
    return total

def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    Copied from `https://www.thepythoncode.com/article/get-directory-size-in-bytes-using-python`
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"

def delete_output_directory():
    shutil.rmtree(output_dir)

def check_for_output_directory():
    if not os.path.isdir(output_dir):
        print ('Directory \'' + output_dir + '\' does not exist. Creating...')
        os.mkdir(output_dir)
    else:
        print ('Directory \'' + output_dir + '\' found.')
        print ('Size: ' + str(get_directory_size(output_dir)))