import pandas as pd 
students = pd.DataFrame({"Name": ["Alex", "Maria", "John"], "Age": [20,21,19], "Grade": [85,92,78] })
print(students)

students["Grade"]
students["Name"]

students.iloc[1]


pd.Series([20,21,19], name="age")


students.head()
students.tail()
students.shape

employees_imp = pd.read_csv('employees.csv')
employees_imp.head()
print(employees_imp.head())
print(employees_imp.shape)

employees_imp.columns
employees_imp.index
employees_imp.info()

employees_imp[["Name", "Department"]]
employees_imp.iloc[0]

print(employees_imp["Department"] == "IT")
print(employees_imp[employees_imp["Department"] == "Sales"])
print(employees_imp[employees_imp["Salary"] < 3000])
print(employees_imp[
    (employees_imp["Department"] == "IT") 
    & (employees_imp["Salary"] > 3000)
    ])
print(employees_imp[employees_imp["Salary"] >= 3000])

employees_imp["Annual_Salary"] = employees_imp["Salary"] * 12
print(employees_imp.head())

print(employees_imp.sort_values(by="Annual_Salary", ascending=True))
print(employees_imp["Department"].value_counts())

print(employees_imp.groupby("Department")["Salary"].mean())
print(employees_imp.groupby("Department")["Salary"].agg(["mean", "min", "max"]))
print(employees_imp.groupby("Department")["Salary"].agg(["count", "mean", "min", "max"]))



test = pd.DataFrame({
    "Name": ["Alex", "Maria", "John", "Anna"],
    "Salary": [3000, None, 3500, None]
})

print(test)
print(test.isna().sum())

print(test.dropna())
print(test)

print(test["Salary"].fillna(test["Salary"].mean()))

print(test.dtypes)
print(employees_imp.dtypes)

employees_imp["Salary_K"] = employees_imp["Salary"] / 1000
print(employees_imp)

print(employees_imp[
    (employees_imp["Department"] == "IT") 
    & (employees_imp["Salary_K"] > 3.0)
    ])

print(employees_imp.loc[0, ["Name", "Salary"]])
print(employees_imp.loc[[0, 2, 5],["Name", "Department", "Salary"]])


employees_sort_salary = employees_imp[employees_imp["Salary"] > 3000].sort_values(by="Salary", ascending=False)
print(employees_sort_salary[["Name", "Department", "Salary"]])



employees_imp["Department_Full"] = employees_imp["Department"].map({
    "IT": "Information Technology",
    "HR": "Human Resources",
    "Sales": "Sales Department",
    "Finance": "Finance Department"
})
print(employees_imp[["Department", "Department_Full"]])


employees_imp["Salary_Level"] = employees_imp["Salary"].apply(
    lambda salary: "High" if salary > 3500 else ("Low" if salary < 3000 else "Medium")
)
print(employees_imp)


employees_imp["Department_Code"] = employees_imp["Department"].map({
    "IT": 1,
    "HR": 2,
    "Sales": 3,
    "Finance": 4
})
print(employees_imp)


employees_group_department = employees_imp.groupby("Department")
print(employees_group_department["Name"].count())
print(employees_group_department["Salary"].agg(["mean", "max"]).sort_values(by = "mean", ascending=False))


employees_imp = employees_imp.rename(
    columns= {
        "Name": "Employee_Name",
        "Salary": "Monthly_Salary"
    }
)
print(employees_imp.head())



new_employees = pd.DataFrame({
    "Employee_Name": ["Peter", "Linda"],
    "Department": ["IT", "HR"],
    "Monthly_Salary": [3300, 2900]
})
employees_all = pd.concat([employees_imp, new_employees], ignore_index=True)
print(employees_all)


employees = pd.DataFrame({
    "Employee_ID": [1, 2, 3],
    "Employee_Name": ["Alex", "Maria", "John"]
})
salaries = pd.DataFrame({
    "Employee_ID": [2, 1, 3],
    "Salary": [3000, 2500, 3500]
})
merg_emp_sal = pd.merge(employees, salaries, on="Employee_ID")
print(merg_emp_sal)


departments = pd.DataFrame({
    "Department": ["IT", "HR", "Sales"],
    "Manager": ["Bob", "Kate", "Mike"]
})
employees_merg_depart = pd.merge(employees_all, departments, on="Department")
print(employees_merg_depart)


#Небольшой проект на основе прохождение КУРСА
print(employees_all[(employees_all["Department"] == "IT") & (employees_all["Monthly_Salary"] > 3000)].sort_values(by="Monthly_Salary", ascending=False)) 
employees_group_department2 = employees_all.groupby("Department")
print(employees_group_department2["Employee_Name"].count())
print(employees_group_department2["Monthly_Salary"].mean())
print(employees_all.isna().sum())
employees_all["Annual_Salary"] = employees_all["Annual_Salary"].fillna(employees_all["Monthly_Salary"] * 12)
print(employees_all)
print(employees_group_department2["Monthly_Salary"].mean().sort_values(ascending=False).head(1))




#========================================
#Level 2
sales = pd.DataFrame({
    "Customer": ["Alex", "Maria", "John", "Alex", "Anna", "John", None, "Artem"],
    "Product": ["Laptop", "Phone", "Laptop", "Laptop", "Tablet", "Laptop", "Phone", "Tablet"],
    "Price": [1200, 800, 1200, 1200, None, 1200, 800, 2000],
    "Quantity": [1, 2, 1, 1, 3, 1, 2, 3],
    "Date": ["2026-01-05", "2026-01-06", "2026-01-07",
             "2026-01-05", "2026-01-08", "2026-01-07", "2026-01-09", "2026-03-05"],
})
print(sales)

#1) Исследуем
print(sales.index)
print(sales.columns)
print(sales.dtypes)
print(sales.isna().sum())
print(sales.duplicated().sum())
print(sales.shape)

print(sales[sales.duplicated()])
sales = sales.drop_duplicates()
print(sales)

sales = sales.reset_index(drop=True)
print(sales)

print(sales[sales.isna().any(axis=1)])

sales = sales.dropna(subset=["Customer"])
print(sales)

sales["Price"] = sales["Price"].fillna(sales.groupby("Product")["Price"].transform("mean"))
print(sales)

#2) Работа с Датами
print(sales.dtypes)
sales["Date"] = pd.to_datetime(sales["Date"])
print(sales.dtypes)
sales["Year"] = sales["Date"].dt.year
sales["Month"] = sales["Date"].dt.month
sales["Day"] = sales["Date"].dt.day
print(sales[["Date","Year", "Month", "Day"]])
print(sales[sales["Date"] > "2026-02-01"])   
print(sales[(sales["Month"] == 1) & (sales["Year"] == 2026)])

sales["Days_Since_Sale"] = pd.to_datetime("2026-03-10") - sales["Date"]
print(sales)
print(sales.dtypes)

sales["Days_Since_Sale"] = sales["Days_Since_Sale"].dt.days
print(sales[["Date", "Days_Since_Sale"]])
print(sales.dtypes)

print(sales[sales["Days_Since_Sale"] > 60])

#3) Работа со строками через str.
sales["Customer_Upper"] = sales["Customer"].str.upper()
print(sales["Customer_Upper"])

print(sales[sales["Product"].str.contains("a", case=False)])
print(sales[sales["Customer"].str.startswith("A")])

print(sales[sales["Customer"].str.endswith("a")][["Customer", "Product"]])

sales["Product_New"] = sales["Product"].str.replace(
    "Laptop", "Notebook"
)
print(sales["Product_New"])

sales["New_Name_Customer"] = sales["Customer"].str.replace(
    "a", "@"
)
print(sales["New_Name_Customer"])

names = pd.Series(["Alex Smith", "Maria Ivanova", "John Brown"])
print(names)

#names = names.str.split(" ")
names = names.str.split(" ", expand=True)
print(names)
names.columns = ["First_Name", "Last_Name"]
print(names)

names["Initial"] = names["First_Name"].str.get(0)
print(names)

#4)query
print(sales.query("Price >= 1200 and Quantity >= 2"))

print(sales.query("Product == 'Tablet' and Days_Since_Sale < 30"))

min_quantity = 2
print(sales.query("Quantity >= @min_quantity"))

#5)pivot_table
print(pd.pivot_table(
    sales,
    index="Product",
    columns="Month",
    values="Quantity",
    aggfunc="sum",
    fill_value=0
))

print(pd.pivot_table(
    sales,
    index="Customer",
    columns="Product",
    values="Quantity",
    aggfunc="sum",
    fill_value=0
))

print(sales)

print(pd.pivot_table(
    sales,
    index="Product",
    values=["Quantity", "Price"],
    aggfunc= {
        "Quantity": "sum",
        "Price": "mean"
    }
))

print(pd.pivot_table(
    sales,
    index = "Product",
    columns="Month",
    values="Quantity",
    aggfunc="sum",
    margins="True",
    fill_value=0
))

#6) еще задачи про merge
customers = pd.DataFrame({
    "Customer_ID": [1, 2, 3, 4],
    "Customer": ["Alex", "Maria", "John", "Anna"]
})

orders = pd.DataFrame({
    "Customer_ID": [1, 2, 2, 5],
    "Order": ["Laptop", "Phone", "Tablet", "Monitor"]
})

print(pd.merge(
    customers,
    orders,
    on="Customer_ID",
    how="inner"
))

print(pd.merge(
    customers,
    orders,
    on="Customer_ID",
    how="left"
))

print(pd.merge(
    customers,
    orders,
    on="Customer_ID",
    how="right"
))

print(pd.merge(
    customers,
    orders,
    on="Customer_ID",
    how="outer"
))

left = pd.DataFrame({
    "Customer_ID": [1, 1, 2],
    "City": ["Almaty", "Astana", "Shymkent"]
})

right = pd.DataFrame({
    "Customer_ID": [1, 1, 3],
    "Product": ["Laptop", "Phone", "Tablet"]
})

print(pd.merge(
    left,
    right,
    on="Customer_ID",
    how="inner"
))

print(left["Customer_ID"].duplicated().sum())
print(right["Customer_ID"].duplicated().sum())

print(left["Customer_ID"].value_counts())
print(right["Customer_ID"].value_counts())

print(pd.merge(
    left,
    right,
    on="Customer_ID",
    #validate="one_to_many"
))

print(pd.merge(
    customers,
    orders,
    on="Customer_ID",
    how="outer",
    indicator=True
))

merged = pd.merge(
    customers,
    orders,
    on="Customer_ID",
    how="outer",
    indicator=True
)

print(merged[merged["_merge"] == "left_only"])

dirty = pd.DataFrame({
    "Department": [" IT ", "it", "HR", " hr ", "Sales", "sales ", "N/A", None]
})

print(dirty)
dirty["Department"] = dirty["Department"].str.strip()
dirty["Department"] = dirty["Department"].str.upper()
print(dirty)

dirty["Department"] = dirty["Department"].replace(
    "N/A", pd.NA
)
print(dirty)
print(dirty.isna().sum())

dirty_2 = pd.Series(
    [
        "N/A", "NA", "none", "-", ""
    ]
)
print(dirty_2)
dirty_2 = dirty_2.replace(["N/A", "NA", "none", "-", ""], pd.NA)
print(dirty_2)
print(dirty_2.isna().sum())

