def mutate_string(string, position, character):
    newString = string[:position] + character + string [position+1:]
    return newString