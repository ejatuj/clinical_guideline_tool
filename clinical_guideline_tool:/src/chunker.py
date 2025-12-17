"""Chunk documents into searchable segments."""


def chunk_by_lines(content, chunk_size=5):
    """
    Split content into chunks of N lines.
    
    Args:
        content: the text to split
        chunk_size: how many lines per chunk (default is 5)
    
    Returns:
        A list of text chunks
    """
    # Split content into lines
    lines = content.split('\n')
    
    chunks = []
    
    # Go through lines in steps of chunk_size
    i = 0
    while i < len(lines):
        # Take chunk_size lines (or whatever is left)
        chunk_lines = []
        for j in range(chunk_size):
            if i + j < len(lines):
                chunk_lines.append(lines[i + j])
        
        # Join the lines back together
        chunk_text = '\n'.join(chunk_lines)
        
        # Only keep chunks that have actual content
        if chunk_text.strip() != "":
            chunks.append(chunk_text.strip())
        
        # Move to next chunk
        i = i + chunk_size
    
    return chunks


def chunk_protocols(protocols):
    """
    Chunk all protocols into searchable segments.
    
    Args:
        protocols: list of protocol dictionaries from loader
    
    Returns:
        List of chunk dictionaries with 'protocol', 'chunk_id', and 'text'
    """
    all_chunks = []
    
    # Go through each protocol
    for protocol in protocols:
        # Break this protocol into chunks
        chunks = chunk_by_lines(protocol['content'], chunk_size=5)
        
        # Number each chunk
        for idx in range(len(chunks)):
            # Create a dictionary for this chunk
            chunk_dict = {}
            chunk_dict['protocol'] = protocol['title']
            chunk_dict['chunk_id'] = idx
            chunk_dict['text'] = chunks[idx]
            
            all_chunks.append(chunk_dict)
    
    print(f"✓ Created {len(all_chunks)} searchable chunks")
    return all_chunks


# Test the function if running this file directly
if __name__ == "__main__":
    from loader import load_protocols
    
    protocols = load_protocols()
    chunks = chunk_protocols(protocols)
    
    print(f"\nFirst chunk:")
    print(chunks[0])