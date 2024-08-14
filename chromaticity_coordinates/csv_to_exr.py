# Standard Pakages
import pathlib
import pprint

# External Pakages
# import cv2
import numpy as np
import pandas as pd
import imageio

def create_image(image_array):
    print('Create Image')
    
    # 縦のピクセル数を取得
    h = len(image_array)
    # 横のピクセル数を取得
    w = len(image_array[0])
    
    # 確認
    print(f'width = {w} height = {h}')
    
    # 32fpの黒でピクセルを塗りつぶす=新規画像
    result = np.zeros((h, w, 3), np.float32)
    
    # ピクセルの値を設定
    for h in range(0, h):
        for w in range(0, w):
            value = image_array[h][w]
            result[h, w] = value

    return result

def main():
    # スクリプトがあるフォルダを取得
    file_path = pathlib.Path(__file__).parent / 'xyz1931cmfs.csv'
    
    # pandasでcsvを読み込み
    df = pd.read_csv(file_path, header=None)
    # pandasのDataFrame型をリストに変換
    data_list = df.values.tolist()

    pprint.pprint(data_list)
    
    # ピクセルの値用変数作成
    image_array = []
    # 1ラインのデータを作成
    line_value = [ [d[0], d[1], d[2]] for d in data_list]
    # ピクセルにラインを追加
    image_array.append(line_value)
    
    # データの確認
    pprint.pprint(image_array)

    # create image
    img = create_image(image_array)
    
    # cv2はtifはnukeが16bit intとして認識
    # cv2.imwrite(fr'{root}/StdObsFuncs.tif', img)
    # cv2.imwrite(fr'{root}/StdObsFuncs.hdr', img)

    # iio
    path = file_path.with_suffix('.exr')
    imageio.imsave(path, img)    

if __name__ == '__main__':
    main()