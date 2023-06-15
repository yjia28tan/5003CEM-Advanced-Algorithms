import threading


# calculate the monthly repayment for the customer
def calculate_monthly_repayment(customer, amount_to_loan, interest_rate, loan_duration_year):
    loan_duration_months = loan_duration_year * 12

    total_interest = amount_to_loan * (interest_rate/100) * loan_duration_year
    # divide 100 to convert interest rate from percentage to decimal
    total_amount_repayable = amount_to_loan + total_interest
    monthly_repayment = total_amount_repayable / loan_duration_months

    # Displaying the monthly repayment
    print(f"Calculate the monthly repayment for {customer}.")
    print(f"The monthly repayment for a loan of RM{amount_to_loan:.2f} with {interest_rate:.2f}% interest rate "
          f"for {loan_duration_year} years is RM{monthly_repayment:.2f}.\n")


# Main program
def main():
    # Input values for three customers
    customers = []

    # Accept user input for three customers
    for i in range(3):
        customer = {}
        print(f"Customer {i + 1}:")
        customer["customer"] = input("Please enter customer name: ")

        while True:
            try:
                customer["amount_to_loan"] = float(input("Please enter the amount to loan: "))
                if customer["amount_to_loan"] > 0:
                    break
                else:
                    print("Invalid input. Please enter a loan value that greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        while True:
            try:
                customer["interest_rate"] = float(input("Please enter interest rate: "))
                if customer["interest_rate"] > 0:
                    break
                else:
                    print("Invalid input. Please enter the interest rate that greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        while True:
            try:
                customer["loan_duration"] = int(input("Please enter loan duration (in years): "))
                if customer["loan_duration"] > 0:
                    break
                else:
                    print("Invalid input. Please enter a loan period that greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        customers.append(customer)
        print("")

    threads = []  # a list to save all the threads
    for customer in customers:
        # Create a thread for each customer and start it
        thread = threading.Thread(target=calculate_monthly_repayment,
                                  args=(customer["customer"], customer["amount_to_loan"], customer["interest_rate"],
                                        customer["loan_duration"]))
        thread.start()  # to start the execution of the thread
        # initially the target function in a separate thread, start() allows the threads to run concurrently
        threads.append(thread)  # insert the 3 customer thread into list
        # to keep track of all the threads that have been created. By appending each thread to the list,
        # the program can iterate over the list and use the join() method on each thread to wait for their completion.

    # Wait for all threads to finish then only end the program
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()

"""References:
Multithreading in Python | Set 1 (n.d.) 
https://www.geeksforgeeks.org/multithreading-python-set-1/

Brownlee, J. (2022) Python Threading: The Complete Guide 
https://superfastpython.com/threading-in-python/
"""
