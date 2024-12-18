from knowledge_base import KnowledgeBase

def display_menu():
    """Display the main menu options for the user."""
    print("\nWelcome to the Intelligent Tutoring System!")
    print("1. Get all mathematical and geometric concepts")
    print("2. Get formulas for a shape")
    print("3. Get details about a chemical element")
    print("4. Get all properties in the ontology")
    print("5. Exit")

def handle_user_input(kb):
    """Handle user input and interact with the knowledge base."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            print("\nMathematical and Geometric Concepts:")
            concepts = kb.get_all_classes()
            for concept in concepts:
                print(concept)
        
        elif choice == '2':
            shape_name = input("\nEnter the name of the shape (e.g., Circle, Rectangle): ")
            formulas = kb.get_shape_formulas(shape_name)
            if formulas:
                print(f"\nFormulas for {shape_name}:")
                for formula, comment in formulas:
                    print(f"Formula: {formula}, Description: {comment}")
            else:
                print(f"No formulas found for {shape_name}.")

        elif choice == '3':
            element_name = input("\nEnter the name of the element (e.g., Hydrogen, Helium): ")
            details = kb.get_element_details(element_name)
            if details:
                for atomic_number, atomic_mass in details:
                    print(f"Atomic Number: {atomic_number}, Atomic Mass: {atomic_mass}")
            else:
                print(f"No details found for element {element_name}.")
        
        elif choice == '4':
            print("\nProperties in the ontology:")
            properties = kb.get_all_properties()
            for prop in properties:
                print(prop)
        
        elif choice == '5':
            print("\nExiting the Intelligent Tutoring System. Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

def main():
    """Main function to initialize the ITS and run it."""
    # Update the path to the ontology file
    ontology_path = r"C:\Users\Acer\Desktop\Intelligent Tutoring System\owl\shapes_ontology.owl"
    kb = KnowledgeBase(ontology_path)
    handle_user_input(kb)

if __name__ == "__main__":
    main()
