Question 1:
    You've been assigned to tackle designing a SASS (sofware as a service) that provides digital media backup services. The goal of this project is to provide customers with a tool that will automatically backup the photos and documents created on company media shoots.

    In a few paragraphs talk about how you would approach this design problem and lay out a hypothetical plan to solve key technology issues. Feel free to make liberal assumptions. Be sure to include some detail about the technology stack you would reccommend, the assumptions you make, as well as some of the key questions you'd ask when designing this solution.

Question 2:
    Imagine that the SASS tool you have designed has nearly a million users and the data services that power this tool you have created need to be upgraded to a new version. How would you plan to do this upgrade to those live services, ensuring both minimum down time and no data loss?

Question 3:
    Imagine that this backup solution you have designed has been working well and serving hundreds of thousands of customers for several months. One day, probably in the middle of the night as these things usually happen, you begin to get an increasing volume of customers reporting backup failures, and super slow backups. What are your first steps to triage the issues after being woken up? What tools might you use to verify the reports?

Question 4:
    Tell us about a software project you've worked on that you wish you could re-write/re-design knowing what you know now and what you learned from it?

Question 5:
    What do you think are the most cruicial traits to have in a successful software team and why?

Question 6: 
    Write a function that given an array of N positive integers it will print k largest elements from the array. The output function should print elements in descending order with a comma to seperate them if there is more than one. The number of elements in the array will always be larger than or equal to k. See Question6.py for the basic function laid out.

    Example:
        output(1, [5, 8, 9, 12]) should print: 12
        output(3, [12, 54, 3, 4, 6, 7]) should print: 54, 12, 7

Question 7:
    Your given an input json file in this folder. Imagine that you recieve one of these files every 2-10 minutes.

        Part A: Design and implement a batch model function that computes the running sum for the balance field. Each of the output items should correspond to an input item where the balance has been calculated to be a running total. Be sure to save your computed output back to a file (output_a.json)

        Part B: Imagine that instead of recieving the entire file, you recieve the individual objects one at a time and only have access to that one object at that time. Write a second implementation of the function you just wrote using a stream model design approach. Be sure to save your computed output back to a file (output_b.json)

    For example given this input:
        [
            ...
            {
                "_id": "5e8341284060d78ae49bce61",
                "index": 1,
                "guid": "0ab5a33b-667b-48e5-b447-39d14a52e64f",
                "isActive": true,
                "balance": "$3,530.08",
                ...
            },
            {
                "_id": "5e83412869df3c4e3e877031",
                "index": 2,
                "guid": "86b8d2af-f6a1-4262-a9fd-4cdeef904abc",
                "isActive": false,
                "balance": "$2,204.47",
                ...
            }
        ]

    Your output should be:
        [
            ...
            {
                "_id": "5e8341284060d78ae49bce61",
                "index": 1,
                "guid": "0ab5a33b-667b-48e5-b447-39d14a52e64f",
                "isActive": true,
                "balance": "$3,530.08",
                ...
            },
            {
                "_id": "5e83412869df3c4e3e877031",
                "index": 2,
                "guid": "86b8d2af-f6a1-4262-a9fd-4cdeef904abc",
                "isActive": false,
                "balance": "$5,734.55",
                ...
            }
        ]
