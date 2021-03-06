### Spanish-Level-Checker
A project to create a machine learning model to help users predict the CEFR* level of a Spanish text.

The idea arose after reading many mind-numbing stories about cats/Jose's trip to the shops and wanting to learn Spanish through reading about topics I was actually interested in. However, it can be difficult to know if these more interesting articles are too difficult for you until you've spent a frustrating amount of time struggling to read them.

Throughout this project I scraped articles/stories/songs and their CEFR* levels using Selenium, Engineered features that were related to level (such as average sentence length or presence of certain verb tenses), used statistical analysis to determine which feature's were most significant, and finally trained a model to predict the level of unseen Spanish texts. This model used a K nearest neighbours algorithm and could predict a Spanish text's level exactly with 53% accuracy or with an error of 1 level with 87% accuracy. The A1 level was excluded as it would significantly decrease the accuracy of the model and it didn't seem likely that a user would expect to find A1 texts that weren't specifically designed to be A1 level.

The feature engineering and data analysis was done in the jupyter notebooks: spanish_texts_exploration.ipynb and analysis_and_model.ipynb.

*CEFR = Common European Framework of Reference for Languages
