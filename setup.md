## Creating a Python Project with Git and Virtual Environment in IntelliJ IDEA (Community Edition)
Follow these step-by-step instructions to create a Python project with Git and a virtual environment using the free version of IntelliJ IDEA:

**Step 1: Install IntelliJ IDEA Community Edition**

Download and install the free version of IntelliJ IDEA from the official website: [IntelliJ IDEA Community Edition](https://www.jetbrains.com/idea/)

**Step 2: Configure Git**

- Install Git on your system if you haven't already. You can download it from the official Git website: [Git Downloads](https://git-scm.com/downloads)
- Open IntelliJ IDEA and go to `File -> Settings` (or `IntelliJ IDEA -> Preferences` on macOS).
- In the Settings/Preferences dialog, navigate to `Version Control -> Git`.
- Click on the "Test" button to ensure IntelliJ IDEA can detect the Git executable.
- Close the Settings/Preferences dialog.

**Step 3: Create a New Python Project**

- Open IntelliJ IDEA and click on "Create New Project" or go to `File -> New -> Project`.
- In the New Project dialog, select "Pure Python" and click "Next".
- Choose a location for your project and give it a name. Click "Finish" to create the project.

**Step 4: Set up a Virtual Environment**

- Open the terminal in IntelliJ IDEA by going to `View -> Tool Windows -> Terminal`.
- Navigate to the root folder of your project using the `cd` command.
- Run the following command to create a virtual environment:
  ```
  python3 -m venv venv
  ```
- Activate the virtual environment:
    - For macOS/Linux:
      ```
      source venv/bin/activate
      ```
    - For Windows:
      ```
      venv\Scripts\activate
      ```

**Step 5: Initialize Git Repository**

- In the terminal, make sure you are still in the root folder of your project.
- Run the following command to initialize a Git repository:
  ```
  git init
  ```

**Step 6: Create a .gitignore File**

- Create a file named `.gitignore` in the root folder of your project.
- Add any files or directories you want to ignore in the Git repository. For example:
  ```
  venv/
  __pycache__/
  *.pyc
  *.log
  ```

**Step 7: Commit and Push Changes**

- In the terminal, run the following commands to stage all files for commit, commit the changes, and push them to a remote repository (if desired):
  ```
  git add .
  git commit -m "Initial commit"
  git remote add origin <remote repository URL>
  git push -u origin master
  ```

**Step 8: Install Pytest and Create a Demo Program**

- Make sure your virtual environment is activated.
- In the terminal, run the following command to install pytest:
  ```
  pip install pytest
  ```
- Create a demo Python file named `demo.py` in your project folder and add the following code to it:
  ```python
  def add_numbers(a, b):
      return a + b
  ```


```python
def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(10, -5) == 5
  ```

**Step 10: Run the Unit Test**

- Make sure your virtual environment is activated.
- In the terminal, run the following command to execute the pytest command:
  ```
  pytest
  ```
- This will discover and run any tests in files that match the `test_*.py` pattern.
- You should see the test results in the terminal output.

That's it! You've created a Python project with Git and a virtual environment in IntelliJ IDEA, and also executed a simple unit test using pytest. You can continue adding more tests and writing your project code within this setup.

For further reference, you can explore the following resources:

- [IntelliJ IDEA Community Edition](https://www.jetbrains.com/idea/)
- [Git Documentation](https://git-scm.com/doc)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [Pytest Documentation](https://docs.pytest.org/en/latest/)

Feel free to consult these resources for more detailed information on the tools and concepts involved.