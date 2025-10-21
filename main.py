# Main Python script that prompts user for search term and downloads videos from TikTok and Instagram

import os
import requests

# Function to prompt user for search term

def prompt_search_term():
    return input("Enter search term: ")

# Main function to download videos

def main():
    search_term = prompt_search_term()
    # Logic to download videos from TikTok and Instagram

if __name__ == '__main__':
    main()