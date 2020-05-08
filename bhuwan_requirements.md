
# Questions
---

## About the Company
---

### We need to know about the client. Allows us to know more about their operational context as well as the domain they operate in. 

#### What does your business do?  
Our company, Zomato, is a startup that connects foodies to restaurants. It provides a platform for people to search dishes, order online and get them delivered at their doorstep. We are operating over all major cities in India and abroad(USA, Canada, UK, UAE, etc)and are expanding very fast.
What product or service are you selling?


#### What is your mission and vision?  
Our mission is to serve delicious and healthy dishes while saving customers’ time and money. We want to achieve our mission and win our customers heart at the same time.  

#### What should we know about the domain the company operates in?  
Zomato is a restaurant aggregator and food delivery company. Our partners are restaurants who don’t want the hassle of owning and maintaining a delivery service and a website. Our customers are general public that enjoy food. Companies like Uber eats, Swiggy are our competitors.  



## Context on the Product

### We need to know where the product fits in in their overall scheme of things.

#### Why do you need this new system? What is the business need?  
We collect feedback from our customers. We want to convert the data we get from our customer into valuable insights that will help us and our partner restaurants find areas they need to improve in.  


#### Is there a system in place to do it right now (even if manual)? If so, how is it done right now? Is the process documented?  
No, there is no such system right now.  

#### Even if not, How would an expert in the space approach this problem? What would be the variables/pieces of data that person would base a solution on?   
An expert would manually go through each of the customer feedback and find out the areas that need improvement. For example if many people complain about being biryani from the restaurant “Oye Amritsar” spicy then the expert would suggest the chef to use less spices. Contrary to this, if an expert finds that people love spicy biryani then the expert would suggest the chef to continue doing so.  



#### What features do you like about your current system?  
We like how the existing system can handle workload. It is efficient, fault tolerant, has high availability.  

#### What features don't you like about the current system?  
It’s not the feature but lack of it that we do despise. We could know our customers, their taste, better if only we knew the sentiments behind each feedback.



### About the new system/product

#### What are the basic, crucial needs of the new software?  
The new software should parse all feedbacks, identify sentiment for each, identify entity(e.g momo, pizza, biryani, etc) associated with each of the feedback, and identify the word/phrase that describes the feedback(e.g spicy, amazing, oily and stale, etc).  
Additionally, the product should also add visualization to identify the sales of dishes, most profitable dishes, most loved dishes, Dishes with most complaints, etc.  

#### What benefit can the product provide for your customers?
It will allow our partners(restaurants) to know what consumers love/hate about their dishes, dishes that they need to stop selling, predict the sales of their dishes.  

#### What should be the top priority? 
The top priority should be to extract sentiment for each customer feedback, the entity(pizza, momo) associated with it and the phrase that describes the entity(hot, spicy, bad, stale and oily, etc.)  



#### What are the acceptance criteria, if any? Please be specific. Eg: 20% decrease in manual responses to tickets. Do you have systems in place to measure those metrics?  
The accuracy should be at least 80%. The product should save human expert’s time of manually going through feedbacks and analyzing them.  




### System Usage

#### Which of your staff will be using or involved in the product the most?  

Our partners, restaurant owners/managers, will be involved in using the product the most. They will use it to monitor their sales, customer behaviour, customer feedback, identify areas they need to improve in and areas that they are already good at.  


#### Will the system need to integrate with any other type of software?  

No, the system doesn’t need to integrate with any type of software. We want you to build the api for us so that we can send a json request from our end and get a response from the api. 


### About the Data


#### What data do you have that might be related, in any way, to the problem being solved?  
After the delivery of food we ask the user to provide feedback about the delivery service. Then a few hours later we ask customers to provide feedback on the food, its taste, quality, etc. For both delivery service and food we store textual feedback and ratings provided by customers.  


#### How is the data stored, manipulated right now? What’s your data infrastructure?  
Currently we store all our data in aws database server. We would like to keep it that way. Our applications are also deployed using aws cloud. We also want this api to be deployed in aws.  


#### Do you have internal data-dedicated teams?  
Yes, we have a data-dedicated team. Its primary focus is to store the data in database, make sure data is available and backed up regularly. However, we don’t have a team to generate insights from the data.  

### Caveats  

#### What are the constraints on the system being built (resourcing, timing, etc)?  
Each feedback should be processed and the results should be stored in a separate table. Each feedback should not take more than 3 second to process. The system should utilize aws services like api gateway for making the api endpoint, lambda function to call the deep learning model and sagemaker to host the deep learning model. The application should also have a feedback loop so that it trains with new feedback coming each day.  


#### What is the strategy for your organisation? [One year, five years]. Are there considerations that need to be taken into account?  
In the next five years, we plan to increase our customer base by 5 times, so the api should be able to handle a workload that is significantly higher that what we have right now. Also we want the api to be edge optimized--response time should not depend on the location from where the api is being called. For this you deploy the api on multiple regions in the aws.  

### General  

#### Do you have a timeline in mind?  

We are expecting a proof of concept within a month. It is not necessary to construct a custom model, you can use the existing services (sentiment classification, entity extraction, etc) provided by aws. From the second month we would like the product to be ready for beta testing. We want to ship the product to the user within 3 months. In 5 months the product should me mature enough to have an accuracy of 80%.  



# Requirements Analysis  
---

## General Study  
The client is a popular restaurant aggregator and delivery service. Their mission is to bring quality and healthy food right at the customers’ doorstep. While doing so they also want to help their partner restaurant to identify their customers’ taste better and tailor their dishes to make them happy.  

The company has been collecting feedback from the customers regarding their food and delivery service, and has a huge database currently stored in the aws. They now want to analyze the feedback to get information regarding the food served, what the customers like and dislike?  

## Requirements
---

The company wants to process the feedback given by their customers and identify the key areas that need improvement. They want to know what their customers like and dislike about the food served.   
The major requirements are:  
* The company wants to gather meaningful information from the feedback automatically.  
* The api is an internal tool that the company wants to use for itself.  
* The api should be able to classify the feedbacks at large scale so that it can handle big data and multiple requests.  

### Functional Requirements  

* They want the product as an api they can send a request to and get a response back.  
* They want to utilize the existing services as much as they can.  
* The system should have an accuracy of 80%.  
* They also want a dashboard so that owners/managers from their partner restaurants can login and get information like the areas they need to improve in, what customers like/dislike about their dishes, their most popular dishes and rarely ordered dishes.  
* The system should process each feedback within 3 second.  

## Timeline  

The company needs the prototype ready in a month. They want to beta-test the product from the second month and ship it to the user within 3 months. However in 5 months the product should be able to get an accuracy of 80% measured against a human.


