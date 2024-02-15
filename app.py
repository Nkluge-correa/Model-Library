import gradio as gr
from datasets import load_dataset

db = load_dataset("nicholasKluge/model-library", split='main')
db = db.to_pandas()

def display_model_information(value):
    """
    This function will display the model information for the selected model
    """
    # If the value is empty, return None
    if value == '':
        return None, None

    # Get the model information
    info = db.iloc[int(db[db.model_name_string == value].index.values)]
    
    # Create the model details and model info
    model_details = f"""## Model Details

- Name: {info.model_name_url}
- Model Size: {info.model_size_string}
- Dataset: {info.dataset}
- Input/Output Format: {info.data_type}
- Research Field: {info.research_field}
- Contains an Impact Assessment: {info.risks_and_limitations}
- Associated Risks: ☣️ {info.risk_types} ☣️
- Date of Publication: {info.publication_date}
- Organization: {info.organization_and_url}
- Country/Origin: {info.country}
- License: {info.license}
- Publication: {info.paper_name_url}
"""
    model_info = f"""## Description

{info.model_description}

## Organization

{info.organization_info}
"""

    return model_details, model_info

with open('data/risks_list.md', 'rb') as f:
    risk_text = f.read().decode('utf-8')[44:]

with gr.Blocks(theme='HaleyCH/HaleyCH_Theme') as demo:

    gr.Markdown("""<h1><center>Model Library</h1></center>""")

    gr.HTML("""<center><img src="file/assets/logo.png" width="200" height="200"></center>""")

    gr.HTML(f"<center><div style='max-width: 50%;'>The Model Library is a project that maps the risks associated with modern machine \
        learning systems. Here, we assess some of the most recent and capable AI systems ever created. \
            We have already mapped {len(db)} models from the AI community!</div></center>")

    dropdown = gr.Dropdown(
        choices=db.model_name_string.tolist(),
        label="Choose a model", 
        info="These are the models we have already produced reports."
    )

    display = gr.Button(value="Display")

    with gr.Row():
        with gr.Column(scale=1):
            model_details = gr.Markdown()
        with gr.Column(scale=4):
            model_info = gr.Markdown()
    
    with gr.Accordion(label="Mapped Risks", open=False):
        gr.Markdown(risk_text)
    
    gr.HTML(f"<center><div style='max-width: 50%;'>If you would like to add a model, read our\
        documentation and submit a PR on <a href='https://github.com/Nkluge-correa/Model-Library' \
            target='_blank'>GitHub</a>!</div></center>")
    
    display.click(fn=display_model_information, inputs=dropdown, outputs=[model_details, model_info])
    

demo.launch(debug=True, favicon_path="file/assets/favicon.ico")