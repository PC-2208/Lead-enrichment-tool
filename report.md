# Lead Enrichment Tool – AI Readiness Challenge

## Goal:
Build a lightweight, fast tool to help Caprae’s M&A and growth teams find LinkedIn profiles of key decision-makers for any business.

## What I Built:
- A web app where users input a company domain (like `stripe.com`)
- Uses **SerpAPI** to search Google for:  
  `Founder stripe site:linkedin.com/in`
- Extracts **LinkedIn profile names and URLs**
- Displays results in a table + allows **CSV export**

##  Stack:
- Python
- Streamlit (UI)
- SerpAPI (API search)
- Pandas (table, CSV export)

##  Business Value:
- Helps quickly identify founders or key people for outbound sales or acquisition interest
- Real-time, domain-based enrichment
- Clean, no-login interface for analysts or BD teams

##  Next Steps:
- Add Hunter.io for email enrichment
- Auto-verify LinkedIn titles (e.g., CEO, CTO)
- CRM integration (e.g., HubSpot)

