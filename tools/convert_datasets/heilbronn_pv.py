# Copyright (c) OpenMMLab. All rights reserved.
import argparse
import glob
import math
import os
import os.path as osp
import tempfile
import zipfile

import mmcv
import numpy as np


def parse_args():
    parser = argparse.ArgumentParser(
        description='Convert potsdam dataset to mmsegmentation format')
    parser.add_argument('dataset_path', help='Heilbronn PV folder path')
    parser.add_argument('--tmp_dir', help='path of the temporary directory')
    parser.add_argument('-o', '--out_dir', help='output path')
    parser.add_argument(
        '--clip_size',
        type=int,
        help='clipped size of image after preparation',
        default=512)
    parser.add_argument(
        '--stride_size',
        type=int,
        help='stride of clipping original images',
        default=256)
    args = parser.parse_args()
    return args


def clip_big_image(image_path, clip_save_dir, args, to_label=False):
    # Original image of Potsdam dataset is very large, thus pre-processing
    # of them is adopted. Given fixed clip size and stride size to generate
    # clipped image, the intersection　of width and height is determined.
    # For example, given one 5120 x 5120 original image, the clip size is
    # 512 and stride size is 256, thus it would generate 20x20 = 400 images
    # whose size are all 512x512.
    image = mmcv.imread(image_path)

    h, w, c = image.shape
    clip_size = args.clip_size
    stride_size = args.stride_size

    num_rows = math.ceil((h - clip_size) / stride_size) if math.ceil(
        (h - clip_size) /
        stride_size) * stride_size + clip_size >= h else math.ceil(
            (h - clip_size) / stride_size) + 1
    num_cols = math.ceil((w - clip_size) / stride_size) if math.ceil(
        (w - clip_size) /
        stride_size) * stride_size + clip_size >= w else math.ceil(
            (w - clip_size) / stride_size) + 1

    x, y = np.meshgrid(np.arange(num_cols + 1), np.arange(num_rows + 1))
    xmin = x * clip_size
    ymin = y * clip_size

    xmin = xmin.ravel()
    ymin = ymin.ravel()
    xmin_offset = np.where(xmin + clip_size > w, w - xmin - clip_size,
                           np.zeros_like(xmin))
    ymin_offset = np.where(ymin + clip_size > h, h - ymin - clip_size,
                           np.zeros_like(ymin))
    boxes = np.stack([
        xmin + xmin_offset, ymin + ymin_offset,
        np.minimum(xmin + clip_size, w),
        np.minimum(ymin + clip_size, h)
    ],
                     axis=1)

    if to_label:
        # color_map = np.array([[0, 0, 0], [255, 255, 255], [255, 0, 0],
        #                       [255, 255, 0], [0, 255, 0], [0, 255, 255],
        #                       [0, 0, 255]])
        # flatten_v = np.matmul(
        #     image.reshape(-1, c),
        #     np.array([2, 3, 4]).reshape(3, 1))
        # out = np.zeros_like(flatten_v)
        # for idx, class_color in enumerate(color_map):
        #     value_idx = np.matmul(class_color,
        #                           np.array([2, 3, 4]).reshape(3, 1))
        #     out[flatten_v == value_idx] = idx
        #image = image.astype(np.int)
        #image = image.astype(np.uint8)
        image = image[:, :, 0] // 255

    for box in boxes:
        start_x, start_y, end_x, end_y = box
        clipped_image = image[start_y:end_y,
                              start_x:end_x] if to_label else image[
                                  start_y:end_y, start_x:end_x, :]
        # idx_i, idx_j = osp.basename(image_path).split('_')[2:4]
        img_name = osp.basename(image_path).split('.')[0]
        mmcv.imwrite(
            clipped_image.astype(np.uint8),
            osp.join(
                clip_save_dir,
                # f'{idx_i}_{idx_j}_{start_x}_{start_y}_{end_x}_{end_y}.png')
                f'{img_name}_{start_x}_{start_y}_{end_x}_{end_y}.png'))


def main():
    args = parse_args()
    """
    splits = {
        'train': [
            'pv153', 'pv154', 'pv155', 'pv156', 'pv157', 'pv158', 'pv159', 'pv160', 'pv161'
            
        ],
        'val': [
            'pv162', 'pv163', 'pv164', 'pv165'
        ]
    }
    """
    splits = {
        'train': [
            'id_1', 'id_3', 'id_7', 'id_12', 'id_13', 'id_14', 'id_15',
            'id_17', 'id_18', 'id_19', 'id_20', 'id_21', 'id_22', 'id_23',
            'id_24', 'id_25', 'id_27', 'id_28', 'id_29', 'id_30', 'id_31',
            'id_32', 'id_35', 'id_36', 'id_37', 'id_38', 'id_39', 'id_40'
        ],
        'val': [
            'id_2', 'id_4', 'id_5', 'id_6', 'id_8', 'id_9', 'id_10',
            'id_11', 'id_16', 'id_26', 'id_33', 'id_34'
        ]
    }

    dataset_path = args.dataset_path
    if args.out_dir is None:
        out_dir = osp.join('data', 'heilbronn_pv.py')
    else:
        out_dir = args.out_dir

    print('Making directories...')
    mmcv.mkdir_or_exist(osp.join(out_dir, 'img_dir', 'train'))
    mmcv.mkdir_or_exist(osp.join(out_dir, 'img_dir', 'val'))
    mmcv.mkdir_or_exist(osp.join(out_dir, 'ann_dir', 'train'))
    mmcv.mkdir_or_exist(osp.join(out_dir, 'ann_dir', 'val'))

    dir_src = glob.glob(dataset_path)
    dir_list = os.listdir(dir_src[0])
    # glob.glob(os.path.join(dataset_path, '*.zip'))
    print('Find the data', dir_list)

    for tmp_dir in dir_list:
        src_path_list = glob.glob(os.path.join(dir_src[0], tmp_dir, '*.tif'))
        if not len(src_path_list):
            sub_tmp_dir = os.path.join(tmp_dir, os.listdir(tmp_dir)[0])
            src_path_list = glob.glob(os.path.join(sub_tmp_dir, '*.tif'))

        prog_bar = mmcv.ProgressBar(len(src_path_list))
        for i, src_path in enumerate(src_path_list):
            img_name = osp.basename(src_path).split('.')[0]

            data_type = 'train' if img_name in splits[
                'train'] else 'val'

            if 'label' in src_path:
                dst_dir = osp.join(out_dir, 'ann_dir', data_type)
                clip_big_image(src_path, dst_dir, args, to_label=True)
            else:
                dst_dir = osp.join(out_dir, 'img_dir', data_type)
                clip_big_image(src_path, dst_dir, args, to_label=False)
            prog_bar.update()

    print('Removing the temporary files...')

    print('Done!')


if __name__ == '__main__':
    main()
