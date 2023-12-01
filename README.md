# THE BODY-MASS INDEX CALCULATOR

![Am I responsive](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/bmic-aimresponsive.png?raw=true)

This application provides a simple and efficient tool to calculate Body Mass Index (BMI). By entering weight and height, the program calculates the BMI and classifies the user into one of the standard categories (for example, underweight, normal weight, overweight, obese). After obtaining the result, the user has the option to save this information to track it over time, making it easier to monitor changes in BMI and promote a healthy lifestyle.

Visit the live site: [The Body-Mass Index Calculator](https://body-mass-index-calculator-1e646be6468f.herokuapp.com/)

# UX

## Site Goal

- This program was created with the idea of ​​being able to show the user's progress over time after joined and started at the Gym-Fitness (Project 1). 
The objective is to motivate people doing excersice showing their progress.

## Project Goals:

- Create a friendly and easy going interface that allows users to enter their weight and height without complications.

- Provide a clear classification of BMI and offer information about what each category means.

- Provide information about which BMI category the user belongs to.

- Allow users to save their BMI results to track changes and progress over time.

## Audience
- People interested in maintaining or improving their health and physical well-being.
- Dietitians, nutritionists and personal trainers who can use the tool to advise their clients.

## Design

### Flowchart

![Flowchart](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/Flowchart.jpeg)

## Features

## Current Features

### **Welcome Screen**

The user is welcomed to the program and ask to input their name.

![Welcome screen](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/welcome.jpg)

### **Main Menu**

The user has to input one of the three options. The options are "Calculate the body-mass index", "see your history" or "exit". 

![Select option](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/main-menu.jpg)

If the user input an invalid option, it will show a message saying "Please, insert a valid option". The valid options are 1, 2, or 3.

![Invalid option](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/invalid-mainmenu.jpg)

#### **Option 1**: *Calculate body-mass index*

When the user select the first option, the program will ask for their weight and their height.

![Weight and height](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/height.jpg)

If the user input an invalid value, a message will show saying "Please, insert a right value"

![Invalid value](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/invalid-calculator.jpg)

After inserting the two values, the program will calculate the body-mass index "(weight/(height/100)" and show a message saying the index and the category which the user is in.

At the same time, it will show a message asking if the user wants to save this record on a spread sheet table linked with the program. It will save the actual date and the body-mass index.

![Calculator](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/result.jpg)

![spread-sheet](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/spread-sheet.jpg)

If the user input a wrong value, a message will show up saying "Invalid option. Please write the letter 'Y' to save the record or 'N' to go back to the main menu"

![Invalid record](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/invalid-record.jpg)

#### **Option 2**: *See history*

This option will show a table with the records saved on the spread sheet

![History Table](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/table-history.jpg)

[Google Spreadsheet Table](https://docs.google.com/spreadsheets/d/1qZY_p_HG4QQAfTqoE2zHePFe6yACsM6PSTclSzWzjWs/edit#gid=0)

#### **Option 3**: *Exit*

This option will close the program.

### Features Left to Implement

In the future, I would like to:

- To add a spreadsheet in which the user enters the meals eaten during the day and automatically calculates and showing the total of calories and proteins ingested.

- To include educational information about the importance of BMI and tips for maintaining a healthy weight.

- To add colours and more ASCII art and formatting to the program.

## Testing
The code has been tested by using [CI Python Linter](https://pep8ci.herokuapp.com/)

The PEP8 Linter validator initially came back with quite a few errors, however these were mainly too many blank lines and whitespace. Once these were all fixed, the validator came back with just only line too long errors.

![CI Python Linter results]("https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/CI-Python-Linter.png?raw=true")

### Bugs
There are no bugs on this program. It's not possible to break the code. If the user tries to input a wrong value, the program will always ask to insert a right value.

### Fixed Bugs
Doing the Readme I realised that I don't need to use quotes for web links, but I need it for URL images.

### Errors
- 48: E501 line too long (96 > 79 characters)
- 50: E501 line too long (96 > 79 characters)
- 52: E501 line too long (94 > 79 characters)
- 54: E501 line too long (89 > 79 characters)
- 76: E501 line too long (126 > 79 characters)

## Technologies Used

### Languages Used

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

- [Gitpod](https://www.gitpod.io/) To create my workspace

- [GitHub](https://github.com/) - To save and store the files for the website.

- [Heroku](https://id.heroku.com/) - To deploy the App.

- [Code Institute template](https://github.com/Code-Institute-Org/p3-template) - To run the game in the terminal using Heroku.

- [CI Python Linter](https://pep8ci.herokuapp.com/) - Was used to test the code

### Data Storage

- [Google Drive API](https://developers.google.com/drive/api/guides/about-sdk)
- [Google Sheet API](https://developers.google.com/sheets/api/guides/concepts)

## Deployment & Local Development

### Deployment

This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account
2. On the main page click the button labeled New in the top right corner and from the drop-down menu select Create New App
3. You must enter a unique app name
4. Next select your region
5. Click on the Create App button
6. The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
7. Click Reveal Config Vars and enter port into the Key box and 8000 into the Value box and click the Add button
8. Click Reveal Config Vars again and enter CREDS into the Key box and the Google credentials into the Value box
9. Next, scroll down to the Build pack section click Add Build pack select Python and click Save Changes
10. Repeat step 8 to add node.js. o Note: The Build packs must be in the correct order. If not click and drag them to move into the correct order
11. Scroll to the top of the page and choose the Deploy tab
12. Select Github as the deployment method
13. Confirm you want to connect to GitHub
14. Search for the repository name and click the connect button
15. Scroll to the bottom of the deploy page and select the preferred deployment type
16. Click either Enable Automatic Deploys for automatic deployment when you push updates to GitHub

## Credits

- [Martina Terlevic](https://www.linkedin.com/in/martinaterlevic/) - Code Institue Mentor. She gave me ideas and advices for the project and how to improve and fix it.
- [Code Institute](https://codeinstitute.net/ie/) - The Love Sandwiches walkthrough was very helpful to learn how to import gspread and google.auth. It helped me to remind me how to deploy it on Heroku as well.