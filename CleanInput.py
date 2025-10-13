def clean_input(input_string):
    cleaned_string = input_string.strip()
    
    words = cleaned_string.split()
    
    final_string = ' '.join(words)
    
    return final_string