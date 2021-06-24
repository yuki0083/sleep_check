import cv2
import os
import glob
import sys
"""
#ここを指定
#opencvで日本語のパス名は使えない！！
select_path ="data_check"

#video_path_directry = os.path.join("../nwcam/original", select_path)#ビデオのあるディレクトリ
dir_path = select_path #画像の保存場所
video_path_directry = 'data_temp'
filelist = glob.glob(video_path_directry+"/*")#ディレクトリ内のすべてのビデオのパスを取得
"""

def save_first_frame(video_path, dir_path, ext='jpg'):
    # video_pathは元の動画のパス
    # dir_pathはフレームを保存するディレクトリ
    # extのデフォルトはjpg

    video_name = os.path.basename(video_path).split('_')[0]  # 10588044(video_name)を取り出す

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("cap")
        sys.exit()

    os.makedirs(dir_path, exist_ok=True)  # exit_ok=Trueとすると既存のディレクトリを指定してもエラーにならない
    base_path = os.path.join(dir_path, video_name)  # 画像保存用のパスを作成

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))  # フレーム数の桁数を取得 int型はstr()で文字列にできる



    ret, frame = cap.read()

    cv2.imwrite('{}.{}'.format(base_path, ext), frame)

    cap.release()

def save_frames(filelist, dir_path="data_check"):
    for video_path in filelist:
        save_first_frame(video_path, dir_path)
