import streamlit as st

grading = {
    'Labs': 5,
    'Assignment 1': 15,
    'Assignment 2': 15,
    'Final Exam': 65
}

# TODO 1: Setup
# 1.1: Give the page a title (and optionally an icon) using set_page_config~
st.set_page_config(page_title="ISOM3400 Grade Calculator")

# You can also change the title displayed on the app if you want!
st.title("ISOM3400 Grade Calculator")
st.write("Let's see if you will pass this course~")


# TODO 1.2: Create a form to group the input together.
#           You can choose to use the 'with' notation (given) or directly call methods on the form object.
with st.form("input form"):

    # TODO 2: Ask for user input by creating number inputs/sliders. (Please remove the None values!)
    # You may define max/min values to restrict the valid range.
    labs_attended = st.number_input("Number of labs attended (max 12)", min_value=0, max_value=999)
    asm1_score = st.slider("Assignment 1 score (out of 100)", 0, 100, 0)
    asm2_score = st.slider("Assignment 2 score (out of 100)", 0, 100, 0)
    final_score = st.slider("Final exam score (out of 100)", 0, 100, 0)


    # Don't forget the submit button! You can also pass in text to display on the button.
    click_submit = st.form_submit_button("Calculate My Final Grade") 


# TODO 3: Calculate scores
if click_submit: 
    # When the click_submit button returns True, all obtained values will be sent to the Streamlit server.
    # Process the obtained values and calculate the total (weighted) score!
    # (You can refer to the grading dictionary at the top for the weights.)
    lab_ratio = min(labs_attended, 10) / 10  # cap at 10
    lab_score = lab_ratio * 100  # scaled to 100

    total_score = (
        lab_score * grading['Labs'] / 100 +
        asm1_score * grading['Assignment 1'] / 100 +
        asm2_score * grading['Assignment 2'] / 100 +
        final_score * grading['Final Exam'] / 100
    )

    st.markdown(f"### Your final score is: **{total_score:.2f}**") 


    # You should then display the calculated score on the web app. (e.g. with st.write()/st.markdown()...)

    # TODO 4: Display result
    # Once the total score has been calculated, let the user know if they are likely to pass the course or not.
    # Note that we stay in the indented block under if click_submit.
    # We do not want anything to be displayed if the user has not submitted yet.
    if total_score < 50:
        st.error("You may fail the course. Don't give up — talk to your instructor!")
    else:
        st.success("You are likely to pass the course. Good job!")





    pass
