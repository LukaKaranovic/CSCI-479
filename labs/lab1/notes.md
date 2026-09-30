# Lab 1 - Notes

## Data Exploration/Pre-processing

Exploring and trying to understand the data before using it is essential.

- Data has different formats (csv - comma separated value, xlsx - excel spreadsheets, arff - attribute-relation file format)
- Do not manually handle data
- Ways to explore/pre-process data: ML platforms, excel, openoffice calc, write your own program, or a table (using DBMS)

## Goals of data pre-processing

What do we want to achieve by exploring and pre-processing the data?

- Whether attribute is discrete, continuous, nominal, ordinal, etc.
  - If it's qualitative - how many distinct values appear? frequency of those distinct values
    - knowing frequency will help with calculating probabilities
  - If it's continuous - what is the distribution and range of that attribute?
    - we may try to convert continuous data into discrete data (since a lot of ML algorithms can't handle continuous attributes very well)
      - discretization or binarization:
        - how do we choose what values for categories thresholds?
          - domain knowledge

Each ML algorithm will have its own characteristics (strengths and weaknesses)

- Each type of algorithm will require their own specific data pre-processing procedure.

## Learning outcome for labs and assignments

- No lab submissions - for practice
- Submit a report for assignments - narrative is as (or more) important as result
  - report back how you get the data exploration results (tools, methods, justification)
  - Make sure report is easy to read, easy to understand
