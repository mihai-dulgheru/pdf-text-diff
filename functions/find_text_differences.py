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
    a = text_dict[text_names[0]]['text'].values[0].strip()
    b = text_dict[text_names[1]]['text'].values[0].strip()

    # Calculate the similarity between the two texts
    seq_matcher = SequenceMatcher(None, a, b)
    opcodes = seq_matcher.get_opcodes()

    # Find the diffs between the two texts
    differences = {'replace': [], 'delete': [], 'insert': []}
    for opcode in opcodes:
        if opcode[0] == 'replace':
            # <old> should be replaced by <new>.
            differences['replace'].append({'position': f"{opcode[1]}:{opcode[2]}", 'original': a[opcode[1]:opcode[2]],
                                           'new': b[opcode[3]:opcode[4]]})
        elif opcode[0] == 'delete':
            # <value> should be deleted.
            differences['delete'].append({'position': f"{opcode[1]}:{opcode[2]}", 'value': a[opcode[1]:opcode[2]]})
        elif opcode[0] == 'insert':
            # <value> should be inserted at a[<position>].
            differences['insert'].append({'position': f"{opcode[1]}", 'value': b[opcode[3]:opcode[4]]})

    # Check if the texts are identical
    if not differences['replace'] and not differences['delete'] and not differences['insert']:
        return {}

    return differences
