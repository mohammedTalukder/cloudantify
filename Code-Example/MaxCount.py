def Max_con_occurrences(a,b):
    max_count = 0
    current_count = 0

    for c in a:
        if c == b:
            current_count=current_count+1
            max_count=max(max_count, current_count)
        else:
            current_count = 0
    return max_count

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    input_char = input("Enter a character: ")
    c=Max_con_occurrences(input_string,input_char)
    print(f"Max Count is:{c}")
    
    
    
