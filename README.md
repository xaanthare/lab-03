# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Isabel Fernandez
- Aline Garcia-Sanchez

## Lab Question Answers

Question 1: Why are RESTful APIs scalable?

Because the client and server are kept separate, the RESTful APIs can be scaled with ease without affecting functionality. Furthermore, they optimize interactions by integrating a cache and having each request be independent (no need to remember previous client requests). 

Question 2: According to the definition of “resources” provided in the AWS article above,
What are the resources the mail server is providing to clients?

Recipient
Sender
Subject
Body
mail_id

Basically the mail components… in this case they are kept in a list of dictionaries called ‘“mail”, so that could very well be considered the resource since everything else is kept inside that.

Question 3: What is one common REST Method not used in our mail server? How could
we extend our mail server to use this method?

	We do not use HTTP headers. We could use them to format the way the server returns the data, such as making the name of the recipient and sender bigger or making the subject in bold.

Question 4: Why are API keys used for many RESTful APIs? What purpose do they
serve? Make sure to cite any online resources you use to answer this question!

	API keys are a form of authentication for RESTful APIs. They assign an ID to your key and thus know who you are and allows you to access resources (although it is not the most safe since people can send their keys around). 
//used the aws article 

