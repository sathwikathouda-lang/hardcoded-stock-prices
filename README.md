his program uses basic Python programming constructs and file handling concepts to build a stock portfolio tracker.

1. Input/Output Functions
input()
Used to take data from the user (stock symbol, quantity, save option).
Helps make the program interactive.
print()
Used to display results like portfolio summary and total investment value.
2. Data Structure
Dictionary (dict)
stock_prices: stores stock names as keys and their prices as values.
portfolio: stores user-entered stock quantities.
Useful because it allows fast lookup using keys (stock symbols).
3. Control Statements
for loop
Repeats input collection for multiple stocks.
Also used to calculate total portfolio value.
if statement
Checks whether the stock exists in the predefined price list.
Used for decision-making.
continue
Skips invalid stock entries and moves to the next iteration.
4. String Handling
.upper()
Converts input stock symbol to uppercase for consistency.
.lower()
Converts user response (yes/no) to lowercase for comparison.
5. Operators
Arithmetic Operators (*, +=)
* → calculates stock value (price × quantity)
+= → accumulates total investment value
6. File Handling
open() with "w" mode
Creates a new file or overwrites an existing file.
with open()
Ensures safe file handling (automatically closes the file).
file.write()
Writes portfolio data into a text file.
7. Formatting
f-strings (f"")
Used to format output in a readable way by embedding variables inside strings.
Summary (Theory)

This program demonstrates the use of:

Input/output operations
Dictionaries for data storage
Loops and conditional statements for logic control
String manipulation for consistency
File handling for storing results
Arithmetic operations for financial calculations

If you want, I can also convert this into a short exam answer (5 marks / 10 marks format).
