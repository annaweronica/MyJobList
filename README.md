

---

[THE JOB LIST](https://my-job-list.herokuapp.com/)

---

# UX

---

**Target audience:**<br>
The job seeker who is interested in job advertisements.
The employee seeker who wants to post a job advertisement.

**Aim:**<br>
To enable post and browse job offers for job and/or employees seekers.


**The structure:**<br>

- MAIN PAGE:
    - Navigation pantel at the top of the webpage allows the user to *Post a job* or navigate back to main page by clicking on the *IT JOBS STOCKHOLM*.<br>
    - Header section contains two parts. To the right there is an image for visual purpose. To the left the user can be dynamically re-dicerted to *Post a job* sub-page and read a static heading about a posibbility of browsing job offers underneath.<br>
    - Below there is a list with available job offers. Each line has a *job title*, *company name* and a button re-directing the user to a sub-page *JOB DETAILS* <br>

- POST A JOB
    - One page with form to fill in as follows:
        - Job title
        - Name of the company
        - Job description
        - List of requiremens
        - Description of the company
        - Website linking to the original job offers
    - A button *POST A JOB* which creats the job offers
    - The user will not be able to post a job offer unless he fills in the input.
    - All input required to be text ecept *Link to original job post* which must be an url
    - If the user changes his mind then he can be back to the main page by clicking on the logo in the navigation panel
    - Clicking *Post a job* button redirects the user to sub-page *JOB DETAILS* where he can see his job being created 


- JOB DETAILS
    - Silmpe, one page view with the clear heading at the top and then as follows underneath:
        - Job title
        - Name of the company
        - Job description
        - List of requiremens
        - Description of the company
    - Three buttons with actions:
        - *Apply* which redirects the user to new browser tab with thr original job post website
        - *Update* which redirects the user to sub-page allowing editing the post job
        - *Delete* which triggers confirmation model asking the user is he sure to delete the job post.

- UPDATE JOB
    - The sub-page allows the user to edit already existing job offer
    - The user can *Re-post the job* which re-directs him to the main page with the list of all job offers
    - The user can change his mind by clicking on *Cancel* button which redirects him back to the job offer he wanted to edit
    - The user can take no action by clicking on the logo in navgation menu at the top of the website
    
- Delete
    - The job offer can be deleted by clicking on the button *Delete* in the *View details* sub-page. Clicking on the *Delete* button will trigger confirmation model with the question is the user sure to delete a job post. The user have two options:
        - *Cancel* which take no action so the user is still in the *Job view* sub-page
        - *Delete* which re-directs him to the mian page
    

**Wireframes**

![1. Main view - Desktop, iPad](../wireframes/main-page.png)<br>
![2. Create - Desktop, iPad](../wireframes/create.png)<br>
![3. Read - Desktop, iPad](../wireframes/edit.png)<br>
![4. Update - Desktop, iPad](../wireframes/read.png)<br>
![5. Delete - Desktop, iPad](../wireframes/delete.png)<br>
![all iPhone view](../wireframes/iPhone-view.png)<br>

**USER STORIES:**

- As a potential employee I want to be able to read job offers at home website.
- As a potential employee I want to be able to click on view details to see job description.
- As a potential employee I want to apply for a job add.
- As a employer I want to create and post a job ads so potential employees can see it.
- As a employer I want to update already posted job ad.
- As a employer I want to delete posted job ad.

 - 
 - https://bootstrapious.com/p/bootstrap-navbar-with-logo
 - https://bootstrapious.com/p/bootstrap-sticky-footer
 - https://www.w3schools.com/howto/howto_css_delete_modal.asp


--------

Enjoy!
