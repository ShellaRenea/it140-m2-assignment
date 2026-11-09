from datetime import datetime

def main():
    # Prompt the user for their name and age
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    
    # Dynamically fetch the current year to avoid hardcoding
    current_year = datetime.now().year
    
    # Calculate the birth year
    birth_year = current_year - age
    
    # Output the formatted message to the user
    print(f"\nHello {name}! You were born in {birth_year}.")

if __name__ == "__main__":
    main()

