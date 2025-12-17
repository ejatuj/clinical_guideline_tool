"""Load and parse clinical protocol files."""


def load_protocols():
    """
    Load all protocol text files from the protocols directory.
    
    Returns a list of dictionaries. Each dictionary has:
    - filename: name of the file
    - title: human-readable name
    - content: the full text
    """
    import os
    
    protocols = []
    protocols_dir = "protocols"
    
    # Check if directory exists
    if not os.path.exists(protocols_dir):
        print(f"Error: Directory '{protocols_dir}' not found!")
        return protocols
    
    # Get all .txt files in the directory
    files = os.listdir(protocols_dir)
    
    for filename in files:
        # Only process .txt files
        if filename.endswith(".txt"):
            filepath = os.path.join(protocols_dir, filename)
            
            try:
                # Open and read the file
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Create a dictionary for this protocol
                protocol = {}
                protocol['filename'] = filename
                
                # Make a nice title (remove .txt and replace _ with spaces)
                title = filename.replace('.txt', '').replace('_', ' ')
                protocol['title'] = title.title()  # Capitalize each word
                
                protocol['content'] = content
                
                # Add to our list
                protocols.append(protocol)
                
            except Exception as e:
                print(f"Error loading {filename}: {e}")
    
    print(f"✓ Loaded {len(protocols)} protocols")
    return protocols


# Test the function if running this file directly
if __name__ == "__main__":
    protocols = load_protocols()
    for protocol in protocols:
        print(f"\n{protocol['title']}")
        print(f"Length: {len(protocol['content'])} characters")