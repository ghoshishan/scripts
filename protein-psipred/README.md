# Run PSIPRED from terminal
This Repository contains python code to run **PSIPRED** (PSI-blast based secondary structure PREDiction) for Protein Secondary Structure Prediction.
This code runs throgh the terminal instead of the official PSIPRED Workbench (http://bioinf.cs.ucl.ac.uk/psipred/). If you would like to have more functionality please visit the above link.

## Requirements
1. Requests
    ```bash
    sudo pip3 install requests
    ```
2. JSON
    ```bash
    sudo pip3 install simplejson
    ```

## Installation
```bash
git clone "https://github.com/Ishan1742/protein_psipred.git"
cd protein_psipred
```

## Running
1. Enter your Protein sequence in **input.txt**
2. Open a new terminal at that folder location
3. run the command
    ```bash
    python3 runpsipred.py
    ```
4. Wait
5. The predicted Secondary sequence will be stored in **sequence.ss2**

Note. Example sequence is already provided in input.txt