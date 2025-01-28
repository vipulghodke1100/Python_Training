'''Write python program to extract email address from dataframe column. Please use 
following sample dataframe.(Feel free to create new one). '''

import pandas as pd
import re
data = { 
        "Company Name": ["ABC Inc.", "XYZ Corporation", "Tech Solutions Ltd.", 
        "Global Services LLC", "Innovative Ventures"], 
        "Description": ["Contact us at info@abcinc.com for more information.", 
                        "For inquiries, email us at contact@xyzcorp.com.", 
                        "Tech Solutions Ltd. provides support via support@techsolutions.com.", 
                        "Reach out to us at info@globalservicesllc.net for business inquiries.", 
                        "Email us at hello@innovativeventures.org for partnership opportunities."] 
        } 


def find_match(row):
    """_summary_

    Args:
        row (dataframe): takes pandas dataframe as input

    Returns:
        _type_: _description_
    """
    pattern= r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    result= re.search(pattern,row['Description'])
    print(result)
    return result.group() 
    

def main_function():
    df=pd.DataFrame(data)
    df['email']=df.apply(find_match , axis=1)
    print(df[["Company Name","email"]])
    
    
    
if __name__=='__main__':
    main_function()
         
