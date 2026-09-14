# VLM Study

Vision-Language Model을 공부하면서 작성한 실습 코드와 간단한 실험을 정리한 저장소입니다.

## 📚 Study Topics

- Vision-Language Models
- Image-Text Understanding
- Multiple Image Input
- Question Answering
- Model Confidence / Probability

## 📁 Repository Structure

```text
VLM-study/
├── practice/
│   ├── basic_vlm.py
│   ├── multiple_images.py
│   ├── multiple_qna.py
│   └── probability.py
│
├── mini-project/
│   └── med_vlm_reliability.ipynb/
│
├── images/
└── README.md

##🧪 Experiments
VLM Reliability Experiment
VLM이 출력하는 답변과 confidence가 실제로 얼마나 신뢰할 수 있는지 간단한 실험을 진행했습니다.
실험 내용:
- 동일한 질문 반복
- 여러 이미지 입력
- 답변 consistency 확인
- probability / confidence 비교
자세한 내용은 아래 notebook에 정리했습니다.
mini-project/med_vlm_reliability.ipynb
🛠 Tech Stack
- Python
- PyTorch
- Google Colab
- Visual Studio Code
- Git / GitHub
##🎯 Purpose
VLM과 딥러닝 모델의 구조를 이해하고, 논문에서 배운 내용을 실제 코드와 실험으로 연결하는 것을 목표로 합니다.

## 💡 What I Learned

- VLM이 생성하는 confidence가 항상 실제 정답 가능성을 의미하지는 않는다.
- 동일한 입력에서도 질문 방식에 따라 출력이 달라질 수 있다.
- Multiple image 입력에서 모델의 reasoning consistency를 확인할 필요가 있다.
