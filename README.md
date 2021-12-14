# Tutorial for DS04 - MRS Spring 2022
See symposium session [link](https://www.mrs.org/meetings-events/spring-meetings-exhibits/2022-mrs-spring-meeting/call-for-papers/detail/2022_mrs_spring_meeting/ds04/Symposium_DS04)

## About
This repo includes the tutorial materials for the MRS Spring 2022 - DS04 tutorial on MLOps. The tutorial description is copied below:

> The ability to leverage machine learning (ML) is rapidly becoming a part of the material scientist’s
toolkit, whether for aiding ab initio computational work, screening datasets of candidate materials, or
interfacing with in-lab experimenters and equipment. This tutorial aims to address the problems that
frequently arise after a materials scientist builds their first few successful ML models: How can multiple
versions of models, and their predictions, be effectively tracked? Are there ways to automatically test
models before running large batch predictions?
>
> This tutorial will use case studies from recent work in combinatorial science and materials screening to
present an interactive Python tutorial for participants. Familiarity with basic machine learning
principles along with Git version control are recommended for participation in this tutorial.

## Learning Outcomes

+ The concept of using correlation IDs to track models and predictions, which is a best-practice
from large scale ML in the (web-based) technology industry.
+ Using automated workflow tools, such as the free Github Actions, to automate testing and
sanity checks for ML models before time and resources are committed for large predictions.
+ A short survey of ML systems design principles, including:
  + logging ML parameters with experiment-tracking libraries (e.g., MLflow),
  + packaging Python dependencies to improve reproducibility,
  + orchestrating ML pipelines to allow partial restarts (e.g., re-run predictions without
retraining) and easier debugging.

## Contents

In lieu of slides, this tutorial uses interactive Jupyter notebooks. These notebooks will be stepped through during the tutorial with opportunities for Q&A throughout. The tutorial considers three mock (but realistic!) scenarios:

1. In a **ML-driven materials screening experiment**, you've made updates to an ML model after you've already started working with some of your screened materials. How will you track, manage, and reconcile different screening "runs" produced by different ML models?
2. Some scientists in your computational & ML group are **experimenting with new ML models** that might outperform your previous models. How can you bake in some sanity checks before committing to "real" predictions on your dataset of materials and material properties, which you plan to send to your experimental-science collaborators?
3. You've worked out a matured ML workflow, where you build new models regularly and leverage predictions on large materials datasets. Now your research team has grown to include more grad students, postdocs, and research scientists. **How can your systems scale alongside your team**?
4. 
