# Parti

## Model Details

- Name: [Parti](https://github.com/google-research/parti) 📚🖼️
- Model Size: 20B
- Dataset: [LAION-400M dataset](https://huggingface.co/datasets/laion/laion400m), [ALIGN training data](https://arxiv.org/abs/2102.05918), and the [JFT-4B dataset](https://paperswithcode.com/paper/scaling-vision-transformers)
- Input/Output Format: Text, Image
- Research Field: Computer Vision, Natural Language Processing
- Contains an Impact Assessment: Yes
- Associated Risks: Disinformation, Algorithmic Discrimination, Environmental Impacts, Technological Unemployment
- Date of Publication: 6/22/2022
- Organization: [Google Research](https://research.google/) (Subsidiary)
- Country/Origin: United States of America
- License: Proprietary License
- Publication: [Scaling Autoregressive Models for Content-Rich Text-to-Image Generation](https://arxiv.org/abs/2206.10789)

## Description

Pathways Autoregressive Text-to-Image model ([Parti](https://github.com/google-research/parti)) is a series of autoregressive text-to-image generation models, from 350M to 20B parameters,  that achieves high-fidelity photorealistic image generation. Unlike Google’s [Imagen](https://imagen.research.google/), a diffusion model, Parti is an autoregressive model.  
  
Parti treats text-to-image generation as a sequence-to-sequence modeling problem, analogous to machine translation – which allows it to benefit from advances in large language models, especially capabilities that are unlocked by scaling data and model sizes. In this case, the target outputs are sequences of image tokens instead of text tokens in another language. Parti uses an image tokenizer, [ViT-VQGAN](https://ai.googleblog.com/2022/05/vector-quantized-image-modeling-with.html), to encode images as sequences of discrete tokens, and then reconstructs the image token sequences as images.

Parti models, code, and data are not available to the public.

## Organization

[Google Research](https://research.google/) is a research division of Google that focuses on advancing computer science, machine learning, artificial intelligence, and other related fields. Meanwhile, Google is a subsidiary of Alphabet Inc., a publicly traded company with multiple classes of shareholders.  
  
Google Research is responsible for developing new technologies and products that can be used by Google and its users. The division has several research areas, including natural language processing, computer vision, robotics, and more. Google Research, like other Google-related organizations, abides by [Google's AI Principles](https://ai.google/responsibility/principles/).
