import streamlit as st
from backend.youtube_analyzer import analyze_channel
from backend.hashtag_generator import generate_hashtags
from backend.content_ideas import generate_ideas
from backend.best_time import get_best_posting_times

st.set_page_config(page_title="AI YouTube Manager", page_icon="📊", layout="centered")
st.title("📊 AI YouTube Manager")
st.subheader("Analyze any YouTube channel in seconds")

channel_url = st.text_input("Enter YouTube Channel URL:")

if st.button("Analyze"):
    with st.spinner("Analyzing Channel..."):
        try:
            channel_data = analyze_channel(channel_url)

            # ✅ Better validation
            if channel_data and 'name' in channel_data:
                st.success("Analysis Successful ✅")

                st.markdown(f"**Channel Name:** {channel_data['name']}")
                st.markdown(f"**Subscribers:** {channel_data['subscribers']}")
                st.markdown(f"**Total Views:** {channel_data['views']}")
                st.markdown(f"**Total Videos:** {channel_data['videos']}")

                st.markdown("**Channel Description:**")
                st.write(channel_data['description'])

                hashtags = generate_hashtags(channel_data['description'], channel_data['recent_titles'])
                st.markdown("---")
                st.markdown("### 🔖 Hashtag Suggestions:")
                st.write(", ".join(hashtags))

                content_ideas = generate_ideas(channel_data['description'], channel_data['recent_titles'])
                st.markdown("---")
                st.markdown("### 💡 Content Ideas:")
                for idea in content_ideas:
                    st.write(f"- {idea}")

                best_times = get_best_posting_times(channel_data['name'])
                st.markdown("---")
                st.markdown("### ⏰ Best Times to Post:")
                for day, time in best_times.items():
                    st.write(f"- {day}: {time}")
            else:
                st.error("Failed to fetch channel data. Please check the URL.")
        except Exception as e:
            st.error(f"Error: {str(e)}")
