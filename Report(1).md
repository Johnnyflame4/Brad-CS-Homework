# Homework 05 Report

1. What does the `in` operator do? Provide examples of the `in` using strings and lists (or tuples). 
   It checks to see if the previous string or value is contained within the following value or string. 
    For example, 

guest_list = [jonathan, rick, ashley]

def add_to_guest_list(namr:str)
    append(guest_list)
    print(name " has been added to the guest list")

def check_guest_list(name:str)
    if name in guest_list:
        print(name " is on the list")
    else:
        print(name " is not on the list")

add_to_guest_list(Brad)
check_guest_list(Brad)

2. Taking a moment to research, why would one want to use .casefold() instead of .lower() in python when comparing strings? Please include the reference on where you find the information.
   casefold if a more extreme version of .lower. If a character is not recognized as typically from the english language, it will not be converted by .lower. It can be especially usefull for converting characters of words in other languages. 

   Source: Gitlab Copilot

3. For each of the three sequential types you have learned (list, string, tuple) - label as mutable or immutable (refer to the team activity).
   * string - immutable
   * list - mutable
   * tuple - immutable

4. Explain mutability and immutability in your own words.
    Mutable can be changed, similar to mutate. Immutable meams it can not be changed.
    
5. Given the following code:

    ```python
    def mystery_function(x):
        x = 100

    x = 1
    print(x)
    mystery_function(x)
    print(x)
    ```

* What is the output of the code above?
  1
  1

* Explain why the output is what it is.
Because the assignment of x as 100 in the mystery_function can't take place after x is assgined as 1 as a global variable outside of a function

6. Given the following code:

    ```python
    def mystery_function(x):
        x[0] = 100

    x = [1, 2, 3]
    print(x)
    mystery_function(x)
    print(x)
    ```
* What is the output of the code above? 
    [1, 2, 3]
    [100, 2, 3]

* Explain why the output is what it is.
Here x is a list and not a variable. The list has values of 1, 2, 3. When the program prints x, it prints as the list defined outside of the function. When the mystery_function is called with the value x, it executes by assigning index 0 in the list named x with 100. So, 1 is replaced with 100. The list of x is now 100, 2, 3 which is printed out in the next line. 

7. Would happen if `x` was a tuple? What is generated when you try to run the code above with a tuple?

    ```
    # put the error message here

(1, 2, 3)
Traceback (most recent call last):
  File "c:\Users\Brad\Documents\VS Code Projects\Python Projects\Homework 05\Hacker Rank Capitalize.py", line 19, in <module>
    mystery_function(x)
    ~~~~~~~~~~~~~~~~^^^
  File "c:\Users\Brad\Documents\VS Code Projects\Python Projects\Homework 05\Hacker Rank Capitalize.py", line 15, in mystery_function
    x[0] = 100
    ~^^^
TypeError: 'tuple' object does not support item assignment

    ```


8. Given the following code:

    ```python
    def mystery_function(x):
        x[1][0] = 100

    x = (3, [1, 2, 3], [4, 5, 6])
    print(x)
    mystery_function(x)
    print(x)
    ```

* What is the output of the code above?
* 
(3, [1, 2, 3], [4, 5, 6])
(3, [100, 2, 3], [4, 5, 6])

## Deeper Thinking

We talked a lot about immutable and mutable. Why would this matter? Take a moment to describe in your own words why computers would care. Pay particular attention to how computers store data in memory, and how making something immutable may help with that storage.
---

It is important to outline what items and values can be changed and ones that can not. There are systems that are defined as a "source of truth" usually in identity tools. This means that system and the data connected to a certain person is the one single correct source. The computer cares that an aspect of that person can not be changed, or the source of truth can not be trusted. 
---

### Software Engineering Exploration and Reflection (Deeper Thinking Part 2)

As someone learning about software engineering and application development, you need to understand the real-world complexities and challenges that professional developers face when building large-scale applications. This assignment will help you explore the field and reflect on what it means to work in software development.


Find three different sources that discuss major complications, failures, or challenges in building real-world applications. Look for diverse perspectives - perhaps a case study of a software failure, a technical blog post from an engineering team discussing lessons learned, or an industry report on development challenges. Very are a fair number of blogs on switching from one language to another, and why that was selected. Your sources should come from credible places like engineering blogs, tech publications, academic sources, or documented case studies.

After reading your sources, write a reflective response (3 paragraphs, approximately 150-200 words each) that explores:

- What surprised you most about the challenges these applications faced? What complications did you not expect, and how do these real-world problems differ from what you might encounter in coursework or small personal projects?

- Based on your research, how do you now view the role of a software engineer? What skills beyond coding seem most important, and what aspects of the job appear most challenging or rewarding?

- How does this research influence your understanding of software development as a career field? What areas would you want to learn more about, and what questions do you still have about working in application development?

This is a personal reflection meant to help you think more deeply about the software engineering field. Focus on your genuine reactions and insights rather than trying to provide "correct" answers. Include mentions of your sources, but the emphasis should be on your own thinking and learning process. Make sure to link your sources, and write your reflection below. 

---
Sources: 
https://www.cio.com/article/286790/software-testing-lessons-learned-from-knight-capital-fiasco.html
https://slack.engineering/stabilize-modularize-modernize-scaling-slacks-mobile-codebases/
https://spectrum.ieee.org/how-the-boeing-737-max-disaster-looks-to-a-software-developer

Report on Real-World Software Engineering Challenges

In reading about these real-world cases, the thing that surprised me most was how often organizational pressure, hidden assumptions, and legacy baggage play a bigger role in failures than pure coding mistakes. In the Knight Capital fiasco, a configuration or test flag ended up running in production and caused a $440 million loss in 30 minutes, not because someone got a loop wrong but because risk management, deployment discipline, and oversight failed. At Slack, scaling the mobile apps revealed that inconsistent architectural patterns, long build times, and tangled interdependencies were major bottlenecks, forcing a multi-year “Project Duplo” to stabilize, modularize, and modernize. And in Boeing’s case, the MCAS software was introduced to mask deeper hardware–design issues, with limited transparency and assumptions carried over from earlier models. These show that the problems in large systems are often subtle: assumptions about how components should interact, decisions made for expediency, and the inertia of prior design choices. Those are rarely captured in small classroom projects, which tend to assume a clean, greenfield setting.

After studying these, I now see that a software engineer’s role extends far beyond writing correct algorithms. You must think about architecture, modularity, testing and monitoring, risk mitigation, and system evolution. In Slack’s case, engineers had to weigh whether to fully rewrite or refactor gradually; they also had to propose metrics and risk models for each stage of the refactor. In Knight’s example, engineers needed to know deployment strategies, configuration isolation, and how to create retrospectives that surface hidden problems. In Boeing’s situation, engineers had to reason about how software would compensate for or mask hardware changes, with all of the safety, regulatory, and human factors that brings. The most challenging aspects appear to be reconciling conflicting priorities (speed vs. safety vs. maintainability), keeping large teams aligned on patterns, and anticipating failure modes. The most rewarding parts may come when you refactor a messy system into something cleaner, or when your monitoring and safeguards prevent a disaster.

This research has shifted how I look at software development as a career: it’s as much about engineering judgment, communication, and long-term thinking as it is about coding fluently. I’m now more curious about observability systems, chaos engineering, deployment pipelines, and large-scale modularization strategies. I still wonder: how do teams decide when to rewrite versus refactor? How do you convince leadership to invest in long-term tech health when short-term features dominate? And how do engineers ensure that hidden assumptions or “band-aids” don’t accumulate and become systemic risks? These are questions I’d like to explore further as I prepare for working in real, complex systems.