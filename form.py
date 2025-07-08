import streamlit as st
import query as f

def validate_form(first_name, last_name, enrollment):
    errors = []
    if not first_name.strip():
        errors.append("First name is required.")
    if not last_name.strip():
        errors.append("Last name is required.")
    if not enrollment.strip():
        errors.append("Enrollment number is required.")
    elif not enrollment.isdigit():
        errors.append("Enrollment number must be numeric.")
    return errors

def main():
    st.set_page_config(page_title="Student Form", layout="centered")
    st.title("📝 Student Form")
    
    # Initialize session state for form visibility
    if 'show_form' not in st.session_state:
        st.session_state.show_form = False
    
    # Main form toggle button
    if st.button("Form", type="primary"):
        st.session_state.show_form = not st.session_state.show_form
    
    # Only show form if toggled on
    if st.session_state.show_form:
        with st.form("student_form"):
            st.subheader("Enter Your Details")
            
            col1, col2 = st.columns(2)
            with col1:
                first_name = st.text_input("First Name*", key="first_name")
            with col2:
                last_name = st.text_input("Last Name*", key="last_name")
            
            enrollment = st.text_input("Enrollment Number*", key="enrollment")
            submitted = st.form_submit_button("Submit")
            
            if submitted:
                errors = validate_form(first_name, last_name, enrollment)
                
                if errors:
                    for error in errors:
                        st.error(error)
                else:
                    f.insert_data(first_name, last_name, enrollment)
                    st.success("✅ Submitted successfully!")
                    st.write(f"**Name:** {first_name} {last_name}")
                    st.write(f"**Enrollment:** {enrollment}")
                    
                    # Optionally clear session state
                    st.session_state.show_form = False

if __name__ == "__main__":
    main()
    
