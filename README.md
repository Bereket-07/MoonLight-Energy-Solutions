# ☀️ MoonLight-Energy-Solutions ☔

## Table of Contents

- [Overview](#overview)
- [Technologies](#technologies)
- [Folder Organization](#folder-organization)
- [Setup](#setup)
- [Notes](#notes)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project is a Streamlit-based interactive dashboard designed for performing Exploratory Data Analysis (EDA) on different datasets. The tool allows users to select a dataset from a sidebar and choose various EDA options, including summary statistics, correlation analysis, time series analysis, and more

## Technologies


The set of technologies we utilized in this project:

1. **Programming Language**: [![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
2. **Data Visualization**: [![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat&logo=matplotlib&logoColor=white)](https://matplotlib.org/)
3. **Data Manipulation**: [![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat&logo=seaborn&logoColor=white)](https://seaborn.pydata.org/)
4. **Web Framework**: [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
5. **Data Analysis**: [![Pandas](https://img.shields.io/badge/Pandas-130654?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
6. **Data Hosting**: [![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=flat&logo=googledrive&logoColor=white)](https://www.google.com/drive/)

## Folder Organization

```
📁.github
└──
    └── 📁workflows
         └── 📃CI.yml
         └── 📃unittests.yml
└── 📁notebooks
         └── 📓__init__.ipynb
         └── 📃__iniit__.py
         └── 📰README.md
└── 📁scripts
         └── 📃__init__.py
         └── 📰README.md
└── 💻src
    └── 📁dashboard-div
                    └── 📝app.py
                    └── 📝README.md
└── ⌛tests
         └── __init__.py
└── 📜.gitignore
└── 📰README.md
└── 🔋requirements.txt
└── 📇templates.py

```

### Folder Structure: A Deep Dive

- **📁.github**: This folder contains GitHub-related configurations, including CI/CD workflows.

  - **📁workflows**: Contains the CI/CD pipeline definitions.
    - **📃CI.yml**: Configuration for Continuous Integration.
    - **📃unittests.yml**: Configuration for running unit tests.

- **📁notebooks**: This directory holds Jupyter notebooks and related Python files.

  - **📓**init**.ipynb**: Initialization notebook, potentially for setting up the environment or performing preliminary tasks.
  - **📃**init**.py**: Initialization Python file for the notebook module.
  - **📰README.md**: Documentation for the notebooks.

- **📁scripts**: Contains Python scripts used throughout the project.

  - **📃**init**.py**: Initialization file for the scripts module.
  - **📰README.md**: Documentation for the scripts.

- **💻src**: The main source code of the project, including the Streamlit dashboard and other related files.

  - **📁dashboard-div**: Holds the code for the dashboard.
    - **📝app.py**: Main application file for the dashboard.
    - **📝README.md**: Documentation specific to the dashboard component.

- **⌛tests**: Contains test files, including unit and integration tests.

  - ****init**.py**: Initialization file for the test module.

- **📜.gitignore**: Specifies files and directories to be ignored by Git.

- **📰README.md**: The main documentation for the entire project.

- **🔋requirements.txt**: Lists the Python dependencies required to run the project.

- **📇templates.py**: Contains templates used within the project, possibly for generating or processing data.

## Setup

1. Clone the repo

```bash
git clone https://github.com/Bereket-07/MoonLight-Energy-Solutions.git
```

2. Install all dependencies

```bash
pip install -r requirements.txt
```

3. change directory to run the streamlit app locally.

```bash
cd src\dashboard-div
```

4. Start the streamlit app

```bash
streamlit run app.py
```

## Contributing

We welcome contributions to this project! To get started, please follow these guidelines:

### How to Contribute

1. **Fork the repository**: Click the "Fork" button at the top right of this page to create your own copy of the repository.
2. **Clone your fork**: Clone the forked repository to your local machine.
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```
3. **Create a new branch**: Create a new branch for your feature or bugfix.
   ```bash
   git checkout -b feature/your-feature
   ```
4. **Make your changes**: Implement your feature or fix the bug. Ensure your code adheres to the project's coding standards and style.
5. **Commit your changes**: Commit your changes with a descriptive message.
   ```bash
   git add .
   git commit -m 'Add new feature or fix bug'
   ```
6. **Push your branch**: Push your branch to your forked repository.
   ```bash
   git push origin feature/your-feature
   ```
7. **Create a Pull Request**: Go to the repository on GitHub, switch to your branch, and click the `New Pull Request` button. Provide a detailed description of your changes and submit the pull request.

## Additional Information

- **Bug Reports**: If you find a bug, please open an issue in the repository with details about the problem.

- **Feature Requests**: If you have ideas for new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License

### Summary

The MIT License is a permissive free software license originating at the Massachusetts Institute of Technology (MIT). It is a simple and easy-to-understand license that places very few restrictions on reuse, making it a popular choice for open source projects.

By using this project, you agree to include the original copyright notice and permission notice in any copies or substantial portions of the software.
