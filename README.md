# Dicten
Educational project about steganography way resistant to frequency analysis.

## Pyhon
Tested with 3.9.5

Windows (mingw):
```bash
python -m venv dicten-runtime
alias dicten=/c/src/Dicten/dicten-runtime/Scripts/python /c/src/Dicten/src/dicten.py
dicten --help
```

## Actions
3 actions will be implemented for dicten: analyse, dict, encrypt, decrypt.

Analyse action will do statistical analysis of specific text saved to file and shows report:
```
dicten analyse --input=/c/src/Dicten/examples/1/text.txt
```

Dict action will create crypto dictionary in regards with defines specification:
```
dicten dict [--byte-rich=4] [--byte-depth=40] --output=/c/src/Dicten/temp/example.dict
```

Encrypt action will encrypt specific text via provided dictionary:
```
dicten encrypt --dictionary=/c/src/Dicten/temp/example.dict [--use-noise] [--noise-amount=5] --input=/c/src/Dicten/examples/1/text.txt --output=/c/src/Dicten/temp/secured.bin
```

Decrypt action will decrypt specified binary file by provided dictionary:
```
dicten decrypt --dictionary=/c/src/Dicten/temp/example.dict --input=/c/src/Dicten/temp/secured.bin --output=/c/src/Dicten/temp/text.txt
```

## Use cases
TBA
