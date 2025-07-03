# Lead Enrichment Tool

A Streamlit-based app to find founders and executives on LinkedIn using just a company domain.

##  Features
- Enter a domain (e.g., stripe.com)
- Get list of founders via Google search using SerpAPI
- View results in table
- Download as CSV

##  Stack
- Python
- Streamlit
- SerpAPI
- Pandas

##  Installation

```bash
git clone https://github.com/yourusername/lead-enrichment-tool.git
cd lead-enrichment-tool
python -m venv env
env\Scripts\activate  # (use . env/bin/activate on Mac/Linux)
pip install -r requirements.txt
streamlit run app.py
