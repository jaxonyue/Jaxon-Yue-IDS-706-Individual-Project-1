# IDS 706 Mini Project 2 [![CI](https://github.com/nogibjj/Jaxon-Yue-IDS-706-Mini-Project-2/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Jaxon-Yue-IDS-706-Mini-Project-2/actions/workflows/cicd.yml)
This repository includes the components for Mini-Project 2 - Pandas Descriptive Statistics Script. It uses my Python template and contains a series of EDA on a dataset related to the development of average annual wages across various countries in the world. The EDA process includes getting essential statistics such as mean and median, as well as a quick data visualization on the growth of the average annual wages. This repo also contains respective tests to check whether the statistics calculated in the EDA process match with the real data points.

### Key elements in the repository are:
* Development of average annual wages.csv
* Makefile
* requirements.txt
* Dockerfile
* devcontainer
* main.py
* test_main.py
* GitHub Actions

### Steps needed to run:
1. Create a virtualenv: 'virtualenv ~/.venv'
2. Edit my '~.bashrc'
3. Run 'make all'

### Results
Using Github Actions, I have passed make format, make lint, and make test as shown below.
<img width="900" alt="Screenshot 2023-09-09 at 11 45 49 AM" src="https://github.com/nogibjj/Jaxon-Yue-IDS-706-Mini-Project-2/assets/70416390/9b64a511-794e-40da-a33d-245ea11cb3ec">
