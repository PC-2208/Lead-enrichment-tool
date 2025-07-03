import requests

# Your SerpAPI Key
SERP_API_KEY = "074aef51e4aea0cc919bdef81923f57fa819d0cacacc6e2b4ff3b5b0113eeeff"

def enrich_leads(domain):
    try:
        company_name = domain.split('.')[0]  # e.g., "stripe" from "stripe.com"
        query = f"Founder {company_name} site:linkedin.com/in"
        
        url = "https://serpapi.com/search"
        params = {
            "engine": "google",
            "q": query,
            "api_key": SERP_API_KEY
        }

        r = requests.get(url, params=params)
        data = r.json()

        leads = []
        for result in data.get("organic_results", []):
            leads.append({
                "LinkedIn Name": result.get("title", "N/A"),
                "Profile URL": result.get("link", "N/A")
            })

        return leads if leads else [{"info": "No LinkedIn profiles found."}]

    except Exception as e:
        return {"error": str(e)}
