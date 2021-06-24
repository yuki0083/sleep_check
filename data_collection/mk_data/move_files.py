import shutil
import os

def make_dir(data_temp_path='data_temp'):
    if not os.path.exists(data_temp_path):
        os.makedirs(data_temp_path)

#nwcampathからabst_num(10動画)に一つ抽出し、data_tempに移動
def move_nwcam(nwcam_path = 'C:\\nwcam', data_temp_path = 'data_temp', abst_num = 10):
    nwcam_list = os.listdir(nwcam_path)
    nwcam_selected_list = []

    for i in range(len(nwcam_list)):
        if i%abst_num == 0:
            nwcam_selected_list.append(nwcam_list[i])

    for i in range(len(nwcam_selected_list)):
        nwcam_selected_list[i] = os.path.join(nwcam_path, nwcam_selected_list[i])
    #ファイルの移動
    for i in range(len(nwcam_selected_list)):
        nwcam_selected_list[i] = shutil.move(nwcam_selected_list[i], data_temp_path)

    return nwcam_selected_list