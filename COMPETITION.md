# COMPETITION

## Rules

- You must be an attendee of the MRS Spring 2022 DS04 Tutorial
- You must be a current student (e.g., undergraduate or graduate level)
- You must submit your entry before the end of the tutorial on 8 May 2022

## THE COMPETITION

Looking back at sections 1 and 2, think about the key takeaways on prediction-tracking and model tests.  **Submit a Github pull request** that implements the following:

1. Improve the `predict_single()` function in `01_tracking_predictions/model.py`, such that it returns a more richly-structured output, decorated with appropriate metadata. (See the `structured_prediction_*.json` files for examples.)
2. Add another "physicality" test in `02_testing_models/physicality_tests.py`. Some examples could include: verifying invariance to order of elements, verifying that predicting the same material many times returns the same result (within reasonable numerical precision). **NB: These tests don't necessarily have to pass when run.**

## PRIZES AND SCORING

Submissions will be evaluated wholistically, based on code correctness, readability, documentation, and maintainability. Prizes are TBD.