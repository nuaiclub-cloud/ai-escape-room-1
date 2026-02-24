import streamlit as st

st.title("Watch your step",text_alignment="center")
st.image("watch your step.jpg", caption="unsplash-Julee Juu")
st.header("Let's make an AI Model")
st.subheader("I want to make an AI Model that predicts NVIDIA stock prices")

@st.dialog("Wrong Move.")
def game_end():
	st.image("game end.jpg")
	st.stop()

@st.dialog("Nice job. Here's your first code. Write it down...or dont")
def you_win():
	st.image("first clue.jpg")
	st.stop()

r = ["Data Collection", "Data Cleaning", "Train-Test Split", "Model Training", "Model Evaluation"]
w = ["Data Quality", "Data Processing", "Binary Debugging", "Web Scraping", "Modelling" ]
options1 = ["Data Collection", "Data Processing"]
selection1 = st.pills("What's step 1?", options1, selection_mode="single", width = 1000)

if selection1 in r:
	options2 = ["Data Quality", "Data Cleaning"]
	selection2 = st.pills("Step 2?", options2, selection_mode="single", width = 1000)
	if selection2 in r:
		options3 = ["Train-Test Split", "Binary Debugging"]
		selection3 = st.pills("Step 3", options3, selection_mode="single", width = 1000)

		if selection3 in r:
			options4 = ["Web Scraping", "Model Training"]
			selection4 = st.pills("Step 4?", options4, selection_mode="single", width = 1000)

			if selection4 in r:
				options5 = ["Modelling", "Model Evaluation"]
				selection5 = st.pills("Almost there. What's the last thing I need?", options5, selection_mode="single",width=1000)
				if selection5 in r:
					you_win()
				if selection5 in w:
					game_end()


			if selection4 in w:
				game_end()

		if selection3 in w:
			game_end()

	if selection2 in w:
		game_end()

if selection1 in w:
	game_end()


