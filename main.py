from api import get_all_information
from formatter import display_information




def main():
    """Display the menu and handle user selections."""
    while True:
        print("\n" + "=" * 45)
        print("                 IP INSIGHT")
        print("=" * 45)
        print("1. Check Public IP Information")
        print("2. Exit")


        choice = input("\nEnter your choice: ").strip()


        if choice == "1":
            print("\nRetrieving IP information. Please wait...")
            information = get_all_information()
            display_information(information)


        elif choice == "2":
            print("\nThank you for using IP Insight!")
            break


        else:
            print("\nInvalid choice. Please select 1 or 2.")




if __name__ == "__main__":
    main()
