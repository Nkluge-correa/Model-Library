# CLIP

## Model Details

- Name: [CLIP](https://openai.com/blog/clip/) 📚🖼️
- Model Size: Not specified
- Dataset: Trained on publicly available image-caption data
- Input/Output Format: Text, Image
- Research Field: Computer Vision, Natural Language Processing
- Contains an Impact Assessment: Yes
- Associated Risks: Algorithmic Discrimination, Surveillance and Social Control, Environmental Impacts
- Date of Publication: 2/26/2021
- Organization: [OpenAI Inc.](https://openai.com/) (Non-profit)
- Country/Origin: United States of America
- License: MIT License
- Publication: [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)

## Description

[CLIP](https://openai.com/blog/clip/) (Contrastive Language-Image Pre-training) is a neural network capable of associating natural language snippets with images, learning the relationship between sequences of tokens and images. According to its [model card](https://github.com/openai/CLIP/blob/main/model-card.md#model-type), "_the base model uses a ResNet50 with several modifications as an image encoder and uses a masked self-attention Transformer as a text encoder. These encoders are trained to maximize the similarity of (image, text) pairs via a contrastive loss. There is also a variant of the model where the ResNet image encoder is replaced with a Vision Transformer_."
  
According to its developers, one of the critical insights behind the CLIP model was to leverage natural language as a flexible prediction space, thus allowing for greater generalization and transfer. Hence, CLIP can be instructed in natural language, with a simple prompt agnostic training task, without needing specific phrases and labeled images.

The dataset used to train CLIP has 400 million records split between images and text collected from the internet. CLIP has been evaluated on 30 benchmarks, covering tasks like OCR, video recognition, geolocation, and other fine-grained object classification tasks. Like other foundation models, by not directly optimizing for a given benchmark/task, CLIP proves to be more general. CLIP is open source and can be used following the [linked tutorial](https://github.com/openai/CLIP).

## Organization

[OpenAI](https://openai.com/) is an American artificial intelligence research laboratory consisting of the non-profit OpenAI, Inc. and its for-profit subsidiary corporation OpenAI, L.P, founded in 2015 by Ilya Sutskever, Greg Brockman, Trevor Blackwell, Vicki Cheung, Andrej Karpathy, Durk Kingma, Jessica Livingston, John Schulman, Pamela Vagata, and Wojciech Zaremba. Their mission "_is to ensure that General Artificial Intelligence benefits all of humanity_."  
  
The organization maintains an active research and development agenda in AI Safety. In "_[Our approach to AI safety](https://openai.com/blog/our-approach-to-ai-safety)_", OpenAI states that it is committed to keeping Artificial Intelligence safe and broadly beneficial.
