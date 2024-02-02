# Muse

## Model Details

- Name: [Muse](https://muse-model.github.io/) 📚🖼️
- Model Size: 3B
- Dataset: [Imagen](https://imagen.research.google/) dataset consisting of 460M text-image pairs
- Input/Output Format: Text, Image
- Research Field: Computer Vision, Natural Language Processing
- Contains an Impact Assessment: Yes
- Associated Risks: Disinformation, Algorithmic Discrimination, Environmental Impacts, Technological Unemployment
- Date of Publication: 1/2/2023
- Organization: [Google Research](https://research.google/) (Subsidiary)
- Country/Origin: United States of America
- License: Proprietary License
- Publication: [Muse: Text-To-Image Generation via Masked Generative Transformers](https://arxiv.org/abs/2301.00704)

## Description

[Muse](https://muse-model.github.io/) is a text-to-image Transformer model trained on a masked modeling task, i.e., given the text embedding extracted from a pre-trained large language model (LLM), Muse is trained to predict randomly masked image tokens, similar to what language models trained via MLM (masked language modeling), like BERT and RoBERTa do. Muse models achieve SOTA on benchmarks like CC3M and COCO, being also able to directly enable several image editing applications without the need to fine-tune or invert the model.

Muse models come in a size range from 632M parameters to 3B parameters. Each model consists of several sub-models: (1) a pair of VQGAN tokenizer models that can encode an input image to a sequence of discrete tokens as well as decode a token sequence back to an image; (2) a base masked image model conditioned on the unmasked tokens and a T5XXL; and (3) a "_superres_" transformer model which translates (unmasked) low-res tokens into high-res tokens (also conditioned on the unmasked tokens and a T5XXL).

Muse models are not open to the public, but a demo can be found in this [URL](https://muse-model.github.io/).

## Organization

[Google Research](https://research.google/) is a research division of Google that focuses on advancing computer science, machine learning, artificial intelligence, and other related fields. Meanwhile, Google is a subsidiary of Alphabet Inc., a publicly traded company with multiple classes of shareholders.  
  
Google Research is responsible for developing new technologies and products that can be used by Google and its users. The division has several research areas, including natural language processing, computer vision, robotics, and more. Google Research, like other Google-related organizations, abides by [Google's AI Principles](https://ai.google/responsibility/principles/).
