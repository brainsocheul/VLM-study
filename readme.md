# VLM Study

A repository for code written while studying Vision-Language Models (VLMs).

The main purpose of this repository is to connect concepts from papers and lectures
with small hands-on implementations and exploratory tests.

This is primarily a **study repository**, rather than a collection of production-level
implementations or formal research experiments.


## Contents

### Practice

Small scripts written while learning how to use and interact with VLMs.

Topics include:

- Basic image-text inference
- Multiple-image inputs
- Question answering with visual inputs
- Inspecting model output probabilities / confidence-related values


## Exploratory Analysis

### VLM Performance on SGMRI-VQA-fixed

I conducted a small-scale exploratory evaluation using the **SGMRI-VQA**
dataset to better understand how a VLM responds to medical visual question
answering tasks.

Rather than generating new prompts, I used the questions provided in the dataset
without modification.

The dataset contained two question types:

1. **Abnormality detection**
   - Whether the given image contains an abnormal finding.

2. **Abnormality localization**
   - Where the abnormal finding is located.


### Evaluation Procedure

The evaluation followed a two-stage procedure.

For each image, the model was first asked whether an abnormality was present.

The localization question was asked only when:

- an abnormality was actually present in the image, and
- the model correctly answered that an abnormality was present.

Therefore, the second-stage analysis evaluates localization performance
**conditional on successful abnormality detection**, rather than the model's
overall ability to identify and localize abnormalities.


### What I Examined

The notebook was used to inspect:

- whether the model could correctly recognize the presence of an abnormality
- how the model described the location of an abnormal finding
- differences between detection and localization performance
- cases in which apparently plausible answers did not match the reference answer
- the extent to which model outputs appeared consistent with the provided labels


### Scope and Limitations

This was intended as an exploratory exercise rather than a formal benchmark of
medical VLM performance.

In particular:

- the original dataset questions were used without prompt optimization
- only two question types were examined
- localization was evaluated only among cases that passed the first-stage detection step
- therefore, localization results should not be interpreted as unconditional
  localization accuracy
- no conclusions about general clinical reliability can be drawn from this analysis


## Repository Structure

```text
VLM-study/
├── practice/
│   ├── vlm_basic.py
│   ├── multiple_images.py
│   ├── multiple_qna.py
│   └── probability.py
│
├── mini-project/
│   └── med_vlm_reliability.ipynb
│
├── images/
└── README.md
