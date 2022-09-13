# Copyright (c) OpenMMLab. All rights reserved.
from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class MapDataset(CustomDataset):
    """Map dataset.

    In segmentation map annotation for map, 0 stands for background,
    which is included in 12 categories. ``reduce_zero_label`` is fixed to False.
    The ``img_suffix`` is fixed to '.png' and ``seg_map_suffix`` is fixed to
    '.png'.
    """

    CLASSES = ('Blank', 'Cml.', 'Cat. 1 Resi.', 'Cat. 2 M&H. Excl. Resi.',
               'Cat. 1 L. Excl. Resi.', 'Quasi-industrial', 'Vicinity',
               'Quasi-residential', 'Cat. 2 L. Excl. Resi.', 'Cat. 1 M&H. Excl. Resi.'
               'Cat. 2 Resi.', 'Nbhd. Cml.')

    PALETTE = [[255, 255, 255], [233,107,130], [253,245,175], [213,228,188],
               [128,187,130], [179,167,227], [234,236,236], [239,130,50], [159,208,227],
               [175,205,123], [236,209,162], [239,167,185]]

    def __init__(self, **kwargs):
        super(MapDataset, self).__init__(
            img_suffix='.png',
            seg_map_suffix='.png',
            reduce_zero_label=False,
            **kwargs)

