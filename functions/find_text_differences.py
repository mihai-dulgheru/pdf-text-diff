from difflib import SequenceMatcher


def find_text_differences(text_dict):
    """
    Finds the differences between two texts
    :param text_dict: A dictionary containing two dataframes with text as a single column
    :return: A list containing the differences between the two texts
    """
    if len(text_dict) != 2:
        raise ValueError("Text dictionary must have exactly 2 items.")

    text_names = list(text_dict.keys())
    text1 = text_dict[text_names[0]]['text'].values[0].strip()
    text2 = text_dict[text_names[1]]['text'].values[0].strip()

    # Calculate the similarity between the two texts
    seq_matcher = SequenceMatcher(None, text1, text2)
    opcodes = seq_matcher.get_opcodes()

    # Find the diffs between the two texts
    differences = []
    for opcode in opcodes:
        if opcode[0] == 'replace':
            differences.append(f"{text_names[0]}[{opcode[1]}:{opcode[2]}] -> {text_names[1]}[{opcode[3]}:{opcode[4]}]")
        elif opcode[0] == 'delete':
            differences.append(f"{text_names[0]}[{opcode[1]}:{opcode[2]}] -> {text_names[1]}[ ]")
        elif opcode[0] == 'insert':
            differences.append(f"{text_names[0]}[ ] -> {text_names[1]}[{opcode[3]}:{opcode[4]}]")

    return differences
