import matplotlib.pyplot as plt

x1 = ["BSE", "BSCIT", "BCS", "BBIT"]
y1 = [200, 400, 250, 180]

plt.bar(x1, y1, label="yellow Bar", color='y')
plt.plot()
plt.xlabel("Course")
plt.ylabel("Number of students")
plt.title("INTAKE AS PER THE COURSES")
plt.legend()
plt.show() 