# pubmed-find

A Python script to easily search through tens of thousands of pubmed summaries, and save ones including the specified valid/invalid words into an Excel spreadsheet.

## Usage

0. Ensure you have [Python 3](https://www.python.org/downloads/) installed; verify by typing `python --version` on Windows, or `python3 --version` on MacOS (you may have to add Python to your PATH environmental variable if you have installed it but cannot run the command)
1. Clone this repository (if you have Git installed) or Download it as a ZIP (both can be found under the green button)
2. Open a terminal and navigate to the folder/directory you cloned/downloaded this repo
3. Run `pip install -r requirements.txt` to install all dependencies
4. Edit the [pubmed_find.py](./pubmed_find.py) script's `FILES`, `VALID_WORDS`, and `INVALID_WORDS` variables to your desired files and words to include/exclude; ensure that your filenames in the `FILES` variable has their extensions (`.txt`) and that they are in the same folder as the script itself; be sure to save the [pubmed_find.py](./pubmed_find.py) script before the next step
5. Back in the terminal, run `python pubmed_find.py` to execute the script
6. Your .xlsx file(s) should generate in a couple of seconds (could take longer depending on the number of files you are searching/their file sizes); the generated .xlsx files will be in the same folder as the script
