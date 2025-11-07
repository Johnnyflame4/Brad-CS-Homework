# Homework 09 Report

1. Which Airlines have the most flights in 2015? How many flights did they have?
   Southwest Airlines Co.      : 221586

2. Which Airlines have the least flights in 2015? How many flights did they have?
   Virgin America              : 10403

3. Data is an important aspect of our society, and it is important to understand how to work with it. What are some ways you can see data being used in your future career?
   In cyber security, data is the thing that we are protecting, but also how we make decisions. We review data (logs in this case) to understand if the actions taken and executed on an IT system are considered a normal business process as well as by an authorized individual / user. 

4. You should start thinking about larger applications, list some applications /  projects you would like to work on? Narrow it down to projects that you can accomplish within a couple weeks?
   I have been thinking about how to build a cyber compliance software that helps users track their current implementation status against certain controls (NIST 800-171 in this case). 
   At minimum it would work like a checklist allowing you to click on and off the controls you feel that are implemented correctly. 
   Going deeper it may help you with creating the SSP and implementation statements of how you are meeting the control. 

5. Provide output of you running `doctest` with the `-v` flag enabled (i.e. the output generated on your screen)

    ```
PS C:\Users\Brad\Documents\VS Code Projects\Python Projects\Homework 09\homework09-Johnnyflame4\src> python -m doctest flight_counter.py -v
Trying:
    build_counters("../data/flights10.dat", {"AA": "American Airlines",                             "DL": "Delta Airlines", "UA": "United Airlines"})
Expecting:
    {'UA': 2, 'DL': 2}
ok
Trying:
    load_airlines("../data/airlines.dat")                    # doctest: +NORMALIZE_WHITESPACE
Expecting:
    {'UA': 'United Air Lines Inc.',
    'AA': 'American Airlines Inc.',
    'US': 'US Airways Inc.',
    'F9': 'Frontier Airlines Inc.',
    'B6': 'JetBlue Airways',
    'OO': 'Skywest Airlines Inc.',
    'AS': 'Alaska Airlines Inc.',
    'NK': 'Spirit Air Lines',
    'WN': 'Southwest Airlines Co.',
    'DL': 'Delta Air Lines Inc.',
    'EV': 'Atlantic Southeast Airlines',
    'HA': 'Hawaiian Airlines Inc.',
    'MQ': 'American Eagle Airlines Inc.',
    'VX': 'Virgin America'}
ok
Trying:
    counters = {"AA": 10, "DL": 5, "UA": 3}
Expecting nothing
ok
Trying:
    airlines = {"AA": "American Airlines", "DL": "Delta Airlines", "UA": "United Airlines"}
Expecting nothing
ok
Trying:
    print_counters(counters, airlines)                   # doctest: +NORMALIZE_WHITESPACE
Expecting:
    American Airlines: 10
    Delta Airlines:     5
    United Airlines:    3
**********************************************************************
File "C:\Users\Brad\Documents\VS Code Projects\Python Projects\Homework 09\homework09-Johnnyflame4\src\flight_counter.py", line 105, in flight_counter.print_counters
Failed example:
    print_counters(counters, airlines)                   # doctest: +NORMALIZE_WHITESPACE
Expected:
    American Airlines: 10
    Delta Airlines:     5
    United Airlines:    3
Got:
    American Airlines: 10
    Delta Airlines   : 5
    United Airlines  : 3
2 items had no tests:
    flight_counter
    flight_counter.main
2 items passed all tests:
   1 test in flight_counter.build_counters
   1 test in flight_counter.load_airlines
**********************************************************************
1 item had failures:
   1 of   3 in flight_counter.print_counters
5 tests in 5 items.
4 passed and 1 failed.
***Test Failed*** 1 failure.
    ```

6. Output of running `python3 flight_counter.py -h`, and what it means in your own words. (Note: windows is python, and file location may vary based on where you are running it. The above assume linux and running from the homework src directory)

    ```
   Id     Duration CommandLine
  --     -------- -----------
   1        0.121 try { . "c:\Users\Brad\AppData\Local\Programs\Microsoft VS Code\resources\app\out\vs\work… 
   2        0.016 cd "c:\Users\Brad\Documents\VS Code Projects\Python Projects\Homework 09\homework09-Johnn… 
   3        0.071 C:/Python313/python.exe flight_counter.py -h
   4        0.044 python flight_counter.py -h
   5        0.042 python flight_counter.py -h

    ```


## Deeper Thinking

When dealing with large datasets, or data in general, there needs to be a careful consideration of biases, collection, and use of that data. For example, it is very possible for real world data to be biased towards collection biases or sampling biases, and there are very real ethical issues in how that data is being used especially if a bias is not being taken into account. Take a moment to research some issues with data collection and use, and list some examples you can find. You may even find some examples that are related to data you supply on a data basis (i.e. what you give to social media)

1. Sampling Bias and Collection Bias
Issue: Non-representative Data

Data that does not capture the full population of interest can lead to skewed insights and discriminatory outcomes.

Examples:

Facial recognition datasets historically over-represented light-skinned individuals, resulting in significantly higher error rates for darker-skinned people. Multiple academic studies and audits have confirmed these disparities.

Health datasets that rely primarily on data from certain hospitals, geographic regions, or socioeconomic groups often fail to capture conditions prevalent in underrepresented communities. This has produced unequal predictive accuracy in diagnostic algorithms.

2. Labeling Bias
Issue: Human-generated labels reflect the worldview, beliefs, and limitations of annotators.

Even when data volume is large, biased labels can distort models.

Examples:

Content moderation datasets for social platforms have been shown to encode annotators’ cultural or political assumptions, leading to inconsistent classification of speech across demographic groups.

Sentiment analysis datasets sometimes treat phrases common in African American Vernacular English (AAVE) as more negative due to annotator unfamiliarity.

3. Historical and Structural Bias
Issue: Data reflects inequities embedded in society, leading models to reproduce or amplify that inequity even if sampling and labeling are technically correct.

Examples:

Predictive policing systems trained on historical crime data concentrated in over-policed neighborhoods disproportionately direct further policing to those same areas.

Credit scoring models that rely on historical credit patterns can disadvantage applicants from communities with limited access to traditional financial systems.

4. Behavioral Data Exploitation
Issue: Data collected through routine digital activity can be repurposed in ways users did not anticipate.

Examples:

Social media platforms track clicks, dwell time, and interaction patterns to build detailed behavioral profiles. These profiles can be used for targeted advertising, algorithmic content shaping, or inference of sensitive attributes (e.g., political leanings, mental health indicators).

Location data from mobile apps has been resold through data brokers, sometimes enabling inference of visits to sensitive locations such as clinics, places of worship, or political events.

5. Consent and Transparency Failures
Issue: Users do not fully understand what data is being collected, how long it is stored, or how it will be used.

Examples:

Many applications disclose broad data collection rights in lengthy terms-of-service agreements, but provide little operational transparency about how data feeds recommendation engines, third-party advertising networks, or internal analytics.

Some consumer IoT devices (e.g., smart speakers) have been found to record and transmit more data than users expected, sometimes including unintended audio captures.

6. Data Re-identification Risk
Issue: Even when data is “anonymized,” it may remain linkable to individuals when combined with other datasets.

Examples:

Several high-profile anonymized datasets—such as mobility datasets or movie rating archives—have been deanonymized by correlating them with publicly available information.

Data brokers can combine browsing data, purchase histories, and demographic information to reconstruct individual identities despite nominal de-identification.

7. Purpose Creep
Issue: Data collected for one purpose is gradually repurposed for unrelated or more intrusive uses over time.

Examples:

Fitness and health-tracking data originally gathered for personal analytics being later used for insurance risk assessment or advertising segmentation.

Employee productivity monitoring tools expanding from time tracking to granular behavioral surveillance.

8. User-Generated Content and Behavioral Traces on Social Media
Issue: Users supply large volumes of content that become valuable training data or behavioral signals, often without meaningful control.

Examples:

Photos uploaded to social networks may contribute to computer vision model training unless users opt out (where such controls exist).

Comment histories and engagement patterns serve as inputs into recommendation algorithms that shape what content individuals see, creating feedback loops.