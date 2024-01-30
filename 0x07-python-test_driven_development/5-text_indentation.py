#!/usr/bin/python3
def text_indentation(text):
    """prints a text with added lines instead of certain characters
        Args:
                text: The text to be passed
        Returns:
                Nothing, the function just prints.
        Raises:
                TypeError if the text is infact not a str type.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    txt = []
    for i in text:
        if i not in ['.', ':', '?']:
                txt.append(i)
        else:
            txt.append('\n')
            txt.append('\n')
    print("".join(txt).strip())
