import streamlit as st
from api import get_recommendations

def main():
    st.title('Band Recommendation App')

    query = st.text_input('Enter a band or artist name:')
    limit = st.number_input('Enter the number of similar bands to recommend:', min_value=1, max_value=20, value=10, step=1)

    if st.button('Recommend'):
        recommendation = get_recommendations(query, limit)

        if isinstance(recommendation, list):
            st.success(f"Recommended similar bands to '{query}':")
            for i, band in enumerate(recommendation, 1):
                st.write(f"{i}. {band}")
        else:
            st.error(f"Error: {recommendation['error']}")

if __name__ == '__main__':
    main()
