import re
import json


def read_entries(file):
    """
    reads the text file containing numbered entries, separating them using three newlines.
    """
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        entries = content.split('\n\n\n')
        # clean each entry and remove leading/trailing whitespaces
        entries = [entry.strip() for entry in entries if entry.strip()]

    return entries


def process_entries(entries, valid_words, invalid_words):
    """
    create a list of dicts of valid entries' citation, title and author
    """
    valid_entries = []
    
    for entry in entries:
        # check for valid and invalid words
        is_valid = any(re.search(r'\b' + re.escape(word) + r'\b', entry, re.IGNORECASE) for word in valid_words)
        is_invalid = any(re.search(r'\b' + re.escape(word) + r'\b', entry, re.IGNORECASE) for word in invalid_words)
        
        if is_valid and not is_invalid:
            # entry contents separated by two newlines
            entry_content = entry.split('\n\n')
            valid_entries.append({
                'citation':entry_content[0].split('doi')[0], # preserve up to doi link
                'title':entry_content[1].replace('\n',''), # delete newline
                'author':entry_content[2].split('(')[0]
            })

    return valid_entries


file = 'pubmed_data.txt'
valid_words = ['dietary intake', 'diet intake', 'food intake', 'energy intake', 'eating intake', 'eat intake', 'dietary pattern', 'diet pattern', 'eating pattern', 'weekend', 'weekday']
invalid_words = ["ffq", "food frequency questionnaire"]

entries = read_entries(file)
result = process_entries(entries, valid_words, invalid_words)

with open('./results.json','w',encoding='utf-8') as f:
    f.write(json.dumps(result, indent=4))
