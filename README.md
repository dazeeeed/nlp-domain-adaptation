# Domain adaptation in machine translation problems in NLP

## Setup
Prerequisites to install fairseq ON WINDOWS is to have c++ build tools installed, which can be downloaded from [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/). (i think it doesn't work on windows)

To install fairseq on WSL, run:

```sh
git clone https://github.com/pytorch/fairseq
cd fairseq
pip install --editable ./
``` 

Next, you need to download pre-trained model using links from here: [here](https://github.com/facebookresearch/fairseq/blob/main/examples/translation/README.md). After download it should be extracted from archive and placed in "nlp-domain-adaptation/model" folder so the structure looks like this:

nlp-domain-adaptation
├── README.md
├── data
├── model
│   ├── README.md
│   ├── wmt17.v2.en-de.fconv-py
│   │   ├── README.md
│   │   ├── bpecodes
│   │   ├── dict.de.txt
│   │   ├── dict.en.txt
│   │   └── model.pt
│   └── wmt17.v2.en-de.fconv-py.tar.bz2
└── src
      └── main.py


Also install sacremoses and subword-nmt using pip.
```sh
pip install sacremoses subword-nmt
``` 


## Fairseq docs
To find useful information on fairseq go to:
[docs](https://fairseq.readthedocs.io/en/latest/getting_started.html)
[how to read pretrained model](https://github.com/facebookresearch/fairseq/blob/main/examples/translation/README.md)