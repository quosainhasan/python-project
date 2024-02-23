# Function to remove duplicates from a list
def remove_duplicates(input_list):
    return list(set(input_list))

# Example usage
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(original_list)

print("Original List:", original_list)
print("List with Duplicates Removed:", unique_list)
