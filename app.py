import streamlit as st
import pandas as pd
from enrich import enrich_leads

st.set_page_config(page_title=" Lead Enrichment Tool", layout="centered")
st.title(" LinkedIn Lead Finder")
st.write("Enter a company domain (like `stripe.com`) to find founders on LinkedIn.")

# Take domain input from the user
domain = st.text_input("Enter Company Domain")

# Only run this block if the button is clicked
if st.button("Find Founders"):
    if domain:
        with st.spinner(" Fetching leads..."):
            leads = enrich_leads(domain)

        # Now we handle the output only if 'leads' exists
        if isinstance(leads, dict) and "error" in leads:
            st.error(f" Error: {leads['error']}")
        elif isinstance(leads, list) and len(leads) > 0:
            st.success(f" Found {len(leads)} LinkedIn result(s)!")
            df = pd.DataFrame(leads)
            st.dataframe(df)

            # Optional: Save as local file too
            df.to_csv("saved_leads.csv", index=False)

            # CSV download
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label=" Download as CSV",
                data=csv,
                file_name="leads.csv",
                mime="text/csv"
            )
        else:
            st.warning(" No LinkedIn profiles found for this domain.")
    else:
        st.warning(" Please enter a domain.")
