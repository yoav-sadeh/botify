# Botify
Botify's purpose is to enable web scrapers creation easily by 
minimizing the time investment in DOM recording and replay.

##Main User Story:
User launches session and browses through needed 
web destinies.  
When the user finishes, he terminates the session.  
The user can then start a ___Scraper Builder___, based on any 
existing session and create a ready to use scraper, packed as a pip module or python project.  

###Scraper Builder: 
The ___Scraper Builder___ is a designer view in which the user creates ___Scraping Phases___ and ___Code Blocks___.  
It provides a replay feature that helps the user make sure the scraping flow and result are 
satisfactory.  
The ___Scraper Builder___ also allows the exclusion of redundant ___Scraping Phases___. 
 
###Scraping Phases:
___Scraping Phases___ are simply groups of ___Session Events___.  
The purpose of this capability is to better scope phases in 
a more readable manner

###Code Blocks:
___Code Blocks___ are the way ___Botify___ provides code interaction with ___Scraping Phases___ and DOM
elements' attributes as well as any other custom coded logic.

###Session Events:
___Session Events___ are the recorded representation of DOM events.  
Each ___Session Event___ includes the ___DOM Elements___ the event was relevant to.

###DOM Elements:
___DOM Elements___ are the representation of the browser DOM elements.  
Their attributes(text, url, size) are more accessible that they are via javascript or selenium. 