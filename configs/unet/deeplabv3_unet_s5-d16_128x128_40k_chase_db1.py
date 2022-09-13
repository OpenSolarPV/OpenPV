_base_ = [
    '../_base_/models/deeplabv3_unet_s5-d16.py',
    '../_base_/datasets/chase_db1.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_40k.py'
]

data_root = '/Users/kaku/Desktop/Work/my_openlab/data/CHASE_DB1'

model = dict(test_cfg=dict(crop_size=(128, 128), stride=(85, 85)))
evaluation = dict(metric='mDice')

data = dict(
    train=dict(
        type='RepeatDataset',
        times=40000,
        dataset=dict(
            data_root=data_root,)),
    val=dict(
        data_root=data_root),
    test=dict(
        data_root=data_root,))
