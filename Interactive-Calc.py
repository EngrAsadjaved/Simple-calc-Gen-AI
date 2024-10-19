# Import necessary library
import streamlit as st

# Define calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero!"

# Streamlit interface
st.set_page_config(page_title="Interactive Calculator", page_icon="🧮")

# App Title
st.title("🧮 Simple Interactive Calculator")

# Sidebar for selecting the operation
st.sidebar.header("Choose an operation")
operation = st.sidebar.radio(
    "Select the operation you want to perform:", 
    ("Add", "Subtract", "Multiply", "Divide")
)

# Sidebar for input numbers
st.sidebar.header("Input Numbers")
num1 = st.sidebar.number_input("Enter the first number:", format="%f")
num2 = st.sidebar.number_input("Enter the second number:", format="%f")

# Perform calculation and display result
if st.sidebar.button("Calculate Now!"):
    with st.spinner("Calculating..."):
        if operation == "Add":
            result = add(num1, num2)
            st.success(f"✅ The result of addition is: **{result}**")
        elif operation == "Subtract":
            result = subtract(num1, num2)
            st.success(f"✅ The result of subtraction is: **{result}**")
        elif operation == "Multiply":
            result = multiply(num1, num2)
            st.success(f"✅ The result of multiplication is: **{result}**")
        elif operation == "Divide":
            result = divide(num1, num2)
            if isinstance(result, str):  # Error case for division by zero
                st.error(result)
            else:
                st.success(f"✅ The result of division is: **{result}**")
else:
    st.info("👈 Enter the numbers and choose the operation from the sidebar, then hit 'Calculate Now!'")

# Footer
st.markdown("---")
st.write("Deployed by **Engr. Asad Javed**")
st.write("Developed by [Engr. Asad Javed](https://github.com/yourprofile)")

# Option for resetting values
if st.sidebar.button("Reset"):
    st.experimental_rerun()
