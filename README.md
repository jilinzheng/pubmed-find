# pubmed-find

A script to easily sort through tens of thousands of pubmed summaries.

## Usage

0. Ensure you have [Python 3](https://www.python.org/downloads/) installed; verify by typing `python --version` or `py --version` on Windows, or `python3 --version` on MacOS (you may have to add Python to your PATH environmental variable if you have installed it but cannot run the command)
1. Clone this repository (if you have Git installed) or Download it as a ZIP (both can be found under the green button)
2. Open a terminal and navigate to the folder/directory you cloned/downloaded this repo
3. Run `pip install -r requirements.txt` to install all dependencies
4. Edit the [pubmed_find.py](./pubmed_find.py) script's `files`, `valid_words`, and `invalid_words` variables to your desired filenames and words to include/exclude; be sure to save the file
5. Back in the terminal, run `python pubmed_find.py` or `py pubmed_find.py` to execute the script
6. Your .xlsx file should generate in a couple of seconds (could take longer depending on the number of files you are searching/their file sizes)
