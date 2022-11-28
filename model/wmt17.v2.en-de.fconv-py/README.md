Command for training the WMT14 English-German model
===================================================

Setup notes
-----------
- Data is obtained using the scripts in fairseq-py/data:
   https://github.com/facebookresearch/fairseq-py/tree/master/data
- No further pre-processing
- Data is splitted in train and valid:
  - train contains 3960793 sentences
  - valid contains 40062 sentences
- We use a BPE sub-word vocublary with 40k tokens, trained jointly on the
  training data for both languages (see bpecodes)

```
DATADIR="/path/to/preprocessed/data"
python train.py \
  ${DATADIR} -a fconv_wmt_en_de \
  --lr 0.5 --clip-norm 0.1 \
  --force-anneal 50 --dropout 0.2 --max-tokens 4000 \
  --label-smoothing 0.1 
```
