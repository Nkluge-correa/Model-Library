# AudioLM

## Model Details

- Name: [AudioLM](https://arxiv.org/abs/2209.03143) 📢
- Model Size: Not specified
- Dataset: The train split of [unlab-60k](https://github.com/facebookresearch/libri-light), consisting of 60k hours of English speech
- Input/Output Format: Audio
- Research Field: Natural Language Processing, Speech Recognition
- Contains an Impact Assessment: Yes
- Associated Risks: Disinformation, Algorithmic Discrimination, Social Engineering, Environmental Impacts, Technological Unemployment
- Date of Publication: 7/26/2023
- Organization: [Google Research](https://research.google/) (Subsidiary)
- Country/Origin: United States of America
- License: Proprietary License
- Publication: [AudioLM: a Language Modeling Approach to Audio Generation](https://arxiv.org/abs/2209.03143)

## Description

[AudioLM](https://arxiv.org/abs/2209.03143) is a framework for a high-quality audio generation with long-term consistency that can map the input audio to a sequence of discrete tokens and cast audio generation as a language modeling task. According to Google Research, models trained via this framework learn to generate natural and coherent continuations given short audio prompts. Furthermore, this approach extends beyond speech by generating coherent piano music continuations, despite being trained without any symbolic representation of music.

Models trained via the AudioLM are comprised of different components: [SoundStream](https://arxiv.org/abs/2107.03312) (i.e., neural audio codec that can efficiently compress speech), [w2v-BERT](https://arxiv.org/abs/2108.06209), the k-means quantizer for w2v-BERT embeddings, and a decoder-only Transformer. Models were trained on the unlab-60k train split of [Libri-Light](https://github.com/facebookresearch/libri-light), consisting of 60k hours of English speech.

AudioLM models are not available to the public, but demos of its capabilities are exposed in the following [URL](https://google-research.github.io/seanet/audiolm/examples/).

## Organization

[Google Research](https://research.google/) is a research division of Google that focuses on advancing computer science, machine learning, artificial intelligence, and other related fields. Meanwhile, Google is a subsidiary of Alphabet Inc., a publicly traded company with multiple classes of shareholders.  
  
Google Research is responsible for developing new technologies and products that can be used by Google and its users. The division has several research areas, including natural language processing, computer vision, robotics, and more. Google Research, like other Google-related organizations, abides by [Google's AI Principles](https://ai.google/responsibility/principles/).
