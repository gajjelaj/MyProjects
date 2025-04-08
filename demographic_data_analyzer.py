import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex']== 'Male']['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_count = df[df['education'] == 'Bachelors']['education'].count()
    total_count = df['education'].count()
    percentage_bachelors = round((bachelors_count/total_count)*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_edu_df = df[(df['education'] == 'Bachelors') | 
                       (df['education'] == 'Masters') | 
                       (df['education'] == 'Doctorate')]
    higher_edu_count_50k = higher_edu_df[higher_edu_df['salary'] == '>50K']
    higher_education_rich = round(higher_edu_count_50k['education'].count()/higher_edu_df['education'].count()*100,1)
    lower_edu_df = df[((df['education'] != 'Bachelors') & 
                      (df['education'] != 'Masters') & 
                      (df['education'] != 'Doctorate'))]
    lower_edu_50k = lower_edu_df[lower_edu_df['salary'] == '>50K']
    lower_education_rich = round(lower_edu_50k['education'].count()/lower_edu_df['education'].count()*100,1)
    lower_education_rich

    # percentage with salary >50K
    #higher_education_rich = None
    #lower_education_rich = None

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
 

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_work_hours = df['hours-per-week'].min()
    total_count_min_work_hours_df = df[df['hours-per-week'] == min_work_hours]
    count_min_work_50K = total_count_min_work_hours_df[total_count_min_work_hours_df['salary'] == '>50K']['salary'].count()
    rich_percentage = (count_min_work_50K/total_count_min_work_hours_df['salary'].count())*100
    rich_percentage
 

     

    # What country has the highest percentage of people that earn >50K?
    total_country_count = df['native-country'].value_counts()
    country_count_50K = df[df['salary']=='>50K']['native-country'].value_counts()
    earning_country_percentage = (country_count_50K/total_country_count)*100
    highest_earning_country = earning_country_percentage.idxmax()
    highest_earning_country_percentage = round(earning_country_percentage.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_oc = df.groupby('occupation').size()
    top_IN_occupation = top_oc.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
