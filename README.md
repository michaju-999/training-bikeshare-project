Project: Explore US Bikeshare Data
===================================

Resources referenced while completing this project:

1. pandas documentation - https://pandas.pydata.org/docs/
   Used for help with DataFrame filtering, datetime conversion, and value_counts().

2. Python datetime documentation - https://docs.python.org/3/library/datetime.html
   Referenced for understanding how to work with date/time objects.

3. Stack Overflow - https://stackoverflow.com
   Searched for tips on using .mode()[0] to get the most frequent value in a Series,
   and for help formatting time output from seconds into hours/minutes.

4. Udacity course materials and lessons on Python and pandas.

Notes:
- Washington does not include Gender or Birth Year columns, so user_stats() 
  handles that case with a check before trying to access those columns.
- A display_raw_data() function was added as an extra feature to let users 
  page through 5 rows of raw data at a time.

In addition to the above, the below is part of a seperate commit on a branch. specifically, we are providing some narrative explination of the project. In this case,
the project utilizes a data foundation of appoximately 90,000 lines of data across 3 CSV files. 