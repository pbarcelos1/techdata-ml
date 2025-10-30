# techdata-ml
Repository focused on data-driven exploration of technology topics using ML and statistical analysis.

### Main Goal
- Scrape tech news, preprocess the data, and apply NLP techniques in order to cluster the articles into more specific technology areas.

---

### Project Structure
```
techdata-ml/
│
├── data/                   # Dados brutos e processados
│   ├── raw/                # Dados brutos extraídos (JSONL)
│   └── processed/          # Dados limpos
│
├── src/                    # Código-fonte principal
│   ├── scraping/           # Scripts de coleta e parsing de notícias
│   │
│   ├── preprocess/         # Limpeza e pré-processamento de texto
│   │ 
│   ├── clustering/         # Modelagem e análise não supervisionada
│   │
│   └── utils/              # Funções auxiliares
│
├── notebooks/              # Análises exploratórias e testes rápidos
│
├── models/                 # Modelos e vetorizadores treinados
│
├── reports/                # Resultados, gráficos e análises
│
└── README.md
```
---

### Data Collection
The project begins with a **web scraping module** designed to gather technology-related articles from trusted sources.  
Each article includes metadata such as:
- Title  
- Publication date  
- Author (when available)  
- Text content  
- Source URL  

This data is stored in structured `.jsonl` format for further processing.

---

### Data Preprocessing
Collected text undergoes multiple NLP preprocessing stages:
- Tokenization and lemmatization  
- Stopword removal (including custom domain-specific stopwords)  
- Lowercasing and punctuation cleaning  
- TF–IDF vectorization and keyword extraction   

---

### Machine Learning Approach
The main analytical goal is to identify **latent topics or clusters** within the technology domain using:
- **Clustering methods:** K-Means, DBSCAN, or LDA for topic discovery  
- **Dimensionality reduction:** PCA, t-SNE, or UMAP for visualization  
- **Evaluation:** Silhouette score, topic coherence, and qualitative analysis  

---

### Expected Outcomes
- Discover meaningful **topic clusters** within technology news (e.g., AI, cybersecurity, hardware, software development).  
- Build interpretable **visualizations** of semantic similarity between articles.  
- Provide a basis for further **trend analysis** and **content classification models**.  

---

### Future Improvements
- Incorporate **deep learning models** (e.g., BERT embeddings) for improved semantic clustering.  
- Develop a **dashboard** for real-time topic monitoring.  
- Expand scraping to multilingual or domain-specific sources.  
- Add a **pipeline orchestration layer** (e.g., Prefect or Airflow).  

---

### Tech Stack
- **Languages:** Python  
- **Core Libraries:**
  - **Data:** `pandas`, `numpy`, `scikit-learn`
  - **NLP:** `spacy`, `wordcloud`
  - **Web Scraping:** `requests`, `beautifulsoup4`
  - **Visualization:** `seaborn`, `plotly`

---

### Author
**Pedro Barcelos**  
_Data Science and Artificial Intelligence student at PUCRS_  
[LinkedIn](https://www.linkedin.com/in/pedrobarcelos) | [GitHub](https://github.com/pbarcelos1)
