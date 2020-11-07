import os
import shutil

for folderName, subFolder, filename in os.walk('./'):
    print(' folder is '+folderName)
    print('subfolders in '+ folderName + " are " + str(subFolder))
    print('filenames in ' + folderName + ' are ' + str(filename))
    print()

    # for subfold in subFolder:
    #     if 'fish' in subfold:
    #         os.rmdir(subfold)

    # for file in filename:
    #     if file.endswith('.py'):
    #         shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))

