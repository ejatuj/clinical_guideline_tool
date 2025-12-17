"""
Clinical Protocol Search Tool - Main Application

A simple command-line tool to search clinical protocols using keyword matching.
Built using only Helsinki Python MOOC concepts.
"""

from src.loader import load_protocols
from src.chunker import chunk_protocols
from src.search import keyword_search


def print_header():
    """Print the welcome message."""
    print()
    print("=" * 70)
    print("CLINICAL PROTOCOL SEARCH TOOL")
    print("=" * 70)
    print()
    print("Search clinical protocols using natural language queries.")
    print("Type 'quit' to exit.")
    print()


def print_results(query, results):
    """Print search results in a nice format."""
    print(f"\n🔍 Search: '{query}'")
    print("-" * 70)
    
    # Check if we found anything
    if len(results) == 0:
        print("\n❌ No results found. Try different keywords.\n")
        return
    
    print(f"\n✓ Found {len(results)} relevant sections:\n")
    
    # Print each result
    for i in range(len(results)):
        result = results[i]
        result_number = i + 1
        
        print(f"\n📄 Result {result_number} - {result['protocol']}")
        print(f"   Relevance Score: {result['score']}")
        print("-" * 70)
        print(result['text'])
        print()


def main():
    """Main application - this runs when you start the program."""
    
    # Show welcome message
    print_header()
    
    # Load the protocols
    print("📚 Loading protocols...")
    protocols = load_protocols()
    
    # Check if we loaded any protocols
    if len(protocols) == 0:
        print("\n❌ No protocols found!")
        print("Please add .txt files to the 'protocols/' directory.")
        return
    
    # Break protocols into chunks
    print("🔨 Chunking protocols for search...")
    chunks = chunk_protocols(protocols)
    print()
    
    # Start the search loop
    while True:
        # Ask user for input
        query = input("Enter your clinical query: ")
        query = query.strip()  # Remove extra spaces
        
        # Check if user wants to quit
        if query.lower() == "quit" or query.lower() == "exit" or query.lower() == "q":
            print("\n👋 Thanks for using Clinical Protocol Search!")
            print("   Built by [Your Name] - Clinician-Engineer\n")
            break
        
        # Skip if they pressed enter without typing anything
        if query == "":
            continue
        
        # Search for the query
        results = keyword_search(query, chunks, top_k=3)
        
        # Show the results
        print_results(query, results)


# Run the program
if __name__ == "__main__":
    main()