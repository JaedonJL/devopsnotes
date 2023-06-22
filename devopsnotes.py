GitHub Commands

1. Installation and Setup of Git Command Line:
    Download Git from the official website (https://git-scm.com/downloads) and install it on your system.
    Open a terminal or command prompt to verify the installation:
.................................................
     git --version
.................................................

2. Creation of a new local Git Repository:
Navigate to the desired directory where you want to create the repository.
Initialize a new Git repository:
.................................................
     git init
.................................................

3. Commit Files to Git locally:
   Add the files you want to include in the commit:
.................................................
     git add <file1> <file2> ...
.................................................
   Commit the changes with a descriptive message:
.................................................
     git commit -m "Commit message"
.................................................

4. Branches in Git:
   - List all branches:
.................................................
     git branch
.................................................
   - Create a new branch:
.................................................
     git branch <branch_name>
.................................................
   - Switch to a different branch:
.................................................
     git checkout <branch_name>
.................................................
   - Merge branches (while on the destination branch):
.................................................
     git merge <source_branch>
.................................................

5. Create Tags in Git:
   - Create a lightweight tag:
.................................................
     git tag <tag_name>
.................................................
   - Create an annotated tag with a message:
.................................................
     git tag -a <tag_name> -m "Tag message"
.................................................

6. GitHub account:
   - Go to GitHub (https://github.com) and sign up for a new account.

7. Create a new GitHub repository:
   - Log in to your GitHub account.
   - Click on the "+" sign in the top-right corner and select "New repository".
   - Provide a repository name, optional description, and choose other settings as needed.
   - Click "Create repository" to create the new repository.

8. Push Git Local Repository to Remote GitHub repository:
   - Add the remote GitHub repository URL as the origin:
.................................................
     git remote add origin <repository_url>
.................................................
   - Push the local repository to the remote repository:
.................................................
     git push -u origin <branch_name>
.................................................

9. Create a GitHub Readme file:
   - Create a new file named "README.md" in the root directory of your local Git repository.
   - Add content to the README file using Markdown syntax.
   - Save the file and commit it to your Git repository.

10. Create a Git tag and GitHub Release:
    - Create a tag locally:
 .................................................
      git tag -a <tag_name> -m "Tag message"
 .................................................
    - Push the tag to the remote GitHub repository:
 .................................................
      git push origin <tag_name>
 .................................................
    - Go to the GitHub repository page and click on "Releases".
    - Click "Create a new release" and provide the tag name, release title, and description.
    - Publish the release.

11. Creating Git submodules:
    - Navigate to the root directory of the existing Git repository where you want to add a submodule.
    - Add the Git submodule using its repository URL:
 .................................................
      git submodule add <submodule_repository_url>
 .................................................
    - Commit and push the changes to the remote repository.

Troubleshooting

When working with GitHub, having troubleshooting skills can help you overcome common issues and ensure a smooth workflow. Here are some troubleshooting skills and commands you may find useful:

1. Checking Git Configuration:
   - To view your Git configuration settings:
.................................................
     git config --list
.................................................
   - Verify your name and email settings:
.................................................
     git config user.name
     git config user.email
.................................................

2. Checking Git Status:
   - To see the current state of your local repository and any modifications:
.................................................
     git status
.................................................

3. Handling Merge Conflicts: (x)
   - When encountering a merge conflict, open the conflicting file(s) and resolve the conflicts manually.
   - After resolving conflicts, add the modified files and commit the changes.

4. Undoing Changes:
   - To discard changes in a file and revert it back to the last commit:
.................................................
     git checkout -- <file>
.................................................
   - To revert a specific commit (creating a new commit that undoes the changes):
.................................................
     git revert <commit_hash>
.................................................

5. Syncing with Remote Repository:
   - If your local branch is behind the remote branch, fetch and merge the changes:
.................................................
     git fetch
     git merge origin/<branch_name>
.................................................
   - If your local branch is ahead of the remote branch, push your changes:
.................................................
     git push origin <branch_name>
.................................................

6. Resolving Authentication Issues:
   - If you encounter authentication problems, verify your remote URL and credentials.
   - Update the remote URL if needed:
.................................................
     git remote set-url origin <repository_url>
.................................................

7. Checking Remote Repository Information:
   - To view remote repositories:
.................................................
     git remote -v
.................................................
   - Check the upstream repository for a branch:
.................................................
     git branch -vv
.................................................

8. Cleaning Up: ****
   - Remove untracked files and directories:
.................................................
     git clean -df
.................................................
   - Discard all local changes and revert to the last commit:
.................................................
     git reset --hard HEAD
.................................................

9. Reviewing Git Logs:
   - To view commit history:
.................................................
     git log
.................................................
   - Display a compact summary of recent commits:
.................................................
     git log --oneline
.................................................

10. Git Help:
    - Access the Git documentation and command reference:
 .................................................
      git help
      git <command> --help
 .................................................








































Lab Dictionary Example

# Define a dictionary to store employee information
employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]

def get_employees_by_age_range(age_lower_limit, age_upper_limit):
    result = []
    # check for age limits and append the item to result
    for item in employee_data:
        if int(item["age"]) > int(age_lower_limit) and int(item["age"]) < int(age_upper_limit):
            result.append(item)
    return result

def calculate_average_salary():
    total = 0
    average = 0
    salary=[]
    for item in employee_data:
        total = 0
        person =0
        if item["salary"]:
          value = item["salary"]
          total = total + value
          person = person + 1
    average = total / person
    return average

def get_employees_by_dept(department):
    result = []
    for item in employee_data:
      if item["department"]==department:
        result.append(item)
    return result

def display_all_records():
    print(("Name" + "\t" +"Age" +"\t" +"Department" +"\t" +"Salary" ).expandtabs(15))
    for item in employee_data:
        print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(item["salary"])).expandtabs(15))


def display_records(employee_info):
    print(("Name" + "\t" +"Age" +"\t" +"Department" +"\t" +"Salary" ).expandtabs(15))
    for item in employee_info:
        print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(item["salary"])).expandtabs(15))

def display_main_menu():

    print("\n----- Employee information Tracker -----")

    print("Select option\n")

    print("1 - Display all records")
    print("2 - Display average salary")
    print("3 - Display employee within age range")
    print("4 - Display employee in a department")


    print("Q - Quit")

    option = input("Enter selection =>")

    if option == '1':
        display_all_records()

    elif option == '2':
        average_salary = calculate_average_salary()
        print("Average salary = " + str(average_salary))

    elif option == '3':
        age_lower_limit = input("age (Lower Limit) = ")
        age_upper_limit = input("age (Uper Limit) = ")
        employee_info = get_employees_by_age_range(age_lower_limit, age_upper_limit)
        display_records(employee_info)


    elif option == '4':
        department = input("Name of Department = ")
        employee_info = get_employees_by_dept(department)
        display_records(employee_info)

    elif option == 'Q':
        quit()

def main():

    while (True):
        display_main_menu()


if __name__ == "__main__":
    main()


Pytest

import pytest
from employee_info import get_employees_by_age_range
def test_get_employees_by_age_range():
    expected_results = [
       {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
       {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
       {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    given_result = get_employees_by_age_range(30,35)
    if given_result==expected_results:
        assert(True)


from employee_info import calculate_average_salary
def test_calculate_average_salary():
    expected_results = 60000
    given_result = calculate_average_salary()
    if given_result == expected_results:
        assert(True)

from employee_info import get_employees_by_dept
def test_get_employees_by_dept():
    expected_results= [
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
    ]
    given_result= get_employees_by_dept("Marketing")
    if given_result==expected_results:
        assert(True)






























Python Dictionary Navigation Tools

Certainly! Here are some commonly used tools and techniques to navigate dictionaries and arrays in Python, along with examples:

1. Accessing Dictionary Values:
   - Use square brackets (`[]`) with the key to access the corresponding value.
   Example:
   --------------------------------------------------python
   my_dict = {"name": "John", "age": 30, "city": "New York"}
   print(my_dict["name"])  # Output: John
   --------------------------------------------------

2. Accessing Array (List) Elements:
   - Use square brackets (`[]`) with the index to access a specific element in the list. The index starts from 0 for the first element.
   Example:
   --------------------------------------------------python
   my_list = ["apple", "banana", "cherry"]
   print(my_list[1])  # Output: banana
   --------------------------------------------------

3. Iterating Over Dictionary Items:
   - Use a `for` loop with the `.items()` method to iterate over key-value pairs in a dictionary.
   Example:
   --------------------------------------------------python
   my_dict = {"name": "John", "age": 30, "city": "New York"}
   for key, value in my_dict.items():
       print(key, value)
   --------------------------------------------------
   Output:
   --------------------------------------------------
   name John
   age 30
   city New York
   --------------------------------------------------

4. Iterating Over Array (List) Elements:
   - Use a `for` loop to iterate over elements in an array.
   Example:
   --------------------------------------------------python
   my_list = ["apple", "banana", "cherry"]
   for item in my_list:
       print(item)
   --------------------------------------------------
   Output:
   --------------------------------------------------
   apple
   banana
   cherry
   --------------------------------------------------

5. Checking Key Existence in a Dictionary:
   - Use the `in` keyword to check if a key exists in a dictionary.
   Example:
   --------------------------------------------------python
   my_dict = {"name": "John", "age": 30, "city": "New York"}
   if "age" in my_dict:
       print("Age exists in the dictionary.")
   --------------------------------------------------

6. Checking Element Existence in an Array:
   - Use the `in` keyword to check if an element exists in an array.
   Example:
   --------------------------------------------------python
   my_list = ["apple", "banana", "cherry"]
   if "banana" in my_list:
       print("Banana exists in the list.")
   --------------------------------------------------












price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }


quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}




def total_cost_shopping():
total_cost = 0
for key in price_list.keys():
if key in quantity_list:
# complete the implementation below:


print("total cost = ", total_cost)




def cost_of_fruits(fruit, quantity):
for key in price_list.keys():
if key == fruit:
cost = quantity*price_list[key]
break


print("cost of ", quantity, fruit, "=", cost)




def main():


cost_of_fruits('apple', 10)
total_cost_shopping()




if __name__ == "__main__":
main()

