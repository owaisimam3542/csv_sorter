import csv
import sys

def sort_csv(input_file, output_file):
    try:
        # Read the CSV file into a list of rows
        with open(input_file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            rows = list(reader)

            # Check if there are at least two columns in each row
            if any(len(row) < 2 for row in rows):
                raise ValueError("CSV file must have at least two columns in each row.")

            # Sort the rows based on the values in the second column (index 1)
            sorted_rows = sorted(rows, key=lambda x: x[1], reverse=True)

            # Write the sorted rows to a new CSV file
            with open(output_file, 'w', newline='') as output_csv_file:
                writer = csv.writer(output_csv_file)
                writer.writerows(sorted_rows)

            print(f"CSV file successfully sorted and saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' not found.")
    except csv.Error as e:
        print(f"CSV error: {e}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

# Example usage:
if __name__ == "__main__":
    # Check if the script is provided with the correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py input.csv output_sorted.csv")
        sys.exit(1)

    # Get input and output file names from command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Call the function to sort the CSV file
    sort_csv(input_file, output_file)
