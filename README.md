# ParagraphGrader

# Automated Paragraph Grading System

This project implements an automated system for grading written paragraphs using Natural Language Processing (NLP) and Machine Learning techniques. The system evaluates paragraphs based on various linguistic features such as grammar, spelling, sentence structure, and vocabulary usage to assign a grade.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [File Structure](#file-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Training the Model](#training-the-model)
  - [Grading a Paragraph](#grading-a-paragraph)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

The Automated Paragraph Grading System leverages NLP to extract meaningful features from written text and utilizes a machine learning classifier to predict the quality of the paragraph. This system can be used in educational settings to provide quick and consistent feedback to students or as a tool for writers to assess their work.

## Features

- **Feature Extraction:** Analyzes paragraphs to extract features such as the number of sentences, word count, unique words, capitalization errors, misspelled words, and grammar mistakes.
- **Machine Learning Classifier:** Uses a Stochastic Gradient Descent (SGD) classifier to predict grades based on extracted features.
- **Customizable Stop Words:** Allows the inclusion of custom stop words to refine feature extraction.
- **Model Persistence:** Saves and loads trained models for reuse without retraining.

## File Structure
├── clf.object ├── featureExtractor.py ├── featureExtractorOrig.py ├── featureExtractororg.py ├── featureExtractor.pyc ├── grade.py ├── stopwords.txt ├── training.py ├── weights.txt └── README.md


### File Descriptions

- **`training.py`**
  - Reads training data from `trainingData.txt`.
  - Extracts features from each paragraph.
  - Trains the SGDClassifier.
  - Saves the trained model to `clf.object`.

- **`grade.py`**
  - Loads the trained classifier from `clf.object`.
  - Reads a paragraph from `checkData.txt`.
  - Extracts features from the paragraph.
  - Predicts and assigns a grade based on the features.

- **`featureExtractor.py`**
  - Contains functions to extract various linguistic features from text.
  - Utilizes NLTK for tokenization and other NLP tasks.
  - Checks for grammar and spelling errors using `language_check` and `enchant`.

- **`stopwords.txt`**
  - A list of additional stop words to be excluded during feature extraction.

- **`clf.object`**
  - Serialized file containing the trained machine learning model.

- **`weights.txt`**
  - (Assumed) May contain weight information for features or model parameters.

- **`featureExtractorOrig.py`, `featureExtractororg.py`, `featureExtractor.pyc`**
  - Different versions or compiled versions of the feature extractor script.

## Installation

### Prerequisites

- Python 3.x
- Pip package manager

### Required Python Libraries

Install the necessary Python libraries using the provided `requirements.txt`:

```bash
pip install -r requirements.txt
