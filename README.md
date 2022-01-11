# Ethics and data privacy
### Russell J. Funk
### University of Minnesota

Repository for Jupyter notebooks to illustrate data privacy concepts

## Getting started

The notebooks are located in the `sessions` folder.

To run them interactively, you'll need to install some Python packages, which are listed below. 

```
pip install pandas
pip install gensim
pip install numpy
pip install spacy
pip install textacy
pip install umap-learn[plot]
pip install matplotlib
pip install tqdm
pip install bokeh

python -m spacy download en_core_web_lg

python -m gensim.downloader --download glove-wiki-gigaword-50
python -m gensim.downloader --download glove-wiki-gigaword-100
python -m gensim.downloader --download glove-wiki-gigaword-200
python -m gensim.downloader --download glove-wiki-gigaword-300
python -m gensim.downloader --download glove-twitter-25
python -m gensim.downloader --download glove-twitter-50
python -m gensim.downloader --download glove-twitter-100
python -m gensim.downloader --download glove-twitter-200
```

Feel free to email me if you have any questions ([rfunk@umn.edu](mailto:rfunk@umn.edu)).