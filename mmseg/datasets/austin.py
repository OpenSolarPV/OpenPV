# Copyright (c) OpenMMLab. All rights reserved.
from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class AustinDataset(CustomDataset):
    """Austin dataset.

    In segmentation map annotation for Austin, 0 stands for background,
    which is included in 2 categories. ``reduce_zero_label`` is fixed to False.
    The ``img_suffix`` is fixed to '.png' and ``seg_map_suffix`` is fixed to
    '.png'.
    """
    CLASSES = ('others', 'building')

    PALETTE = [[255, 255, 255], [0, 255, 0]]

    def __init__(self, **kwargs):
        super(AustinDataset, self).__init__(
            img_suffix='.png',
            seg_map_suffix='.png',
            reduce_zero_label=False,
            **kwargs)
