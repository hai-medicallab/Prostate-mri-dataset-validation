import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--gpu", type=str, help="gpu id",
                    dest="gpu", default='0')
parser.add_argument("--train_dir", type=str, help="data folder with training vols",
                    dest="train_dir", default="C:/Users/39486/Desktop/VoxelMorph-torch-master/LPBA40/train")
parser.add_argument("--val_dir", type=str, help="test data directory",
                    dest="val_dir", default='C:/Users/39486/Desktop/VoxelMorph-torch-master/LPBA40/test')
args = parser.parse_args()