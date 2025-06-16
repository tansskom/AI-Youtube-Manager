import streamlit as st
from backend.youtube_analyzer import analyze_channel

st.title("📊 AI YouTube Manager")
st.subheader("Analyze any YouTube channel in seconds")

channel_url = st.text_input("Enter YouTube Channel URL:")

if st.button("Analyze"):
    if channel_url:
        result = analyze_channel(channel_url)
        if "error" in result:
            st.error(result["error"])
        else:
            st.success("Analysis Successful ✅")

            st.write(f"**Channel Name:** {result['channel_name']}")
            st.write(f"**Subscribers:** {int(result['subscribers']):,}")
            st.write(f"**Total Views:** {int(result['views']):,}")
            st.write(f"**Total Videos:** {result['videos']}")
            st.write("**Channel Description:**")
            st.write(result['description'])
    else:
        st.warning("Please enter a valid YouTube channel URL.")
