"""Search functionality - Simple keyword search."""


def keyword_search(query, chunks, top_k=3):
    """
    Simple keyword-based search through protocol chunks.
    
    Args:
        query: what the user is searching for
        chunks: list of protocol chunks to search through
        top_k: how many results to return (default is 3)
    
    Returns:
        List of the top matching chunks with scores
    """
    # Split the query into individual words
    query_words = query.lower().split()
    
    results = []
    
    # Check each chunk
    for chunk in chunks:
        # Convert chunk text to lowercase for matching
        text_lower = chunk['text'].lower()
        
        # Count how many query words appear in this chunk
        score = 0
        for word in query_words:
            if word in text_lower:
                score = score + 1
        
        # Only include chunks that match at least one word
        if score > 0:
            # Create result dictionary
            result = {}
            result['protocol'] = chunk['protocol']
            result['chunk_id'] = chunk['chunk_id']
            result['text'] = chunk['text']
            result['score'] = score
            
            results.append(result)
    
    # Sort results by score (highest first)
    # This uses a simple bubble sort for clarity
    for i in range(len(results)):
        for j in range(len(results) - 1):
            if results[j]['score'] < results[j + 1]['score']:
                # Swap them
                temp = results[j]
                results[j] = results[j + 1]
                results[j + 1] = temp
    
    # Return only the top results
    top_results = []
    for i in range(min(top_k, len(results))):
        top_results.append(results[i])
    
    return top_results


# Test the function if running this file directly
if __name__ == "__main__":
    from loader import load_protocols
    from chunker import chunk_protocols
    
    protocols = load_protocols()
    chunks = chunk_protocols(protocols)
    
    # Test query
    query = "sepsis antibiotics"
    results = keyword_search(query, chunks, top_k=3)
    
    print(f"\nSearch: '{query}'")
    print(f"Found {len(results)} results\n")
    
    for idx in range(len(results)):
        result = results[idx]
        print(f"Result {idx + 1}: {result['protocol']} (score: {result['score']})")
        print(result['text'][:100] + "...")
        print()