# Final CS50's Project
![https://github.com/CryptoPinner](https://github.com/CryptoPinner/dinos_restaurante/blob/0ecc04444e93b320d6b029dd191814cc284d6ba7/dinos.png)
## Project done by Matias Etchepare as final project for HarvardX
### Written in
[![Python](https://img.shields.io/badge/Python-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)]()

### Video Demo:
<table style="width:100%">
<tr>
<td>
<a href="https://www.youtube.com/watch?v=TvlxZlWeDRs">
<img src="https://github.com/CryptoPinner/dinos_restaurante/blob/8f01c1a8da5149994718cbf60864b7ce56dd7d8a/dinos3.png">

### Description:
_The program allows you to receive customers in the restaurant, assigns them a discount, depending on whether they are repeat customers or not, then each customer chooses from the available menus and tells them how much they have to pay._

### The program is divide in three parts:
**1) Reception:**

-->The initial prompt display the restaurant's opening hours. Using “datetime”, it will determine if it's lunchtime, dinnertime, or if the restaurant is closed. If it’s closed, it will exit with "sys.exit". If it’s open, a welcome message will be displayed giving formatting with “Figlet”.

-->After the user need to input the quantity of customers, It will only accept a range between 1-8 customers. The program will prompt a message until the user introduce a correct number.

**2) Create a list “Table” with names of customers and applicable disccount per customer:**

-->The program will execute a 'for' loop, using the quantity of customers as the number of iterations. And will ask whether you are a recurring customer or a new one.

-->This code line  accepts 'yes' or 'no' as input. If 'yes' is entered, the program will ask for your membership number, only accept the format "DINOSnnnn". The 're' library and a 'while' loop will be utilized for this purpose. The program will prompt you until a correct format is provided.

-->Then using "with open," the program searches for the customer's number in "customer.csv“ and retrieves the corresponding entire row. The customer's name is extracted from the row and a 10% discount is assigned. This data is appended to the list "Table“. Finally, the programme displays a personalised thanks message with the customer's name.

-->If is not a recurring customer, it will ask for name, age, and gender. This data is appended to "customer.csv". Then, the customer’s name is extracted from the row and applies a 50% discount as you're new. This data is appended to the list "Table“. Finally, the programme displays a personalised welcome message with the customer's name and membership number.

**3) The program promp the disccount aplicable per each customer, they choose the menú they want and promp the total to pay:**

-->After the 'For' loop finishes, the program show in Figlet format the applicable discount for each customer. Then display the three menu options, which are read from either 'lunch.csv' or 'dinner.csv' depending on the current time.

-->Next, the customer need to choose an option between 1, 2, or 3. This process will be repeated for all customers listed in the Table. The program will accumulate the chosen menu prices in a variable called 'final_price’.

-->After the 'for' loop has iterated through all the customers, the program displays a cat with message using the cowsay library. The message includes the names of all the customers at the table, along with the final amount to pay.

## Find me in:
[![Twitter](https://img.shields.io/badge/Twitter-@pinner2020-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white&labelColor=101010)](https://twitter.com/pinner2020)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Matias_Etchepare-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/matias-etchepare)




