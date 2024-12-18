**#Intelligent Tutoring System (ITS)**

This project is an Intelligent Tutoring System (ITS) that provides a user-friendly interface for querying mathematical, geometric, and chemical knowledge from an ontology. It allows users to explore various concepts, formulas, and elements through both a terminal-based interface and a **Streamlit** frontend.

## Features
- **Mathematical and Geometric Concepts**: Retrieve all available mathematical and geometric concepts in the ontology.
- **Shape Formulas**: Get formulas related to specific shapes (e.g., Circle, Rectangle).
- **Chemical Elements**: Retrieve details of chemical elements, such as their atomic number and atomic mass.
- **Properties**: Get a list of all properties in the ontology (e.g., hasRadius, hasArea).
- **Shape Listing**: List all shapes in the ontology with their labels.
- **Streamlit Frontend**: A web-based interface for easy interaction with the system.

## Prerequisites

Ensure the following dependencies are installed before running the system:

- Python 3.x
- **rdflib** library (for RDF graph handling)
- **Streamlit** (for the web-based frontend)

To install the necessary dependencies, you can use the following command:

```bash
pip install rdflib streamlit
```

Additionally, you will need an ontology file in `.owl` format. The project uses the following ontology path:

```
<path_to_ontology>/shapes_ontology.owl
```

Make sure the ontology file is correctly placed in the specified directory, or update the `ontology_path` in the code if you place the file elsewhere.

## File Structure

```plaintext
intelligent-tutoring-system/
│
├── owl/
│   ├── shapes_ontology.owl         # Ontology file (RDF/XML)
│
├── src/
│   ├── knowledge_base.py           # Python module to interact with the ontology
│   ├── main.py                     # Main script to run the ITS application (terminal-based)
│   ├── streamlit_app.py            # Streamlit frontend
│
├── .gitignore                      # Git ignore file (optional)
├── requirements.txt                # Python dependencies
├── README.md                       # This file
└── LICENSE                         # License file (optional)
```

## How to Use

### 1. Clone the Repository

If you haven't already cloned the repository:

```bash
git clone <repository_url>
cd intelligent-tutoring-system
```

### 2. Set up the Ontology

Place your ontology file (`shapes_ontology.owl`) in the `owl/` directory. This ontology file should contain the required classes, formulas, and element data.

### 3. Run the Terminal-based ITS (Optional)

To run the ITS in the terminal, execute the `main.py` script in the `src/` directory:

```bash
python src/main.py
```

This will present a menu for the user to interact with the system.

### 4. Run the Streamlit Frontend

For a web-based interface, you can use **Streamlit**. Here's how to set up and run the **Streamlit** frontend:

1. Navigate to the `src/` directory:

   ```bash
   cd src/
   ```

2. Start the Streamlit app:

   ```bash
   streamlit run streamlit_app.py
   ```

3. Streamlit will open the web-based interface in your default web browser.

### 5. Interact with the System

The web interface will allow you to:

- **Get all mathematical and geometric concepts**
- **Get formulas for a specific shape**
- **Get details about a chemical element (e.g., Hydrogen, Helium)**
- **Get all properties in the ontology**
- **Get a list of all shapes in the ontology**

### 6. Exit the System

To exit the system, simply close the terminal or stop the Streamlit server.

## Code Overview

### `knowledge_base.py`
This module handles the interaction with the ontology, providing methods to query classes, formulas, properties, and elements.

- **Methods**:
  - `get_all_classes()`: Retrieves all the classes in the ontology (mathematical and geometric concepts).
  - `get_all_shapes()`: Retrieves all the shapes in the ontology along with their labels.
  - `get_shape_formulas(shape_name)`: Retrieves formulas for a given shape.
  - `get_element_details(element_name)`: Retrieves details about a chemical element.
  - `get_all_properties()`: Retrieves all properties (e.g., hasRadius, hasArea) in the ontology.

### `main.py`
This is the main entry point for running the Intelligent Tutoring System in the terminal. It provides a menu for the user to select different options and interact with the system.

### `streamlit_app.py`
This file contains the Streamlit frontend. It provides an interactive web interface where users can query mathematical, geometric, and chemical information from the ontology.

- **Streamlit Components**:
  - **Selectbox**: For selecting the action (get concepts, get formulas, etc.).
  - **Text Input**: For entering the name of a shape or element.
  - **Display Output**: Dynamically displays results of queries.

### Running the Streamlit App

When you run the Streamlit app (`streamlit_app.py`), you will see the following components:

- **Select Action**: Allows you to choose whether to get concepts, formulas, element details, or properties.
- **Text Input**: Allows you to enter a shape name or element name based on the selected action.
- **Results**: The relevant results from the ontology will be displayed below.

## Troubleshooting

- **No Formulas Found**: If no formulas are found for a shape, ensure that the shape is correctly defined in the ontology and linked to the relevant formulas.
- **Shape Not Listed**: If a shape doesn't appear in the list, verify that the shape is correctly defined in the ontology and that the ontology path is correct.
- **Invalid Choices**: If you encounter an invalid input, make sure to follow the menu options and input valid choices.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Future Improvements

- **Add more complex queries**: Enhance the system with more advanced querying capabilities.
- **Improve User Interface**: Create a graphical user interface (GUI) using libraries like Tkinter or a more sophisticated web-based UI with Flask or Django.
- **Expand Ontology**: Add more concepts, formulas, and elements to make the system even more powerful.

---

This README now includes details about running the **Streamlit** frontend along with instructions for the terminal-based system. It also provides clear guidelines for setting up, interacting with, and troubleshooting the system.
