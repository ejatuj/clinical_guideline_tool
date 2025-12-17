# clinical_guideline_tool
# Clinical Protocol Search Tool

A command-line application that searches clinical protocols using keyword matching. Built as a portfolio project demonstrating RAG (Retrieval-Augmented Generation) concepts for healthcare applications.

## 🎯 The Clinical Problem

Doctors waste precious minutes searching through lengthy protocols during emergencies. This tool demonstrates how knowledge retrieval systems can provide instant access to relevant clinical information.

## ✨ Features

- **Fast Protocol Search**: Query clinical guidelines using natural language
- **Relevance Ranking**: Results sorted by keyword match score
- **Multiple Protocols**: Searches across sepsis, stroke, and MI protocols
- **Clinical Focus**: Built by a doctor for clinical workflows

## 🚀 Quick Start
```bash
# Navigate to the project directory
cd clinical_guideline_tool/

# Run the application
python main.py
```

## 📖 Usage Examples
Enter your clinical query: nstemi management
Enter your clinical query: stroke thrombolysis criteria
Enter your clinical query: stemi management

## 🏗️ Project Structure


## 🧠 Technical Concepts

### Phase 1 (Current): Keyword Search
- Simple term matching
- Frequency-based ranking
- Demonstrates basic retrieval

### Phase 2 (Planned): Semantic Search
- Embedding-based similarity
- Understanding medical synonyms
- Vector search with sentence-transformers

### Phase 3 (Future): Full RAG
- LLM integration for natural answers
- Source citation
- PDF protocol parsing

## 🎓 Learning Journey

As a doctor learning software engineering, this project taught me:

1. **Document Retrieval**: How search engines work under the hood
2. **RAG Concepts**: Why retrieval + generation is powerful for healthcare
3. **Python Engineering**: File I/O, data structures, modular code
4. **Clinical Product Thinking**: Designing tools doctors will actually use

## 🔧 Built With

- Python 3.14 (standard library only for Phase 1)
- Future: sentence-transformers, OpenAI API

## 💡 Learning Approach

I deliberately kept the code simple using only fundamental Python concepts 
(loops, dictionaries, file I/O) to ensure I deeply understand every line. 
This is Phase 1 - I'm now learning about embeddings and semantic search for Phase 2.

**Why simple code?**
- Easier to maintain and debug
- Shows mastery of fundamentals
- Easy to explain and teach to others
- Can optimize later once core logic is solid

## 👨‍⚕️ About

Built by Ejatu, a residen doctor passionate about using technology to improve clinical workflows.

**Connect**: [www.linkedin.com/in/ejatu-j-9b74b118b] 
