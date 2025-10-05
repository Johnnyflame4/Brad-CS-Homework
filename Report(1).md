# Report

Please answer the questions below. Make sure to ask questions if you have them. 


For all these questions, it is recommended you use the python interpreter and try out the code.  You can also use the python visualizer to help you visualize the code.  You can find the visualizer here: [http://www.pythontutor.com/visualize.html#mode=edit](http://www.pythontutor.com/visualize.html#mode=edit)


1. Correct the following loop.
   ```python
   value = None
   while value == "quit":
       value = input("Enter a value or quit: ")
       print(value)
   ```
    ```python
    ## put your corrected code below this line
   value = None
   while value == "quit":
        value = input("Enter a value or quit: ")
        if value != "quit":
    print("Your value is " + value)

    ```

2. The above code uses a None value to initialize the input variable. This works because python can let a variable be multiple types, but in some languages, you would have to match the type. Assuming you had to match the type (str), what would be a good default input value, that could never cause the loop to not run at least once? Provide reasoning for your logic as there are multiple correct answers. With that said, there is one that is more 'standard' than the rest, so feel free to openly discuss options that come to mind (you do not have to come up with the standard answer, but try to!). 
   In this situation the str("quit") would guarantee that the loop runs at least once because the first line of the while loop is when the value equals "quit" so it will always run until the value is not quit. 

3. Write a small loop that will keep repeating until someone 
   enters a number greater than 0, and less than 5. It has to be
   whole numbers (hint: look up .isnumeric() from the team activity).

   ```python
    n = ""
    while True:
        n = input("Enter a value between 1 and 4")
        if n.isnumeric():
            n = int(n)
            if 0 < n < 5:
                print("Your number is between 1 and 4")
                break
        print("Invalid input")

   ```

4. Draw a flow diagram for your solution to #3
   

5. Looking back at homework #2, we actually had a type of 'loop' in the provided code (look near the main function). First copy the bit of code that causes the loop.
    ```python
    again = input("Run again (y or n)? ")
    if again.strip().lower() == 'y':
        main()  # discussion item: what does this do?
    else: 
        print("Good luck on the move!")
    ```
    Now: what would be some of the pros and cons of looping in such a way (think about 'frames' you see in the python visualizer)?
    This allows you to continue to enter new temperatures if you wish, which is good instead of having to run the program every time you want to test. 

    The drawbacks are that every recursion and repetition of the main() adds to the memory stack and create a stack overflow. It also makes the program harder to debug if there is an issue because of the unclear looping logic. 

6. Thinking about edge cases, it is very common to get an off-by-one (OB1) error with loops. 
   Create two test cases (just as examples/inputs) for the following code. They 
   should both be 'correct' cases, but one of them should uncover the error in the code.

   ```python
    def count_backwards(value: int) -> None:
        """ Counts from value to 0, printing even values until 10 (including 10), and 
        then odd values."""
       counter = value
       while counter >= 0:
          if counter > 10:
            if counter % 2 == 0:
                print(counter)
          else:
            if counter % 2 == 1:
                print(counter)
          counter -= 1
   ```
   * Example test one: >>> count_backwards(10)
                         * 10 (this is the error and it won't print this because the if statement is >, not >=)
                         * 9
                         * 7
                         * 5
                         * 3
                         * 1
   * Example test two: >>> count_backwards(9)
                         * 9
                         * 7
                         * 5
                         * 3
                         * 1

 7. When thinking of these edge cases and OB1 errors, it is common to say one should test
    every condition plus-minus 1. In your opinion, is this beneficial? Why or why not?
    It is impractical to test every condition plus or minus 1 when in a professional environment. It would be best to double check your work as you go to ensure signs and operators are correct.

## Application Runs
The following questions will require you run the Accessibility Analyzer to generate results. 

> Do display colors in the markdown, you will have to switch to standard html and built in styles. For example, the code below, will generate a 'teal' block with black text. Feel free to copy and past the block, only modifying the color values as you need.   
> ![#4ECDC4](https://placehold.co/15x15/4ECDC4/4ECDC4.png) `#4ECDC4`

1. Check WCAG contrast compliance - pick two colors to run with the WCAG option (1) in the color app.
   
   1.1  What two colors did you pick (use the color block but update values)
      * ![#EA5C10](https://placehold.co/15x15/EA5C10/EA5C10.png) `#EA5C10`
      * ![#495269](https://placehold.co/15x15//495269/495269.png) `#495269`


   1.2  What was the result, use the block below to copy and paste the result of the test
   ```
   copy and paste here
   ```    
    ratio = contrast_ratio(245, 73, 39, 73, 82, 105)
    print(passes_wcag_level(ratio, "AA_NORMAL"))
    print(passes_wcag_level(ratio, "AA_LARGE"))
    print(passes_wcag_level(ratio, "AAA_NORMAL"))
    print(passes_wcag_level(ratio, "AAA_LARGE"))

Results:
False
False
False
False


   1.3 Did the results show what you thought?  
   It was what I expected because the first color is ver red heavy and that is very hard to see against the grey color. 

   1.4 Explore colors until you can find two that pass all the WCAG compliance categories.  What two did you find?
   White on black and black on white work for all WCAG compliance.
       
      * ![#000000](https://placehold.co/15x15/000000/000000.png) `#000000`
      * ![#FFFFFF](https://placehold.co/15x15/FFFFFF/FFFFFF.png) `#FFFFFF`
  
1.  Analyze color properties - pick a color to run with this option

    2.1 What color did you pick?
    
       * ![#138BC5](https://placehold.co/15x15/138BC5/138BC5.png) `#138BC5`
    
    2.2 What are the results, copy and paste them below.
     ```
     copy and paste here
     ```
    print (round(calculate_luminance(19, 139, 197)), 3)
    .226
    print(calculate_brightness(19, 139, 197))
    109

2. Test colorblind accessibility - pick two colors to analyze. You need to find two that would end up being the same color (or close to the same color) depending on the type of color blindness. 

    3.1 What colors did you pick?

     * ![#FF003F](https://placehold.co/15x15/FF003F/FF003F.png) `#FF003F`
     * ![#7F7F00](https://placehold.co/15x15/7F7F00/7F7F00.png) `#7F7F00`

    3.2 What were the results for each of them - copy and paste below in each block
    ```
     color 1: copy and paste here
    ```
    print(simulate_colorblindness(255, 0, 63, "protanopia"))
    (127, 127, 63)
    ```
     color 2: copy and paste here
    ```
    print(simulate_colorblindness(127, 127, 0, "tritanopia"))
    (127, 127, 63)

    3.3 Now run modified (by the colorblindness type) colors through the Check WCAG contrast compliance option. Spoiler, at least one should fail, but there may be rare cases it passes. You should also run the original colors through the Check WCAG.
 
     * ![#7F7F3F](https://placehold.co/15x15/7F7F3F/7F7F3F.png) `#7F7F3F`
     * ![#7F7F3F](https://placehold.co/15x15/7F7F3F/7F7F3F.png) `#7F7F3F`

    3.4 What were the results for that test
    ```
      copy and paste here
    ```
    ratio = contrast_ratio(127, 127, 63, 127, 127, 63)
    print(passes_wcag_level(ratio, "AA_NORMAL"))
    print(passes_wcag_level(ratio, "AA_LARGE"))
    print(passes_wcag_level(ratio, "AAA_NORMAL"))
    print(passes_wcag_level(ratio, "AAA_LARGE"))
    False
    False
    False
    False

    ratio = contrast_ratio(255, 0, 63, 127, 127, 0)
    print(passes_wcag_level(ratio, "AA_NORMAL"))
    print(passes_wcag_level(ratio, "AA_LARGE"))
    print(passes_wcag_level(ratio, "AAA_NORMAL"))
    print(passes_wcag_level(ratio, "AAA_LARGE"))
    False
    False
    False
    False

    3.5 Did your your original colors pass better than the modified color blindness ones?
    No, I imagine primary colors like red and yellow are hard to pass the WCAG exactly because they are the colors that are susceptible to color blindness issues with legibility. 

3. Did running this application help you learn anything new about html / web colors? If so, what?
    HTML uses Hex color codes

> Make sure to look at your rendered document in github!  
> Before you turn it in for grading.


## Deeper Thinking

Human Computer Interaction (HCI) is a field within computer science that focuses on how people interact with technology systems. It involves designing interfaces and experiences by continuously communicating with stakeholders, conducting research into effective design patterns, and questioning assumptions about user behavior and needs. 

HCI emphasizes inclusive design - creating systems that work for people across different abilities, backgrounds, and contexts. This approach extends beyond basic accessibility compliance to consider the full spectrum of human diversity. Whether designing web applications, operating systems, VR/AR experiences, or video games, HCI practitioners integrate user research and inclusive principles throughout the development process.

HCI intersects with virtually all domains of computer science and relies heavily on collaboration between designers, developers, researchers, and clients to build systems that better serve diverse communities.

**Assignment:**

Research HCI and UX design to understand the field better. Find at least three credible sources (academic articles, professional publications, or reputable industry resources) and provide links to them. 

After reviewing your sources, write a reflection addressing these questions:

1. Based on your research, how would you define HCI and its core principles?

2. Why is inclusive design particularly important in computer science and HCI? Consider both ethical and practical implications.

3. How might the accessibility concepts you learned in this assignment (color contrast, colorblindness considerations) connect to broader HCI principles?

Your reflection should demonstrate understanding of the field while incorporating insights from your research sources. Write in paragraph form rather than bullet points, and aim for thoughtful analysis rather than simple summaries.

Sources

Nielsen Norman Group — Inclusive Design (overview and practical guidance).
https://www.nngroup.com/articles/inclusive-design

W3C Web Accessibility Initiative — Web Content Accessibility Guidelines (WCAG) 2.1 (contrast, use of color, and accessibility success criteria). 
https://www.w3.org/TR/WCAG21

Alan Dix  — Human–Computer Interaction (textbook/paper covering HCI foundations and principles). 
https://www.researchgate.net/publication/224927543_Human-Computer_Interaction

WebAIM — Understanding WCAG Contrast and Color Requirements (practical explanation of contrast ratios and why they matter). 
https://webaim.org/articles/contrast

Microsoft Inclusive Design resources — principles and practical toolkit for designing with exclusion-awareness. 
https://inclusive.microsoft.design

Reflection

Human–Computer Interaction (HCI), as I understand it after reviewing foundational texts and practitioner resources, is a multidisciplinary field concerned with designing, evaluating, and understanding interactive computing systems in the context of users’ needs, capabilities, and environments. It combines computer science, cognitive psychology, design, and social sciences to make technology usable, useful, and appropriate; core HCI principles therefore emphasize usability (effectiveness, efficiency, satisfaction), learnability, feedback and visibility, mental models, and iterative user-centered evaluation. Classic HCI texts and reviews frame these as both theoretical foundations and practical workflows: understand users and tasks, prototype interactions, evaluate with real users, and refine designs based on evidence. 

Inclusive design is central to HCI not just as an ethical obligation but as a practical design strategy that improves products for everyone. Ethically, designing inclusively recognizes that technology can amplify social inequities and that designers have responsibility to reduce rather than reinforce exclusion; practically, inclusive practices (like designing for a single extreme user and then extending to many) create resilient, flexible systems that serve more contexts and edge cases, reducing long-term support costs and broadening market reach. Organizations like Microsoft and NN/g frame inclusive design as repeatable principles — recognize exclusion, learn from diversity, and solve for one then extend to many — which show that inclusion is both a moral imperative and a pragmatic approach to better product outcomes. 

Accessibility specifics such as color contrast and color-use rules are concrete instances of broader HCI commitments: to perceptual clarity, error prevention, and universal usability. WCAG’s guidance about luminance contrast ratios and the W3C’s rules on not relying solely on color to convey information translate the abstract HCI goals (e.g., making system state visible, ensuring affordances are perceivable) into measurable design constraints; WebAIM’s breakdown of contrast ratios shows how a seemingly small visual choice directly affects readability and task success for people with low contrast sensitivity or color-vision deficiency. In other words, attention to color contrast and colorblind-friendly palettes is not an isolated checklist item but enacts HCI principles—respecting diverse perceptual abilities, supporting robust mental models, and reducing cognitive load—so that interfaces remain usable across lighting conditions, devices, and user differences. This directly relates to the WCAG calculation function we wrote in our color tools program. It calculates the readability of text combining the color of the text against a specific background color. 

Bringing these threads together, the HCI practitioner’s job is to translate human diversity into design decisions: empirical user research reveals how people actually perceive and act; accessibility standards give testable criteria (e.g., contrast ratios, non-color cues) to guarantee baseline functionality; and inclusive design mindsets ensure that solutions account for social, cultural, and situational differences rather than only an “average” user. This combination of evidence-based methods, clear technical guidance (like WCAG), and ethical commitments creates interfaces that not only comply with standards but genuinely empower a wider range of people to accomplish their goals. That synergy is what makes HCI both intellectually rich and pragmatically indispensable in modern computing.