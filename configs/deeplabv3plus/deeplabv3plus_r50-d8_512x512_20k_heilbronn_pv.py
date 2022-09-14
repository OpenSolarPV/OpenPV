_base_ = [
    '../_base_/models/deeplabv3plus_r50-d8.py',
    '../_base_/datasets/heilbronn-pv.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_20k.py'
]

train_pipeline = [
    dict(type='LoadAnnotations', reduce_zero_label=False),
]

model = dict(
    decode_head=dict(num_classes=2), auxiliary_head=dict(num_classes=2))

# data = dict(
#     train=dict(
#         pipeline=train_pipeline))