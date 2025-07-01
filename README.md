# 🎬 YouTube Assistant using LangChain + Mistral

An AI-powered assistant that answers questions about YouTube videos by extracting, chunking, embedding, and analyzing their transcripts. Built with LangChain, MistralAI, and FAISS.

---

## 🚀 Features

- Extracts transcripts from YouTube videos automatically
- Splits and embeds content using `MistralAIEmbeddings`
- Stores vectors in a FAISS vector store
- Retrieves relevant chunks using semantic similarity
- Generates natural language answers using `ChatMistralAI`
- Fully modular and extendable for RAG-based pipelines

---

## 🧠 How It Works

1. **Transcript Extraction**  
   Uses `YoutubeLoader` from LangChain Community to fetch transcript data.

2. **Chunking & Embedding**  
   Splits the text into chunks using `RecursiveCharacterTextSplitter`, then embeds them using `MistralAIEmbeddings`.

3. **Vector Store**  
   Stores embeddings in a local FAISS index for fast similarity search.

4. **RAG-style Querying**  
   Performs a semantic search on the embedded chunks, retrieves top matches, and passes them into a custom prompt.

5. **LLM Response Generation**  
   Uses `ChatMistralAI` to generate point-wise, context-aware answers based on retrieved content.

---

## 🛠️ Tech Stack

| Component          | Tool/Library                   |
|--------------------|--------------------------------|
| Language Model     | [MistralAI](https://mistral.ai) (`ChatMistralAI`) |
| Framework          | [LangChain](https://docs.langchain.com/) |
| Embeddings         | `MistralAIEmbeddings`          |
| Vector DB          | `FAISS`                        |
| Transcripts        | `YoutubeLoader`                |
| Prompting          | `PromptTemplate` + `RunnableSequence` |
| Environment Vars   | `python-dotenv`                |

---
