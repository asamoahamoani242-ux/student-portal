import streamlit as st

st.set_page_config(page_title="iCAMPUS PORTAL", layout="wide")


if "PAGE" not in st.session_state:
    st.session_state.page = "HOME"
if "COURSES" not in st.session_state:
    st.session_state.courses = ["MATH 101", "ENG 101"]

def go_to(page_name):
    st.session_state.page = page_name

with st.sidebar:
    st.image("https://i.imagur.com/8Km9tLL.png", width=120)

    st.title("ASAMOAH AMOANI KWAME")
    st.write("STUDENT ID: 01255295B")
    st.info("please evaluate your lecturers")
    if st.button("⬅ HOME", use_container_width=True):
        go_to("Home")

if st.session_state.page == "HOME":
    st.title("🏠 student dashboard")

    col1, col2, col3, col4 = st.columns(4)

    buttons= [
        "Registration", "Register courses",
"Result", "Check grades",
"General Info", "School Info", 
"My Profile", "Update details",
"Classes", "Your Courses", 
"Time Table", "Class Schedule",
"My Finances", "Fee & Balance",
"Notice Board", "Announcements",
"My Library", "Books", 
"Lecturer Evaluation", "Rate Lecturers",
"My Suggestios", "Send Feedback",
"My Applications", "Apply For Letter",
"My Seat Number", "Exam Seat",
"My CEs", "CA Scores",
"My Reports", "Academic Report",
"Payments", "pay Fees"
]

    for i, name in enumerate(buttons):
        col = [col1, col2, col3, col4][i % 4]
        with col:
            if st.button(name, use_container_width=True):
                go_to(name)

elif st.session_state.page == "Registration":
    st.title("📜 Course Registration")
    new_course = st.selectbox("Select Course",
["CS 201", "STAT 101", "MK 101"])
    if st.button("Add Course"):
                        st.session_state.courses.append(new_course)
                        st.success(f"Registered {new_course}")

    st.write("Your Courses: ",
st.session_state.courses)
    st.button("⬅ Back", on_click=go_to,
arg=("Home",))

elif st.session_state.page == "Result":
    st.title("📊 My Results")
    st.table({"Course": ["MATH 101", "ENG 101"],
"Grade": ["A", "B+"]})

elif st.session_state.page == "My Profile":
    st.title("💀 My Profile")
    name = st.text_input("FULL NAME", "ASAMOAH AMOANI KWAME")
    phone = st.text_input("Phone Number")
    if st.button("Update profile"):
                            st.success("Profile Updated")




