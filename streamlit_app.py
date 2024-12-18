import streamlit as st
from src.knowledge_base import KnowledgeBase

# Initialize KnowledgeBase
ontology_path = r"owl/shapes_ontology.owl"
kb = KnowledgeBase(ontology_path)

# Display Title
st.title("Intelligent Tutoring System")

# Main Menu
menu = ["Get all mathematical and geometric concepts", 
        "Get formulas for a shape", 
        "Get details about a chemical element", 
        "Get all properties in the ontology"]

# Sidebar for navigation
choice = st.sidebar.selectbox("Select an option", menu)

if choice == menu[0]:
    # Get all concepts (mathematical and geometric)
    st.subheader("Mathematical and Geometric Concepts")
    concepts = kb.get_all_classes()
    for concept in concepts:
        st.write(concept)

elif choice == menu[1]:
    # Get shape formulas
    shape_name = st.text_input("Enter the name of the shape (e.g., Circle, Rectangle)")
    if shape_name:
        formulas = kb.get_shape_formulas(shape_name)
        if formulas:
            st.subheader(f"Formulas for {shape_name}:")
            for formula, comment in formulas:
                st.write(f"Formula: {formula}, Description: {comment}")
        else:
            st.write(f"No formulas found for {shape_name}.")

elif choice == menu[2]:
    # Get chemical element details
    element_name = st.text_input("Enter the name of the element (e.g., Hydrogen, Helium)")
    if element_name:
        details = kb.get_element_details(element_name)
        if details:
            st.subheader(f"Details for {element_name}:")
            for atomic_number, atomic_mass in details:
                st.write(f"Atomic Number: {atomic_number}, Atomic Mass: {atomic_mass}")
        else:
            st.write(f"No details found for element {element_name}.")

elif choice == menu[3]:
    # Get all properties in the ontology
    st.subheader("Properties in the Ontology:")
    properties = kb.get_all_properties()
    for prop in properties:
        st.write(prop)
