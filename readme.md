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


### Exploratory Analysis

#### VLM Output Consistency and Confidence

I conducted a small exploratory analysis in Google Colab to better understand
how much confidence can be placed in VLM outputs.

The notebook examines examples such as:

- how responses change across similar prompts
- consistency of answers across repeated queries
- model behavior with multiple visual inputs
- the relationship between generated answers and available probability/confidence information

The goal was not to establish the reliability of VLMs statistically,
but to understand practical limitations that may not be obvious from simply running inference.


## What I Learned

Through these exercises, I became more familiar with:

- how visual and textual inputs are passed to a VLM
- how model outputs can vary depending on prompt formulation and input structure
- why an apparently confident model response should not automatically be interpreted as a reliable answer
- the difference between qualitative observations and conclusions that would require systematic evaluation
- practical considerations when designing an evaluation of model reliability


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
