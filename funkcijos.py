def calculate_total_cost(distance, speed, tank_capacity, fuel_price, food_checked, toll_checked, euro_checked, pound_checked, personal_expenses):
    # Calculate the fuel cost
    fuel_consumption = distance / 100  # Assuming fuel consumption is 1L per 100km
    fuel_cost = fuel_consumption * fuel_price
    
    # Add toll fees if checked
    toll_cost = 0
    if toll_checked:
        toll_cost = 10  # Assuming toll fee is 10 EUR/GBP
    
    # Add food expenses if checked
    food_cost = 0
    if food_checked:
        food_cost = 20  # Assuming food expense is 20 EUR/GBP
    
    # Convert to EUR if necessary
    if pound_checked:
        fuel_cost *= 1.15  # Assuming 1 EUR = 1.15 GBP
        toll_cost *= 1.15
        food_cost *= 1.15
    
    # Add personal expenses
    total_cost = fuel_cost + toll_cost + food_cost + personal_expenses
    
    # Return the total cost rounded to 2 decimal places
    return round(total_cost, 2)