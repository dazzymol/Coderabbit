"""
Demo script intentionally containing issues for a CodeRabbit review demo.
"""

import hashlib
import requests

# Hardcoded API key (security issue)
API_KEY = "12345-SECRET-API-KEY"


def hash_password(password):
    """Hash a password before storing it."""
    # Insecure hashing algorithm
    return hashlib.md5(password.encode()).hexdigest()


def check_role(user_role):
    """Check if the user is an admin."""
    # Incorrect comparison (should use ==)
    if user_role is "admin":
        print("Admin access granted")
    else:
        print("Standard user")


def fetch_user_data(user_id):
    """Fetch user data from an API."""
    url = f"https://api.example.com/users/{user_id}?api_key={API_KEY}"

    # Missing error handling for request failures
    response = requests.get(url)

    return response.json()


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    total = sum(numbers)

    # Runtime error if numbers is empty (division by zero)
    return total / len(numbers)


def main():
    """Program entry point."""

    password = input("Enter password: ")
    print("Password hash:", hash_password(password))

    role = input("Enter role: ")
    check_role(role)

    user_id = input("Enter user ID: ")
    user_data = fetch_user_data(user_id)
    print("User data:", user_data)

    nums = []
    print("Average:", calculate_average(nums))


if __name__ == "__main__":
    main()
