#  Lead Enrichment Tool

Detect founders and decision-makers in real time with lightning-fast SerpAPI scraping — no manual search, no outdated data, just AI-powered lead generation for smarter sales and M&A insights.

# What is the Project?

The Lead Enrichment Tool is a real-time lead generation and enrichment app. It scans the web using **SerpAPI** to find LinkedIn profiles of **founders** and **key decision-makers** based on a company's domain name (e.g., `stripe.com`).

Built with **Streamlit**, this lightweight tool delivers business contacts quickly and efficiently — perfect for sales outreach, M&A research, or CRM enrichment.


# Key Features

1. AI-Powered Search using SerpAPI + Google Results.
2. Find Founders Instantly by entering just the domain
3. Outputs LinkedIn Names & Profile URLs**
4. CSV Export of all results with 1 click
5. Runs in Browser using Python + Streamlit
6. Fast & Lightweight, no heavy ML models required

# Installation & Required Libraries

`requirements.txt`:

`streamlit`

`pandas`

`requests`

`pip install streamlit pandas requests`

# How to Use It (Step-by-Step)

1. Clone the repo:

`git clone https://github.com/yourusername/lead-enrichment-tool.git`

`cd lead-enrichment-tool`

2. Paste your SerpAPI key inside enrich.py:

`SERP_API_KEY = "your_actual_serpapi_key"`

3. Run the app:

`streamlit run app.py`

4. Enter a domain like:

`stripe.com
zomato.com
nykaa.com`

5. Click Find Founders and get:

Founder names

LinkedIn URLs

Download CSV option

# Example Output

After typing zomato.com:

| LinkedIn Name             | Profile URL                                                                  |
| ------------------------- | ---------------------------------------------------------------------------- |
| Deepinder Goyal - CEO     | [https://linkedin.com/in/deepgoyal](https://linkedin.com/in/deepgoyal)       |
| Gaurav Gupta - Co-Founder | [https://linkedin.com/in/gauravzomato](https://linkedin.com/in/gauravzomato) |

# Difference from Other Applications

| Feature                          | Lead Enrichment Tool | Other Scrapers |
| -------------------------------- | -------------------- | -------------- |
| Uses Google + LinkedIn + SerpAPI | ✅ Yes                | ❌ No           |
| Real-time domain → lead pipeline | ✅ Yes                | ❌ Manual       |
| Export as CSV instantly          | ✅ Yes                | ✅/❌ Maybe      |
| Easy to customize                | ✅ Yes                | ❌ Usually not  |
| No login or heavy UI needed      | ✅ Yes                | ❌ Complex UX   |

# Future Scope

Add email enrichment with Hunter.io or Apollo

Filter by location or title (CEO only, India only, etc.)

Build a real-time dashboard of lead insights

Add chat-based lead fetch (e.g., “Find all founders of SaaS startups”)

Auto-sync to CRMs like HubSpot or Salesforce

# Contributions

Pull requests are welcome!

If you want to:

Add support for other platforms (e.g., Twitter, Crunchbase)

Enhance filtering (by industry or region)

Add Streamlit sidebar filters

Feel free to fork the repo or raise an issue.

# Contact

Project Owner: Priyanshi Chaudhary

Email: priyanshichaudhary2015@gmail.com
