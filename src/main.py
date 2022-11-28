import os
from fairseq.models.fconv import FConvModel

def main():

    MODEL_NAME = "wmt14.en-de.fconv-py"
    CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
    MODEL_DIR = os.path.abspath(os.path.join(CURRENT_PATH, "..", "model", "wmt17.v2.en-de.fconv-py"))

    en2de = FConvModel.from_pretrained(
        MODEL_DIR,
        checkpoint_file="model.pt",
        data_name_or_path=MODEL_DIR,
        bpe="subword_nmt",
        bpe_codes=os.path.join(MODEL_DIR, "bpecodes"),
        tokenizer = "moses"    
    )

    result = en2de.translate("What is the meaning of life")
    print(result)


if __name__ == '__main__':
    main()