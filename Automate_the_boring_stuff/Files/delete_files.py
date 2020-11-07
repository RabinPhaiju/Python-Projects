import os
import shutil
import send2trash

print(os.getcwd())

# ------------- single file -------------
# os.unlink('tree/text_shutil.txt')

# -------------delete folder ----------------
# shutil.rmtree('tree')


# --------------- delete specific files ---------
# os.chdir('test_folder')
# for filename in os.listdir():
#     if filename.endswith('.txt'):
#         # os.unlink(filename)
        # print('deleted ' + filename)

# --------- sent to trash instead of delete ---------------
# os.chdir('test_folder')
# for filename in os.listdir():
#     if filename.endswith('.txt'):
#         # send2trash.send2trash(filename)
#             print('sent to trash ' + filename)
