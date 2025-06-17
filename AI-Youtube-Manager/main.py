import streamlit as st
from backend.youtube_analyzer import analyze_channel
from hashtag_generator import generate_hashtags
from content_ideas import generate_ideas
from best_time import get_best_posting_time

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

            st.divider()

            st.subheader("🏷️ Hashtag Suggestions")
            hashtags = generate_hashtags(result['description'])
            st.write(", ".join(hashtags))

            st.divider()

            st.subheader("💡 Content Ideas")
            ideas = generate_ideas(result['description'])
            for idea in ideas:
                st.write(f"• {idea}")

            st.divider()

            st.subheader("🕒 Best Time to Post")
            best_time = get_best_posting_time(result['channel_name'])
            st.write(f"Try posting around **{best_time}** to increase your reach.")
    else:
        st.warning("Please enter a valid YouTube channel URL.")
