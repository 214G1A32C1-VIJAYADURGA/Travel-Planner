import streamlit as st
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

api_key = "Your API Key"

llm = ChatGoogleGenerativeAI(api_key=api_key, model="models/gemini-1.5-pro-latest")

template = """
Act as an expert travel planner. Provide detailed travel options from {source} to {destination} including:
- Cab
- Train
- Bus
- Flight

For each option, provide:
1. *Cost*: Estimated cost range in INR
2. *Time*: Travel time duration
3. *Pros*: Advantages
4. *Cons*: Disadvantages
5. *Notes*: Additional details

Format the response in this exact structure:
*🚕 Cab:*
- *Cost*: ₹X,XXX - ₹X,XXX
- *Time*: X-X hours
- *Pros*: [advantages]
- *Cons*: [disadvantages]
- *Notes*: [additional details]

*🚆 Train:*
- *Cost*: ₹X,XXX - ₹X,XXX
- *Time*: X-X hours
- *Pros*: [advantages]
- *Cons*: [disadvantages]
- *Notes*: [additional details]

*🚌 Bus:*
- *Cost*: ₹X,XXX - ₹X,XXX
- *Time*: X-X hours
- *Pros*: [advantages]
- *Cons*: [disadvantages]
- *Notes*: [additional details]

*✈ Flight:*
- *Cost*: ₹X,XXX - ₹X,XXX
- *Time*: X-X hours
- *Pros*: [advantages]
- *Cons*: [disadvantages]
- *Notes*: [additional details]

Finally, conclude with:
Cheapest Option: [Mode] (₹X,XXX)
Fastest Option: [Mode] (X hours)

*Important Note:* Prices are estimates and can vary based on demand, season, and booking time. Always check with the respective service providers for the latest prices and availability. Remember to factor in travel time to/from stations/airports.
"""

prompt = PromptTemplate(template=template, input_variables=["source", "destination"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

st.title("Travel Planner")
st.subheader("AI-Powered Travel Recommendations")

col1, col2 = st.columns(2)
with col1:
    source = st.text_input("From:", placeholder="Enter starting city")
with col2:
    destination = st.text_input("To:", placeholder="Enter destination city")

if st.button("Plan My Trip", type="primary"):
    if source.strip() and destination.strip():
        with st.spinner("🧠 Analyzing best travel options..."):
            try:
                response = llm_chain.run({"source": source, "destination": destination})
                
                cheapest = "Cheapest Option:" + response.split("Cheapest Option:")[1].split("Fastest Option:")[0]
                fastest = "Fastest Option:" + response.split("Fastest Option:")[1].split("*Important Note:*")[0]
                
                st.markdown(f"""
                <div style="background-color:#d4edda; padding:10px; border-radius:5px; margin-bottom:20px;">
                    <p style="font-size:20px; font-weight:bold; margin:0;">Travel Recommendations:</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"<p style='color:blue; font-size:18px; font-weight:bold;'>Travel Options between {source} and {destination}</p>", unsafe_allow_html=True)
                
                st.subheader("🌟 Best Choices")
                col_cheap, col_fast = st.columns(2)
                with col_cheap:
                    st.markdown(f"{cheapest.replace('Cheapest Option:', '').strip()}")
                    st.caption("Most Budget-Friendly Option")
                with col_fast:
                    st.markdown(f"{fastest.replace('Fastest Option:', '').strip()}")
                    st.caption("Quickest Travel Option")
                
                st.subheader("📋 All Travel Options")
                with st.expander("View Details"):
                    st.markdown(response.split("Cheapest Option:")[0], unsafe_allow_html=True)
                
                st.markdown("---")
                st.warning("*Important Note:* Prices are estimates and can vary based on demand, season, and booking time. Always check with the respective service providers for the latest prices and availability. Remember to factor in travel time to/from stations/airports.")
                
            except Exception as e:
                st.error(f"⚠ Error generating recommendations: {str(e)}")
    else:
        st.warning("ℹ Please enter both source and destination locations.")
