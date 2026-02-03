import streamlit as st

# Function to perform the calculations
def calculate(num1, num2, operation):
    if operation == "➕":
        return num1 + num2
    elif operation == "➖":
        return num1 - num2
    elif operation == "✖":
        return num1 * num2
    elif operation == "➗":
        if num2 == 0:
            return None  # We'll handle this case separately
        return num1 / num2

# Streamlit UI setup
st.title("📱 Simple Calculator App")  # Added a calculator emoji in the title
st.subheader("A user-friendly calculator built with Streamlit")  # Subtitle

# Input fields for numbers
num1 = st.number_input("Enter the first number:", min_value=None, step=1, format="%d")
num2 = st.number_input("Enter the second number:", min_value=None, step=1, format="%d")

# Dropdown to select the operation
operation = st.selectbox("Select an operation:", options=["➕", "➖", "✖", "➗"])

# Error handling and validation
if operation == "➗" and num2 == 0:
    # If division is selected and the second number is zero, show a warning and disable the button
    st.warning("Divided by zero is not allowed!")
    calculate_button = False  # Disable button (we don't need to calculate)
else:
    # Enable the calculate button
    calculate_button = st.button("Calculate")

# Handling the button click and displaying results
if calculate_button:
    result = calculate(num1, num2, operation)
    
    # Show the result if it's not None (None means division by zero)
    if result is None:
        st.warning("Divided by zero is not allowed!")  # Warning when dividing by zero
    else:
        st.subheader(f"Result: {result}")

