import re
import os
import pandas


# SET APPROPRIATELY
FILES = ['abstract-nutritiona-set 2007 to 2014 12 31.txt', 'abstract-nutritiona-set 2014 to 2019 12 31.txt', 'abstract-nutritiona-set 2019 to 2024 07 21.txt']
VALID_WORDS = ['dietary intake', 'diet intake', 'food intake', 'energy intake', 'eating intake', 'eat intake', 'dietary pattern', 'diet pattern', 'eating pattern', 'weekend', 'weekday', 'dietary intakes', 'diet intakes', 'food intakes', 'energy intakes', 'eating intakes', 'eat intakes', 'dietary patterns', 'diet patterns', 'eating patterns', 'weekends', 'weekdays', 'workday', 'workdays', 'offdays', 'offday']
INVALID_WORDS = ['ffq', 'food frequency questionnaire', 'food frequency questionnaires']


def read_entries(file):
    """
    reads the text file containing numbered entries, separating them using three newlines
    """
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        entries = content.split('\n\n\n')
        # clean each entry and remove leading/trailing whitespaces
        entries = [entry.strip() for entry in entries if entry.strip()]

    return entries


def process_entries(entries, valid_words, invalid_words, filename):
    """
    perform search through all entries, extracting all valid ones and desired content
    """
    # create a list of dicts of valid entries' citation, title and author
    excel_entries = {'Title':[],
                     'Author':[],
                     'Citation':[],
                     'Abstract':[]}
    
    for entry in entries:
        # check for valid and invalid words
        is_valid = any(re.search(r'\b' + re.escape(word) + r'\b', entry, re.IGNORECASE) for word in valid_words)
        is_invalid = any(re.search(r'\b' + re.escape(word) + r'\b', entry, re.IGNORECASE) for word in invalid_words)

        if is_valid and not is_invalid:
            # entry contents separated by two newlines
            entry_content = entry.split('\n\n')
            excel_entries['Title'].append(entry_content[1].replace('\n',''))
            excel_entries['Citation'].append(entry_content[0].split('doi')[0].partition('.')[2].strip())
            excel_entries['Author'].append(entry_content[2].split('(')[0])
            try:
                abstract = entry_content[4]
                if "Comment in" in abstract[:10] or "Comment on" in abstract[:10]:
                    abstract = entry_content[5]
                excel_entries['Abstract'].append(abstract.replace('\n',''))
            except:
                excel_entries['Abstract'].append('ERROR: Failed to find abstract...')
    
    return excel_entries


def save_to_excel(excel_entries):
    """
    save a dict of lists into excel
    """
    # delete the results file previously generated if it exists
    if f'results_{filename}.xlsx' in os.listdir(os.path.dirname(os.path.abspath(__file__))):
        os.remove(f'results_{filename}.xlsx')

    # convert data to pandas DataFrame and save into excel sheet
    df = pandas.DataFrame(excel_entries)
    df.to_excel(f'results_{filename}.xlsx', sheet_name='sheet1', index=False, engine='xlsxwriter')


if __name__ == '__main__':
    for file in FILES:
        entries = read_entries(file) # split text file into individual entries
        filename = file.partition('.txt')[0] # filename for the generated excel sheet
        processed_entries = process_entries(entries, VALID_WORDS, INVALID_WORDS, filename)
        save_to_excel(processed_entries)
