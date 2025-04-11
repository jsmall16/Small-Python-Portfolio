import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from spacy import displacy

st.set_page_config(page_title="Custom NER Builder", layout="wide")
st.title("🧠 Custom Entity Ruler for Taylor Swift Lyrics")

# Initialize blank spaCy English pipeline
nlp = spacy.blank("en")

# Add EntityRuler to the pipeline
ruler = nlp.add_pipe("entity_ruler")

with st.form("entity_form"):
    label = st.text_input("Entity Label (e.g., LOVE_INTEREST, CITY, ERA)").upper()
    pattern = st.text_input("Pattern to match (e.g., James, London, Reputation)")
    submitted = st.form_submit_button("Add Pattern")

    # When submitted with valid inputs, add to EntityRuler
    if submitted and label and pattern:
        new_pattern = {"label": label, "pattern": pattern}
        ruler.add_patterns([new_pattern])
        st.success(f"✅ Pattern added: `{pattern}` → `{label}`")
        
        
# Display current patterns
if ruler.patterns:
    st.markdown("### 🧾 Current Patterns:")
    for pat in ruler.patterns:
        st.write(f"- `{pat['pattern']}` → **{pat['label']}**")

# Text input method selector
st.subheader("📝 Input Your Text")
text_input_method = st.radio("Choose input method:", [
    "Sample Taylor Swift Lyrics",
    "Paste Your Own Text",
    "Upload .txt File"
])

# Default fallback
text = ""

# Sample text
if text_input_method == "Sample Taylor Swift Lyrics":
    text = "I remember it all too well. James was the boy from the Folklore era who left in the pouring rain."

# Manual paste
elif text_input_method == "Paste Your Own Text":
    text = st.text_area("Paste your lyrics or any text below:", height=200)

# File upload
else:
    uploaded_file = st.file_uploader("Upload a .txt file", type="txt")
    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")
        
        
if text:
    doc = nlp(text)

    st.subheader("🔍 Highlighted Entities")
    
    # Use spaCy's displacy to render the NER results
    html = spacy.displacy.render(doc, style="ent", jupyter=False)
    st.components.v1.html(html, height=300, scrolling=True)

    # Show entity list
    st.subheader("📋 Entity List")
    if doc.ents:
        for ent in doc.ents:
            st.write(f"- **{ent.text}** → `{ent.label_}`")
    else:
        st.info("No entities detected with current patterns.")
