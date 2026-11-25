import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# 1. Line Plot
plt.figure()
plt.plot(x, y, marker='o')
plt.title("Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid()
plt.show()

# 2. Scatter Plot
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 3. Bar Chart
plt.figure()
plt.bar(x, y)
plt.title("Bar Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 4. Pie Chart
subjects = ['Python', 'Java', 'C', 'DBMS']
marks = [30, 25, 20, 25]

plt.figure()
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

# 5. Box Plot
data = [10, 20, 30, 40, 50, 60, 70, 80]

plt.figure()
plt.boxplot(data)
plt.title("Box Plot")
plt.ylabel("Values")
plt.show()