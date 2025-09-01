from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with. 

print(products)


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_tags = set(customer_preferences)




# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.

converted_products = []
for product in products:
    product_copy = product.copy()  # Create a copy of the product dictionary
    product_copy['tags'] = set(product_copy['tags'])  # Convert tags to a set
    converted_products.append(product_copy)
products = converted_products  # Update products to the converted list




# TODO: Step 5 - Write a function to calculate the number of matching tags

def count_matches(product_tags, customer_tags):
    if not product_tags or not customer_tags:
        return 0
    return len(product_tags.intersection(customer_tags))
\

    #Args:
     #   product_tags (set): A set of tags associated with a product. 
     
      #  customer_tags (set): A set of tags associated with the customer.
    #Returns:
    #    int: The number of matching tags between the product and customer.
    

# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
         list: A list of products containing product names and their match counts.
    '''
    matches = []
    for product in products:
        match_count = count_matches(product['tags'], customer_tags)
        matches.append((product['name'], match_count))
    # Sort by match_count in descending order
    sorted_matches = sorted(matches, key=lambda x: x[1], reverse=True)
    return sorted_matches
    pass


# TODO: Step 7 - Call your function and print the results
recommended = recommend_products(products, customer_tags)
print("Recommended Products:")
for product, count in recommended:
    print(f"{product}: {count} matching tags")
