# voice convert

## Installing

---

```bash
git clone https://github.com/leon0719/voice_convert.git
```
<hr>

## Requirements

```bash
python3.9 -m pip install virtualenv
python3.9 -m virtualenv env
#windows
source env/Scripts/activate
#linux
source env/bin/activate
#--------------------------------
cd voice_convert
pip install -r requirements.txt
```
<hr>

## Download youtube video

```bash
python grab_youtube.py -v "{path/of/youtube/url}"
```
## Audio slicing
```bash
cd voice_convert
python audio-slicer-main/slicer.py
```
<hr>

## Install so-vits requirements

```bash
cd so-vits-svc
pip install -r requirements.txt
```
<hr>

## Download pre-trained models

### See the [download_pre-trained_model.txt](download_pre-trained_model.txt)
<hr>

## Resample audio
```bash
cd so-vits-svc
python resample.py
```
<hr>

## Automatically split the dataset into training and validation sets, and generate configuration files

```bash
cd so-vits-svc
python preprocess_flist_config.py
```
<hr>

##  Generate hubert and f0

```bash
cd so-vits-svc
python preprocess_hubert_f0.py
```
<hr>

## Training

```bash
cd so-vits-svc
python train.py -c configs/config.json -m 44k
```
<hr>

##  Inference
```bash
cd so-vits-svc
# Example
python inference_main.py -m "logs/44k/G_30400.pth" -c "configs/config.json" -n "君の知らない物語-src.wav" -t 0 -s "nen"
```

## Reference

[1] [audio-slicer-main](https://github.com/openvpi/audio-slicer)

[2] [so-vits-svc](https://github.com/svc-develop-team/so-vits-svc)