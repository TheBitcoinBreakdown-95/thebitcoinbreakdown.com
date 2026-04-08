- Right click - inspect
   

**Hit the button top left**
 
- ![Exported image](Exported%20image%2020251228191519-0.png)
    
- Then scroll over the section you want to edit, aka the footer
 ![Exported image](Exported%20image%2020251228191520-1.png)            
- You'll notice on the right highlights the code, then go to the box below
 ![Exported image](Exported%20image%2020251228191521-2.png)

- type display : none
 ![Exported image](Exported%20image%2020251228191536-3.png)  

- Highlight that whole section and copy:  
.entry-footer {  
margin-top: 10px;  
display: none;  
}
   

Then X out and go back to the dashboard, go down to appearance and customize
 
Click additional CSS at the bottom
   
![Exported image](Exported%20image%2020251228191537-4.png)   
OK to be honest this was just me fucking around but I figured it out, the code below is a combination of removing both footers I didn't want, while also adding in display: none afterwards
   

**Paste in this code:**
 
/* remove metadata */  
element.style {  
}  
.entry-footer {  
margin-top: 10px;  
display: none;  
}  
/* remove metadata */  
element.style {  
}  
.site-main .comment-navigation, .site-main .posts-navigation, .site-main .post-navigation {  
margin: 0 0 1.5em;  
overflow: hidden;  
display: none;  
}
   

And then magic it disappears!
 
Because you already did this once, you might only have to wait, or go back to dashboard, appearance, customize, and go into each article and hit enter after the code and then refresh.
   

BASICALLY
 
All I did was use this video:  
[https://www.youtube.com/watch?v=MNXOF0xBy1Q](https://www.youtube.com/watch?v=MNXOF0xBy1Q)
 
But paste my own code, the code that specifically applied to those two bottom footer sections and played around until it worked