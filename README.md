# Spanish-Level-Checker
## Welcome
For this project I set out to create a machine learning model to help users predict the difficulty of a Spanish text. 

The idea arose after reading many mind-numbing stories about cats/Jose's trip to the shops and wanting to learn Spanish through
reading about topics I was actually interested in. However, it can be difficult to know if these more interesting articles are too difficult for you
until you've spent a frustrating amount of time struggling to read them.

Throughout this project this I scraped articles/stories/songs and their CEFR* levels using Selenium, Engineered features that were related to level (such as 
average sentence length or presence of certain verb tenses), used statistical analysis to determine which feature's were most significant,
and finally trained a model to predict the level of an unseen Spanish texts. This model used the Random Forest algorithm and could predict a Spanish text's level 
exactly with 63% accuracy or with an error of 1 level with 94% accuracy.

The feature engineering and data analysis was done in the jupyter notebooks: spanish_texts_exploration.ipynb and analysis_and_model.ipynb.

*CEFR = Common European Framework of Reference for Languages
