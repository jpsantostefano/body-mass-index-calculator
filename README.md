# THE BODY-MASS INDEX CALCULATOR

![Am I responsive](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/bmic-aimresponsive.png?raw=true)

This application provides a simple and efficient tool to calculate Body Mass Index (BMI). By entering weight and height, the program calculates the BMI and classifies the user into one of the standard categories (for example, underweight, normal weight, overweight, obese). After obtaining the result, the user has the option to save this information to track it over time, making it easier to monitor changes in BMI and promote a healthy lifestyle.

Visit the live site: [The Body-mass index](https://body-mass-index-calculator-1e646be6468f.herokuapp.com/)

## User Experience (UX)

#### Key information for the site

This program was created with the idea of ​​being able to show the user's progress over time after joined and started at the Gym-Fitness (Project 1).

Project goals:

- To motivate people doing excersice showing their progress.

## Design

### Flowchart

![Flowchart](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/Flowchart.jpeg)

### Features

#### Existing Features

**Welcome screen**

- The user is welcomed to the program and ask to input their name.

![Welcome screen](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/welcome.jpg)

**Main Menu**

- The user has to select one of the three options. The options are "Calculate the body-mass index", "see your history" or "exit". 

![Select option](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/main-menu.jpg)

- If the user input an invalid option, it will show a message saying "Please, insert a valid option"

![Invalid option](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/invalid-mainmenu.jpg)

**Calculate body-mass index**

- When the user select the first option, the program will ask for their weight and their height.

![Weight and height](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/height.jpg)

- If the user input an invalid value, a message will show saying "Please, insert a right value"

![Invalid value](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/invalid-calculator.jpg)

- After inserting the two values, the program will calculate the body-mass index and show a message saying the index and the category which the user is in.
- At the same time, it will show a message if the user wants to save this record on a spread sheet table linked with the program. It will save the actual date and the body-mass index.

![Calculator](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/result.jpg)

![spread-sheet](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/spread-sheet.jpg)

-If the user input a wrong value, a message will show up saying "Invalid option. Please write the letter 'Y' to save the record or 'N' to go back to the main menu"

![Invalid record](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/invalid-record.jpg)

**See history**

- This option will show a table with the records saved on the spread sheet

![History Table](https://github.com/jpsantostefano/body-mass-index-calculator/blob/main/docs/features/table-history.jpg)

**Exit**

- This option will close the program.

---

### Features Left to Implement

In the future, I would like to:

- Add a calories and protein counter consumed per day.

- Add colours to the program.

- Add more ASCII art and formatting to the program.

---

## Technologies Used

### Languages Used

The language used is Python

### Frameworks, Libraries & Programs Used

[Git](https://git-scm.com/) - For version control.

[GitHub](https://github.com/) - To save and store the files for the website.

[Heroku](https://id.heroku.com/) - To deploy the App.

[Code Institute template](https://github.com/Code-Institute-Org/p3-template) - To run the game in the terminal using Heroku.

## Deployment & Local Development

### Deployment

- This site was deployed by completing the following steps:

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


