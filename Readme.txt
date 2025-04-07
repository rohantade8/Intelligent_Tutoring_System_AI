# Intelligent Tutoring System (ITS)

An **Intelligent Tutoring System (ITS)** that provides a user-friendly interface for querying **mathematical**, **geometric**, and **chemical** knowledge from an ontology. The system offers both a terminal-based and a **Streamlit**-powered web interface for interaction.

---

## 🚀 **Features**

-   📚 **Mathematical & Geometric Concepts** – Retrieve all available concepts in the ontology.
-   📐 **Shape Formulas** – Get formulas related to specific shapes (e.g., Circle, Rectangle).
-   🧪 **Chemical Elements** – Get element details like atomic number and atomic mass.
-   🔍 **Ontology Properties** – Explore all defined properties (e.g., `hasRadius`, `hasArea`).
-   🗂️ **Shape Listing** – List all shapes in the ontology with labels.
-   🌐 **Streamlit Frontend** – Web interface for easy, interactive exploration.

---

## ⚙️ **Prerequisites**

Make sure you have the following installed:

-   Python 3.x
-   [rdflib](https://pypi.org/project/rdflib/) – for RDF graph handling
-   [Streamlit](https://streamlit.io/) – for the web UI

Install the dependencies using:

```bash
pip install rdflib streamlit
```

Also, make sure you have an ontology file in `.owl` format placed at:

```
<project_root>/owl/shapes_ontology.owl
```

If it's located elsewhere, update the `ontology_path` in the code accordingly.

---

## 📁 **Project Structure**

```plaintext
intelligent-tutoring-system/
│
├── owl/
│    └── shapes_ontology.owl         # Ontology file (RDF/XML)
│
├── src/
│    ├── knowledge_base.py           # Handles ontology interaction
│    ├── main.py                     # Terminal-based interface
│    └── streamlit_app.py            # Web-based frontend using Streamlit
│
├── .gitignore                      # Optional
├── requirements.txt                  # Required packages
├── README.md                        # Project documentation
└── LICENSE                         # Optional
```

---

## 🧪 **How to Use**

### 1. **Clone the Repository**

```bash
git clone <repository_url>
cd intelligent-tutoring-system
```

### 2. **Place the Ontology File**

Copy your `shapes_ontology.owl` file into the `owl/` directory.

---

### 3. **Run the Terminal Interface (Optional)**

```bash
python src/main.py
```

This will launch an interactive terminal menu for exploration.

---

### 4. **Run the Streamlit Frontend**

```bash
cd src/
streamlit run streamlit_app.py
```

The app will launch in your default web browser.

---

### 5. **Interact with the System**

From the Streamlit interface, you can:

-   View all mathematical/geometric concepts
-   Get shape-specific formulas
-   Retrieve chemical element details
-   View all ontology properties
-   List all defined shapes

---

### 6. **Exit**

Close the terminal or stop the Streamlit server with `Ctrl+C`.

---

## 🧠 **Code Overview**

### `knowledge_base.py`

Handles RDF ontology interactions using `rdflib`.

-   `get_all_classes()`
-   `get_all_shapes()`
-   `get_shape_formulas(shape_name)`
-   `get_element_details(element_name)`
-   `get_all_properties()`

---

### `main.py`

A CLI-based interface to interact with the system via a menu-driven console.

---

### `streamlit_app.py`

Streamlit-based GUI for querying and displaying information.

-   **Selectbox** – Choose actions
-   **Text Input** – Enter shape or element name
-   **Display Area** – Shows query results

---

## 🛠 **Troubleshooting**

-   **No Formulas Found**: Ensure the shape is correctly defined in the ontology.
-   **Shape Not Listed**: Check if the ontology file is correctly loaded.
-   **Invalid Choices**: Follow the on-screen prompts and provide valid inputs.

---

## 📌 **Future Improvements**

-   Add advanced and customizable SPARQL queries
-   Enhance the UI with libraries like **Tkinter**, **Flask**, or **Django**
-   Expand ontology to include broader subject areas

---

## 📄 **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
