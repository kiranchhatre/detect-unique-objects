# Detect unique persons in a video

Using Centroid Tracking, OpenCV, and Deep Learning.

Contact: [Kiran Chhatre][df1]

**References:**
- [pyimagesearch.com][PlD1]
- [tensorscience.com][PlD2]

### Installation

Create conda environment using the yml file.

```sh
$ conda env create -f mpgevaEnv.yml
```

### Downloads

| Particulars | Link |
| ------ | ------ |
| deploy.prototxt | [G Drive Shared Proto file][PlDb] |
| res10_300x300_ssd_iter_140000.caffemodel | [G Drive Shared model weights][PlGh] |

### Test on video 1

Create conda environment using the yml file.

```sh
$ python object_tracker.py -p deploy.prototxt -m res10_300x300_ssd_iter_140000.caffemodel -v ./video1.mp4
```

### Sample output

Performance of sample video 1: [Link][PlDn]

### Todos

 - Tweak for video 2 and video 3
    - Video 2: Unique object tracking and registering previously seen object when disappered 
    - Video 3: Tweak/ change pretrained model for many object tracking

---
**Note**

It works only with video 1. It has bad performance on video 3 (needs to tweak confidence, frame size. I could not check performance on high frame size since I had limited view on a smaller laptop with 15.6'' screen). This implementation does not necessarily apply to video 2 (might require different stack).

---

[//]: # (Links)

   [df1]: <https://www.linkedin.com/in/kiranchhatre/>
   [PlDb]: <https://drive.google.com/file/d/1FooT6XsUGdBhc4SngwaFTHTItWInoGDf/view?usp=sharing>
   [PlGh]: <https://drive.google.com/file/d/1GeAhhd6Uu_q-s_zyM6i3Sb-Zwsn4oiA2/view?usp=sharing>
   [PlDn]: <https://drive.google.com/file/d/1L8Ty_3Q54D4YGMykYgFywUs_KaZL81cN/view?usp=sharing>
   [PlD1]: <https://www.pyimagesearch.com/>
   [PlD2]: <https://www.tensorscience.com/>
   