"""Description
 
* XYZ 等色関数 1931 csv書き出し用モジュール

"""

import pathlib
from pprint import pprint

import colour
import numpy as np

# パスの設定
ROOT = (pathlib.Path(__file__).parent).resolve()
CSV_FILE = ROOT / 'xyz1931cmfs.csv'

# シェイプ設定
SHAPE = colour.SpectralShape(380, 780, 5)


# Get CMFS XYZ1931等色関数取得
cmfs = colour.MSDS_CMFS['CIE 1931 2 Degree Standard Observer']
# シェイプに合わせる
cmfs = cmfs.align(SHAPE)

print(cmfs)

# Create csv dict data
data = np.array(cmfs.values)

# データ確認
pprint(data)
print(np.shape(data))
data = np.reshape(data, (81, 3))

#---------------------#
# Save CSV
#---------------------#
# 親ディレクトリまでを強制的に作成
CSV_FILE.parent.mkdir(parents = True, exist_ok=True)

# Numpyメソッドでcsv書き出し（標準モジュールだとちょっとだけ面倒
print(f'export: {CSV_FILE.as_posix()}')
np.savetxt(CSV_FILE.as_posix(), data, delimiter=',')