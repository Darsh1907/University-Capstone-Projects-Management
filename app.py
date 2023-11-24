import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

from student.add_proj import add_proj
from student.view_status import view_status
from student.view_domains import view_domains
from student.view_evaluation import view_evaluation
from student.view_panel import view_panel

from faculty.eval import eval
from faculty.panel_details import panel_details
from faculty.your_students import your_students

from admin.create_panel import create_panel
from admin.avail_for_panel import avail_for_panel
from admin.increment_semester import increment_semester
from admin.approve_idea import approve_idea
from admin.add_domain import add_domain
from admin.view_toppers import view_toppers
from admin.delete_domain import delete_domain
from admin.all_faculties import all_faculties
from admin.all_students import all_students


# st.title("PES University")
st.header("Capstone Projects Management")
st.sidebar.image("pes_university.png")


is_login = False # Variable to check if the user has logged in
with open('users.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    with open('users.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    user_type = config['credentials']['usernames'].get(username, {}).get('type', None)
    is_login = True
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')


# User priviledges on frontend after login for student
if is_login and user_type=='Student':
    srn = username
    menu = ["Dashboard", "Add Team", "View Status", "View Evaluation", "View Panel"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice=="Dashboard":
        st.subheader(f'Welcome *{name} ({user_type})*')
        st.image("students.gif", width=550)
        authenticator.logout('Logout', 'main')
    elif choice == "Add Team":
        st.subheader("Available Domains:")
        view_domains()
        st.divider()
        st.subheader("Add your Project")
        add_proj(srn)
    elif choice == "View Status":
        st.subheader("View Status")
        view_status(srn)
    elif choice == "View Evaluation":
        st.subheader("View Your Evaluations:")
        view_evaluation(srn)
    elif choice == "View Panel":
        st.subheader("View Your Panel:")
        view_panel(srn)
    else:
        st.subheader("Select a valid option")

# User priviledges on frontend after login for Admin
if is_login and user_type=='Admin':
    menu = ["Dashboard","Faculties", "Students", "Create Panel", "Increment Semester", "Approve Idea", "Add Domain", "Delete Domain", "Toppers"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice=="Dashboard":
        st.subheader(f'Welcome *{name} ({user_type})*')
        st.image("admin_image.jpg", width=900)
        authenticator.logout('Logout', 'main')
    elif choice=="Faculties":
        st.subheader("List of All Faculties")
        all_faculties()
    elif choice=="Students":
        st.subheader("List Of all students:")
        all_students()
    elif choice=="Add Domain":
        st.subheader("Add Domain")
        add_domain()
    elif choice=="Delete Domain":
        st.subheader("Delete Domain")
        delete_domain()
    elif choice == "Create Panel":
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Available Teachers:")
            avail_for_panel()
        with col2:
            st.subheader("Available Domains for Panel:")
            view_domains()
        st.divider()
        st.subheader("Enter Panel Details:")
        create_panel()
    elif choice=="Increment Semester":
        st.subheader("Increment Semester:")
        st.text("Increment Semester for Each Student")
        st.text("ALERT: This will delete students that will leave 8th semester")
        increment_semester()
    elif choice=="Approve Idea":
        st.subheader("Approve Idea")
        approve_idea()
    elif choice=="Toppers":
        st.subheader("View our Toppers:")
        view_toppers()
    else:
        st.subheader("Select a Valid Option")

# User priviledges on frontend after login for Faculty
if is_login and user_type=='Faculty':
    email_id = username
    menu = ["Dashboard", "Evaluate", "Panel Details", "Students"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice=="Dashboard":
        st.subheader(f'Welcome {name} ({user_type})')
        st.image("faculty.jpg")
        authenticator.logout('Logout', 'main')
    elif choice == "Evaluate":
        st.subheader("Evaluate a student:")
        eval(email_id)
    elif choice == "Panel Details":
        st.subheader("Panel Details:")
        panel_details(email_id)
    elif choice == "Students":
        st.subheader("Students under your Mentorship:")
        your_students(email_id)
    else:
        st.subheader("About tasks")

