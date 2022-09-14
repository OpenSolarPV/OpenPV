# Open Photovoltaics Toolkit(OpenPV)

![openpv](/features/openpv.jpg)

## Introduction

OpenPV is an open source toolbox for solar photovoltaics semantic segmentation.









This project contains several preprocessing tools built by python:

* Building life pattern tree from raw GPS trajectory data.
* Preprocessing tools are used for the generation model of the "pseudo life pattern." 
* Essential preprocessing tools for converting raw GPS data to grid-based data format.
* Pseudo life pattern to the spatial sequence of trips.
* Map-matching as post-processing of GPS trajectory.


## Usage
Please refer to the [requirements.txt](requirements.txt) for the necessary python library.

## Benchmark and model zoo

Results and models are available in the model zoo.

Supported backbones:

Supported methods:

Supported datasets:

- [x] Heilbronn, Germany

- pv polygons: 5442
- building polygons: 38737

![openpv](/features/dataset_Heilbronn.jpg)

- [x] Jiaxing, China

- pv polygons: 5755

![openpv](/features/dataset_Jiaxing.png)







## Project status

This project is currently under development. We will continuously update this project.

### To Do



## Authors and acknowledgment

We will add this part later shortly.

Zhiling Guo
Haoran Zhang
Qi Chen
Peiran Li
Zhan Zhuang
...

## Citation

If this repo is useful for your research, please consider citation

```
@article{li2021understanding,
  title={Understanding rooftop PV panel semantic segmentation of satellite and aerial images for better using machine learning},
  author={Li, Peiran and Zhang, Haoran and Guo, Zhiling and Lyu, Suxing and Chen, Jinyu and Li, Wenjing and Song, Xuan and Shibasaki, Ryosuke and Yan, Jinyue},
  journal={Advances in applied energy},
  volume={4},
  pages={100057},
  year={2021},
  publisher={Elsevier}
}
```



## References

[mmsegmentation](https://github.com/open-mmlab/mmsegmentation)



## License

OpenMOB is released under the MIT license. Please refer to [LICENSES](LICENSE) for the careful check.