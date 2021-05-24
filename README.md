# Dicten
Educational project about steganography way resistant to frequency analysis. MIT license. No guarantee in any way. 

## Pyhon
Tested with 3.9.5

Windows (mingw):
```bash
python -m venv dicten-runtime
alias dicten=/c/src/Dicten/dicten-runtime/Scripts/python /c/src/Dicten/src/dicten.py
dicten --help
```

## Actions
4 actions will be implemented for dicten: ```analyse```, ```dict```, ```encrypt```, ```decrypt```.

```analyse``` action will do statistical analysis of specific text as nonrandom char sequence saved to file and shows report:
```bash
dicten analyse --input-type=text --input=/c/src/Dicten/examples/1/text.txt
```

```dict``` action will create crypto dictionary in regards with defines specification:
```bash
dicten dict --byte-rich=4 --byte-depth=40 --output=/c/src/Dicten/temp/example.dict
```

```encrypt``` action will encrypt specific text by specified dictionary:
```bash
dicten encrypt --dictionary=/c/src/Dicten/temp/example.dict \ 
  --use-noise \
  --noise-amount=5 \
  --input=/c/src/Dicten/examples/1/text.txt \
  --output=/c/src/Dicten/temp/secured.bin
```

```decrypt``` action will decrypt secured messaged provided as binary file by specified dictionary:
```bash
dicten decrypt --dictionary=/c/src/Dicten/temp/example.dict \
  --input=/c/src/Dicten/temp/secured.bin \
  --output=/c/src/Dicten/temp/text.txt
```

## Suggestions
1. All described experiments are assuming that you will use secure way to pass encryption dictionaries to other abonents, or at least protect them from 3rd parties.
2. Choose dictionary with enough depth so as many bytes as possible would be replaced by unique byte sequences.
3. Use small messages without extra words - use noise parameters to add excess information to your encrypted messages.
4. And in general don't hesitate to use noise during encryption via `--use-noise` parameter, this will create additional barier for frequence analysis.
5. Better to use your own unique slang in messages known to small group of people - this will help to create encrypted messages with additioanl complexity.

# Disclaimer
Act with respect to society and local law in your country. I keep right to immediately report any criminal behavior related to usage of this project came to my knowledge such as development of crypto viruses, fraud, intentional damage of information and other prohibited activity.
