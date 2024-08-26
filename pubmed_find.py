import os
import re


""" CONSTANTS """
# target text file needs to be in the same directory and be named 'target'
TARGET_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'target.txt')
LINE_SEPARATOR = u'\u2028'
PARAGRAPH_SEPARATOR = u'\u2029'
VALID_WORDS = ['diet', 'dietary', 'intake', 'eating', 'eat']
INVALID_WORDS = ['food frequency questionnaire', 'FFQ']
VALID_ENTRIES = []
INVALID_ENTRIES = []


""" HELPER FUNCTIONS """
def check_words_in_line(words : list[str], line : str) -> bool:
    for word in words:
        if re.search(r'\b' + word + r'\b', line):
            print('FOUND WORD  "'+ word + '"  IN LINE  "' + line + '"')
            return True
    return False


""" MAIN SCRIPT """
with open(TARGET_FILE) as tf:
    total_entries_digested = 0
    num_carriage_return = 0
    same_entry = False
    entry_number = -1
    wait_til_next_entry = False

    try:
        for curr_line in tf:
            # count newlines that are solely newlines (empty lines)
            if curr_line[len(curr_line)-1] == '\n' and len(curr_line) == 1:
                num_carriage_return+=1

            else:
                # if this is the first time we saw the line
                if not same_entry:
                    # capture the entry number preceding a period for use later
                    entry_number = curr_line.split('.')[0]
                    # make sure we mark it as the same entry from hereafter
                    same_entry = True
                    #print(entry_number)

                # reset the newlines count if we are not on an empty line
                num_carriage_return = 0
                #print(curr_line[:len(curr_line)-1])

            # only enter these checking loops if the entry has not been 'diagnosed' already
            if not wait_til_next_entry:
                # verify if line contains invalid/valid words, and move on if either case
                if check_words_in_line(INVALID_WORDS, curr_line):
                    #print("INVALID WORD FOUND, ADDING ENTRY TO LIST")
                    INVALID_ENTRIES.append(entry_number)
                    wait_til_next_entry = True
                if check_words_in_line(VALID_WORDS, curr_line):
                    #print("VALID WORD FOUND, ADDING ENTRY TO LIST")
                    VALID_ENTRIES.append(entry_number)
                    wait_til_next_entry = True

            # once we hit a double newline, we have finished the entry
            if num_carriage_return == 2:
                same_entry = False
                total_entries_digested += 1
                wait_til_next_entry = False

            # quit early for testing purposes
            if total_entries_digested == 100:
                break
    
    except Exception as e:
        print('\n', e)

print("VALID ENTRIES: ", str(VALID_ENTRIES))
print("INVALID ENTRIES: ", str(INVALID_ENTRIES))