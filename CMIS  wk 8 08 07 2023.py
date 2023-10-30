def calculate_house_cleaning_cost(number_of_rooms, cleaning_type):
    # Dictionary with cleaning prices based on house size and cleaning type
    cleaning_prices = {
        'light': {'small': 25, 'medium': 40, 'large': 60},
        'complete': {'small': 50, 'medium': 75, 'large': 100}
    }

    # Determine the house size based on the number of rooms
    if number_of_rooms <= 4:
        house_size = 'small'
    elif number_of_rooms <= 5:
        house_size = 'medium'
    else:
        house_size = 'large'

    # Calculate the cost based on the cleaning type and house size
    if cleaning_type in cleaning_prices:
        cost = cleaning_prices[cleaning_type][house_size]
        return cost
    else:
        return None


def calculate_yard_service_cost(square_footage, linear_footage, num_shrubs):
    # Cost rates for mowing, edging, and shrub pruning
    mowing_rate_per_sqft = 0.05
    edging_rate_per_ft = 0.1
    shrub_pruning_rate_per_shrub = 5

    # Calculate the cost for each yard service
    mowing_cost = square_footage * mowing_rate_per_sqft
    edging_cost = linear_footage * edging_rate_per_ft
    shrub_pruning_cost = num_shrubs * shrub_pruning_rate_per_shrub

    # Calculate the total cost for yard service
    total_cost = mowing_cost + edging_cost + shrub_pruning_cost
    return total_cost


def main():
    try:
        # Comments explaining the program's purpose and instructions
        print("Welcome to our services.")
        print("Please choose the type of service you want: house cleaning or yard service")

        # List of valid choices for the user to select from
        valid_choices = ['house cleaning', 'yard service']
        choice = input("Enter your choice: ").lower()

        # Loop until the user enters a valid choice
        while choice not in valid_choices:
            print("Invalid choice. Please choose again.")
            choice = input("Enter your choice: ").lower()

        # Perform the selected service based on user's input
        if choice == 'house cleaning':
            print("You've selected house cleaning service.")
            number_of_rooms = int(input("How many rooms do you have?: "))
            print("Which type of cleaning service do you want: light or complete?")
            cleaning_type = input("Enter the type of cleaning you want: ").lower()

            # Call the function to calculate house cleaning cost
            cost = calculate_house_cleaning_cost(number_of_rooms, cleaning_type)

        else:  # Yard Service
            print("You've selected yard service.")
            square_footage = float(input("Enter the square footage of your yard: "))
            linear_footage = float(input("Enter the linear footage of your yard's edges: "))
            num_shrubs = int(input("Enter the number of shrubs in your yard: "))

            # Call the function to calculate yard service cost
            cost = calculate_yard_service_cost(square_footage, linear_footage, num_shrubs)

        # Check if the user is a senior and apply the discount
        is_senior = input("Are you a senior? (yes/no): ").lower()
        senior_discount = 0.1  # 10% discount for seniors

        if is_senior == 'yes':
            cost *= (1 - senior_discount)

        # Display the final cost of the service
        print(f"The cost of the service is ${cost:.2f}.")

    except ValueError:
        print("Please enter valid information for the service.")


if __name__ == "__main__":
    main()
