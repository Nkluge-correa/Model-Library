# Instructions for Submissions

1. The file's name should be the model's name (e.g., GPT-2). Check the [submissions](../submissions/) folder for examples. Also, use our [template file](../submissions/0SUBMISSION-TEMPLATE.md) to create your submission.

2. The submission file's first header must be the model's name (e.g., `# GPT-2`).

3. The first item in "Model Details" is the model name. Use markdown notation to create a hyperlink to the model's repository, model card, or paper (e.g., `[GPT-2](https://github.com/openai/gpt-2) 📚`). We also use emojis after the model hyperlink to denote model type: 📚 = works with text, 🖼️ = works with models and videos, 📢 = works with audio, 🕹️ = works with games, and 🧬 works with biological data. See the [submissions](../submissions/) folder for more examples.

4. The second item in "Model Details" is model size. You can express a range of sizes (e.g., 70M - 20B) or a single value for parameter count (175B). Model size should be accompanied by an indicator for order of magnitude (M, B, T). If this information is unavailable, use the "Not specified" string.

5. The third item in "Model Details" is the dataset. Use markdown notation to create a hyperlink to the dataset's repository, dataset card, or paper (e.g., `[WebText](https://github.com/openai/gpt-2/blob/master/domains.txt)`). You can also briefly describe such a dataset if no external source is available (e.g., "2.81T tokens from public dialog data and other public web documents"). If this information is unavailable, use the "Not specified" string.

6. The fourth item in "Model Details" is the research field tied to the model. Current options are **Reinforcement Learning**, **Computer Vision**, **Natural Language Processing**, and **Speech Recognition**. Check the [submissions](../submissions/) folder for examples if in doubt.

7. The fifth item in "Model Details" asks if an impact assessment accompanies the model on paper or a model card. Possible answers are **Yes** or **No**.

8. The sixth item in "Model Details" asks about the risks associated with a model. If a model has an impact assessment, infer the possible impacts. All identified mapped risks are in the [this](../data/risks_list.md) file. You can also base your analysis on models which perform similar functions.

9. The seventh item in "Model Details" is the model's publication date (e.g., dd/mm/yyyy). If this information is unavailable, use the "Not specified" string.

10. The eighth item in "Model Details" is the organization responsible for developing that model. Use markdown notation to create a hyperlink to the organization's homepage (e.g., `[OpenAI Inc.](https://openai.com/)`). We also add parenteses at the end, a type for that organization (e.g., `[OpenAI Inc.](https://openai.com/) (Non-profit)`). Check the [submissions](../submissions/) folder for examples if in doubt.

11. The ninth item in "Model Details" is the country of origin of that organization (e.g., United States of America). If this information is unavailable, use the "Not specified" string.

12. The tenth item in "Model Details" shows the license associated with that model (e.g., MIT). Check the [submissions](../submissions/) folder for examples if in doubt.

13. The final item in "Model Details" is a hyperlink to a publication or repository tied to that model. Use markdown notation to create the hyperlink, e.g., `[Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)`.

14. The "Description" section should describe the model. What it is, how it works, how it was developed, and how it is licensed. Maximum three paragraphs long! Use markdown notation to create these paragraphs. Check the [submissions](../submissions/) folder for examples if in doubt.

15. The "Organization" section should describe the organization behind the model. Maximum two paragraphs long! Use markdown notation to create these paragraphs. Check the [submissions](../submissions/) folder for examples if in doubt.
