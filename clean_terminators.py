import re

def replace_unusual_terminators(input_file, output_file):
    # Read the content of the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define a regex pattern for unusual line terminators
    pattern = r'[\u2028\u2029]'  # U+2028 is Line Separator, U+2029 is Paragraph Separator

    # Replace unusual terminators with standard newline character
    cleaned_content = re.sub(pattern, '\n', content)

    # Write the cleaned content to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

# Example usage
input_file = 'pubmed_data.txt'
output_file = 'cleaned_pubmed_data.txt'
replace_unusual_terminators(input_file, output_file)