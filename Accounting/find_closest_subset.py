from itertools import combinations



def find_closest_invoice_subset(invoices, target, tolerance): 
    """ Find the subset of invoices whose sum is closest to the target amount. 
    Args: 
        invoices (list): List of invoice amounts (positive numbers). 
        target (float): Target amount.
        tolerance (float): Tolerance percentage for error (default: 1%). 
        
    Returns: 
        dict: Dictionary containing the closest subset, its sum, and the error percentage.
    """ 
    
    best_subset = None 
    best_sum = float('-inf') 
    min_error = float('inf') 
    # Define tolerance range 
    # lower_bound = target * (1 - tolerance) 
    # upper_bound = target * (1 + tolerance)     
    lower_bound = target
    upper_bound = target + tolerance
    
    for r in range(1, len(invoices) + 1): 
        for subset in combinations(invoices, r): 
            subset_sum = sum(subset)  
            error = abs(target - subset_sum) 

            if lower_bound <= subset_sum <= upper_bound and error < min_error:
                best_subset = subset 
                best_sum = subset_sum 
                min_error = error 

    
    if best_subset: 
        return { 
            "subset": best_subset, 
            "sum": best_sum, 
            "error_percentage": (min_error / target) * 100 
            } 
    else:
        return { 
            "message": "No subset found within the given tolerance." 
            }


def show_menu():
    print("\nSimple Accounting Program")
    print("1. Add a list of invoices")
    print("2. Enter the target value")
    print("3. Enter the tolerance percentage")
    print("4. Find closest invoices subset")
    print("5. Exit")


def main():
    target_amount = None
    tolerance_percentage = None

    while True:
        
        show_menu()
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
        
            invoices = input("Enter a list of invoices, Separated by comma: ")
            invoices_list = list(map(int, invoices.split(",")))
            print("You entered: ", invoices_list)
        
        elif choice == "2":
        
            target_amount = int(input("Target value: "))
        
        elif choice == "3":
        
            tolerance_percentage = int(input("Tolerance percentage: "))
        
        elif choice == "4":
            if tolerance_percentage is None:
                tolerance_percentage = 90000
            if target_amount is None:
                break
            result = find_closest_invoice_subset(invoices_list, target_amount, tolerance_percentage)
            print("Result:", result)
        
        elif choice == "5":
        
            print("Goodbye!")
            break
        
        else:
        
            print("Invalid choice. Please try again.")

    


if __name__ == "__main__": 
    main()    


