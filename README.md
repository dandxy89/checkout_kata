# Checkout Kata

Updated: 17/02/2021

## Task

Implement the code for a supermarket checkout that calculates the total price of a number of items. In a normal supermarket, things are identified using Stock Keeping Units, or SKUs. In our store, we’ll use individual letters of the alphabet (A, B, C, and so on as the SKUs). Our goods are priced individually. In addition, some items are multi-priced: buy n of them, and they’ll cost you y. For example, item ‘A’ might cost 50 pence individually, but this week we have a special offer: buy three ‘A’s and they’ll cost you £1.30. In fact this week’s prices are:

| Item | Unit Price | Special Price |
|------|------------|---------------|
| A    | 50         | 3 for 120     |
| B    | 30         | 2 for 45      |
| C    | 20         |               |
| D    | 15         |               |

Our checkout accepts items in any order, so that if we scan a B, an A, and another B, we’ll recognise the two B’s and price them at 45 (for a total price so far of 95). Because the pricing changes frequently, we need to be able to pass in a set of pricing rules each time we start handling a checkout transaction.

An example of the type of questions that might be asked in the interview are:

1. Can you write a unittest?
2. Can you explain what would happen if an Item didn't exist in the Checkout and how you might handle it?
3. Can you explain how you might rewrite or improve upon the initial implementation?

## Prototype

An initial prototype has been prepared - during the interview you'll be expected to extend and improve upon the initial implementation to fulfill all the requirements specified above.
