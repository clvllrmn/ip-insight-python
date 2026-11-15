from api import get_all_information
from formatter import display_information
from report_export import save_report


def main():
    """Display the menu and handle user selections."""
    last_information = None

    while True:
        print("\n" + "=" * 45)
        print("                 IP INSIGHT")
        print("=" * 45)
        print("1. Check Public IP Information")
        print("2. Save Last Report to TXT")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            print("\nRetrieving IP information. Please wait...")
            information = get_all_information()
            last_information = information
            display_information(information)

        elif choice == "2":
            if last_information is None:
                print("\nPlease retrieve IP information first.")
            else:
                try:
                    saved_path = save_report(last_information)
                    print(f"\nReport saved to: {saved_path.resolve()}")
                except OSError as error:
                    print(f"\nCould not save report: {error}")

        elif choice == "3":
            print("\nThank you for using IP Insight!")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
