#!/usr/bin/env python3
"""
Bank Account Class Module
This module defines a BankAccount class that encapsulates banking operations.
ALX Python Programming Paradigm - Milestone Project
"""

class BankAccount:
    """
    A simple bank account class that represents a banking account
    with basic operations like deposit, withdraw, and balance display.
    """
    
    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an initial balance.
        
        Args:
            initial_balance (float): The starting balance for the account. 
                                   Defaults to 0 if not provided.
        """
        # Initialize the account balance with the provided initial balance
        # Using encapsulation - the balance is stored as an instance attribute
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Deposit money into the account.
        
        Args:
            amount (float): The amount to deposit into the account
            
        Note:
            This method modifies the account_balance attribute directly.
        """
        # Add the deposit amount to the current balance
        self.account_balance += amount
    
    def withdraw(self, amount):
        """
        Withdraw money from the account if sufficient funds are available.
        
        Args:
            amount (float): The amount to withdraw from the account
            
        Returns:
            bool: True if withdrawal was successful, False if insufficient funds
        """
        # Check if there are sufficient funds for withdrawal
        if amount <= self.account_balance:
            # Sufficient funds - deduct the amount from balance
            self.account_balance -= amount
            return True  # Withdrawal successful
        else:
            # Insufficient funds - return False without modifying balance
            return False  # Withdrawal failed
    
    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        
        Note:
            This method only displays the balance, it doesn't return any value.
        """
        # Print the current balance formatted to 2 decimal places
        print(f"Current Balance: ${self.account_balance:.2f}")


# Example usage and testing (optional - for development testing)
if __name__ == "__main__":
    # Test the BankAccount class functionality
    print("Testing BankAccount class...")
    
    # Create a test account with $100 initial balance
    test_account = BankAccount(100)
    print("Initial balance:")
    test_account.display_balance()
    
    # Test deposit
    test_account.deposit(50)
    print("After depositing $50:")
    test_account.display_balance()
    
    # Test successful withdrawal
    success = test_account.withdraw(30)
    print(f"Withdrawal of $30 successful: {success}")
    test_account.display_balance()
    
    # Test failed withdrawal (insufficient funds)
    success = test_account.withdraw(200)
    print(f"Withdrawal of $200 successful: {success}")
    test_account.display_balance()