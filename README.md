# voice convert

## Depends

- ### python = 3.9
- ### g++ = 7.5.0

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

## Preprocessing

If you want to use Music Source Separation,recommend using [demucs](https://github.com/facebookresearch/demucs)

```bash
#create another environment
python3.9 -m virtualenv demucs
#windows
source demucs/Scripts/activate
#linux
source demucs/bin/activate
#--------------------------------
pip install -U demucs
```

### Separating tracks

In order to try Demucs, you can just run from any folder (as long as you properly installed it)

```bash
demucs your_wav.wav -o output/ --two-stems vocals
```

You can separate out the vocals and then cut the audio file

<hr>

## Audio slicing

```bash
cd voice_convert
python audio-slicer-main/slicer.py --audio /path/to/vocals.wav --out so-vits-svc-4.0/dataset_raw/{spk_name}
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

## Generate hubert and f0

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

## Inference

```bash
cd so-vits-svc
# Example
python inference_main.py -m "logs/44k/G_30400.pth" -c "configs/config.json" -n "test.wav" -t 0 -s "spk_name"
```
- `-m` : Model path
- `-t` : Pitch adjustment 0\~12 woman -1 \~ -12 man
- `-n` : Wav name in so-vits-svc/raw folder
- `-s` : Speaker name in so-vits-svc/dataset_raw

### Final result in so-vits-svc-4.0/results

## Reference

[1] [audio-slicer-main](https://github.com/openvpi/audio-slicer)

[2] [so-vits-svc](https://github.com/svc-develop-team/so-vits-svc)

[3] [demucs](https://github.com/facebookresearch/demucs)