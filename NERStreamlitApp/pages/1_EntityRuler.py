# Import necessary Libraries 
import pandas as pd
import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from spacy import displacy


# Set title and images
st.title("Custom NER for Taylor Swift Lyrics")
st.image("NERStreamlitApp/pages/TS_Words.jpeg")

# Intro Text
st.write("""
Welcome to the Swiftie Named Entity Recognition builder, a place to turn Taylor Swift lyrics 
into custom insights. Add your own rules, define who or what matters, and watch your entities appear like magic!
""")

# Saves entity patterns across interactions
if "saved_patterns" not in st.session_state:
    st.session_state.saved_patterns = []

# Entity Pattern Input
st.subheader("Add Custom Entity Patterns")
st.write("""
Start by creating custom labels and keywords you want to recognize. 
For example, label "LOVE_INTEREST" and match patterns like "James" or "Tom".
""")

with st.form("add_patterns"): # Creates a form in streamlit
    # Creates a text input field where the user types in the label for their entity 
    label = st.text_input("Entity Label (e.g. CITY)")
    # User types in the matching pattern
    pattern_input = st.text_input("Patterns (London)")
    add = st.form_submit_button("Add Patterns") # form submits when users press button

    if add and label and pattern_input: # Makes sure user clicked button and entered a pattern/label
        # Convert pattern string into token-based spaCy pattern (case-insensitive)
        token_pattern = [{"LOWER": token.lower()} for token in pattern_input.strip().split()]
        st.session_state.saved_patterns.append({"label": label, "pattern": token_pattern}) # stores the pattern and label
        st.success(f"Added `{pattern_input}` to `{label}`") # confirm addition 

# Show saved patterns
if st.session_state.saved_patterns:
    st.markdown("### Saved Entity Patterns") 
    st.write("Here are the rules you've added so far:")
    df = pd.DataFrame([
    {"label": pattern["label"], "pattern": str(pattern["pattern"])}
    for pattern in st.session_state.saved_patterns
    ])

# Text Input Section 

# Intro 
st.subheader("Input Text")
st.write("""
Now choose how you'd like to input text for entity recognition. 
You can use a sample Taylor lyric, paste your own, or upload a `.txt` file.
""")

# Let user choose how they want to input their text
text_method = st.radio("Choose input method:", ["Sample Lyrics", "Paste Text", "Upload .txt File"])

# Initialize an empty string for the text
text = ""

# Option 1: Use sample Lyrics from Taylor Swift's Song London Boy
if text_method == "Sample Lyrics":
    text = "You know I love a London boy. I enjoy walking Camden Market in the afternoon. He likes my American smile. Like a child when our eyes meet, darling, I fancy you."

# Option 2: Allow a user to manually import text
elif text_method == "Paste Text":
    text = st.text_area("Paste your text below:", height=200)

# Option 3: Allow the user to upload a txt file
elif text_method == "Upload .txt File":
    uploaded_file = st.file_uploader("Upload a .txt file", type="txt")
    # If a file is uploaded, decode its content to readable Python text
    if uploaded_file:
        text = uploaded_file.read().decode("utf-8")

#  Run spaCy NER 

# Check if there's any text to process
if text:
    # Create blank spaCy english pipeline
    nlp = spacy.blank("en")
    # add the entity ruler to the pipeline
    ruler = nlp.add_pipe("entity_ruler")
    # add all user_defined patterns
    if st.session_state.saved_patterns:
        ruler.add_patterns(st.session_state.saved_patterns)

    # Apply the pipeline to the input text
    doc = nlp(text)

    # Display original text
    st.subheader("Full Text")
    st.write(text)

    # Visualize entities with displacy 
    st.subheader("Highlighted Entities")
    # Make the text white 
    st.markdown("""
        <style>
        .entities {
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    # Renders entities and makes sure they're visible using dark mode 
    html = displacy.render(doc, style="ent", jupyter=False)
    wrapped_html = f"<div style='color: white;'>{html}</div>"
    st.components.v1.html(wrapped_html, height=300, scrolling=True)

    # List of Detected Entities
    st.subheader("✅ Entity List")
    st.write("Here’s a breakdown of the entities found:")
    
    # If any entities were found, display them 
    if doc.ents:
        for ent in doc.ents:
            st.markdown(f"""
                **Text:** `{ent.text}`  
                **Label:** `{ent.label_}` 
                **Start Pos:** {ent.start_char} | **End Pos:** {ent.end_char}
                        """)
    else:
        st.info("No entities found.")
