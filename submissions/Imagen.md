# Imagen

## Model Details

- Name:  [Imagen](https://imagen.research.google/) 📚🖼️
- Model Size: 14B
- Dataset: 860 million text-image pairs from Google's internal datasets and the [Laion](https://huggingface.co/datasets/laion/laion400m) dataset
- Input/Output Format: Text, Image
- Research Field: Computer Vision, Natural Language Processing
- Contains an Impact Assessment: Yes
- Associated Risks: Disinformation, Algorithmic Discrimination, Environmental Impacts, Technological Unemployment
- Date of Publication: 5/23/2022
- Organization: [Google Research](https://research.google/) (Subsidiary)
- Country/Origin: United States of America
- License: Proprietary License
- Publication: [Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding](https://arxiv.org/abs/2205.11487)

## Description

[Imagen](https://imagen.research.google/) is a text-to-image diffusion model that builds on the language understanding capabilities of large transformer language models and the capacities of diffusion models to promote high-fidelity image generation.

Imagen uses a large frozen [T5-XXL](https://huggingface.co/google/t5-efficient-xxl) encoder to encode the input text into embeddings. Then, a conditional diffusion model maps the text embedding into a 64×64 image. Imagen further utilizes text-conditional super-resolution diffusion models to upsample the 64×64 image to 256×256, and later to 1024×1024.

Imagen is a text-to-image model that has not been released for public use due to concerns regarding responsible open-sourcing of code and demos.

## Organization

[Google Research](https://research.google/) is a research division of Google that focuses on advancing computer science, machine learning, artificial intelligence, and other related fields. Meanwhile, Google is a subsidiary of Alphabet Inc., a publicly traded company with multiple classes of shareholders.  
  
Google Research is responsible for developing new technologies and products that can be used by Google and its users. The division has several research areas, including natural language processing, computer vision, robotics, and more. Google Research, like other Google-related organizations, abides by [Google's AI Principles](https://ai.google/responsibility/principles/).
