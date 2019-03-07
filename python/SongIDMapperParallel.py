from multiprocessing import Pool
from multiprocessing import JoinableQueue as Queue
import os

root_dir_path = '/Users/libuser/Desktop/OasisThesis/OasisThesisDownloads/MappingMaterials/temp'
out_csv_path = ''


def explore_path(path):
    directories = []
    nondirectories = []
    for filename in os.listdir(path):
        fullname = os.path.join(path, filename)
        if os.path.isdir(fullname):
            directories.append(fullname)
        else:
            nondirectories.append(filename)
    # outputfile = path.replace(os.sep, '_') + '.txt'
    # with open(outputfile, 'w') as f:
    #     for filename in nondirectories:
    #         print >> f, filename
    return directories


def parallel_worker():
    while True:
        path = unsearched.get()
        dirs = explore_path(path)
        for newdir in dirs:
            unsearched.put(newdir)
        unsearched.task_done()


unsearched = Queue()
unsearched.put(root_dir_path)

pool = Pool()
pool.apply_async(parallel_worker)

pool.close()
print("closed")
pool.join()
print("joined")

unsearched.join()
print(len(unsearched))
