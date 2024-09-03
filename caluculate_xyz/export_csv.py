import pathlib
from pprint import pprint

import colour


#==================================#
# Settings
#==================================#
ROOT = pathlib.Path(__file__).parent
CSV_FILE = ROOT / 'csv/calc_xyz.csv'
TARGET_SHAPE = colour.SpectralShape(380, 780, 10)


#==================================#
# Get SD data
#==================================#
# D65
ilm = colour.SDS_ILLUMINANTS['D65']
ilm = ilm.align(TARGET_SHAPE)

# CMFs
cmfs = colour.MSDS_CMFS['CIE 1931 2 Degree Standard Observer']
cmfs = cmfs.align(TARGET_SHAPE)

# Checker
light_skin = colour.SDS_COLOURCHECKERS['ISO 17321-1']['light skin']
light_skin = light_skin.align(TARGET_SHAPE)


#==================================#
# Create csv dict data
#==================================#
data = {}
cmfs_sds = cmfs.to_sds()
data['X'] = cmfs_sds[0]
data['Y'] = cmfs_sds[1]
data['Z'] = cmfs_sds[2]
data['D65'] = ilm
data['light_skin'] = light_skin

#==================================#
# Save CSV
#==================================#
CSV_FILE.parent.mkdir(parents=True, exist_ok=True)
colour.write_sds_to_csv_file(data, CSV_FILE.as_posix())