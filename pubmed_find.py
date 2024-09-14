import re


def read_entries(file_path):
    """
    Reads the text file containing numbered entries, separating them using two newlines.
    Allows for one newline within each entry.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Split entries by double newlines
        entries = content.split('\n\n')
        # Clean each entry and remove leading/trailing whitespaces
        entries = [entry.strip() for entry in entries if entry.strip()]
    return entries


def process_entries(entries, valid_words, invalid_words):
    valid_entries = {}
    
    for entry in entries:
        # Extract the entry number
        match = re.match(r'^(\d+)\.', entry)
        if match:
            number = match.group(1)
            
            # Check for valid and invalid words
            is_valid = any(re.search(r'\b' + re.escape(word) + r'\b', entry, re.IGNORECASE) for word in valid_words)
            is_invalid = any(re.search(r'\b' + re.escape(word) + r'\b', entry, re.IGNORECASE) for word in invalid_words)
            
            if is_valid and not is_invalid:
                # Save certain portions of the valid entry in the dictionary
                # Here, we're saving the first 50 characters as an example
                valid_entries[number] = entry[:50] + '...'
                print(valid_entries[number])
    
    return valid_entries


# Example usage
file = './pubmed_data.txt'
valid_words = ['dietary intake', 'diet intake', 'food intake', 'energy intake', 'eating intake', 'eat intake', 'dietary pattern', 'diet pattern', 'eating pattern', 'weekend', 'weekday']
invalid_words = ["ffq", "food frequency questionnaire"]

entries = read_entries(file)
result = process_entries(entries, valid_words, invalid_words)
print(result)