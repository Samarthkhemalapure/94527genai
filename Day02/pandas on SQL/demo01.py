import pandas as pd
import pandasql as ps

emp_hdr =pd.read_csv("emp_hdr.csv")
query= """ SELECT empno from emp_hdr"""

result =ps.sqldf(query,{"emp_hdr": emp_hdr})
print(result)