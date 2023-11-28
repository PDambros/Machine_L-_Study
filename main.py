import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import tkinter as tk
from tkinter import messagebox

# Load the Titanic dataset
data = pd.read_csv('C:/Users/pambros/Documents/titanic.csv')

# Convert 'Sex' column to numerical using one-hot encoding
data = pd.get_dummies(data, columns=['Sex'], drop_first=True)

# Train the machine learning model
features = ['Pclass', 'Sex_male', 'Age', 'Siblings/Spouses Aboard', 'Parents/Children Aboard', 'Fare']
target = 'Survived'
X = data[features]
y = data[target]

# Instantiate and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)


def predict_survival():
    # Get values from the input fields
    pclass = int(entry_pclass.get())
    sex_male = 1 if entry_sex.get() == 'male' else 0  # Assuming you've encoded 'Sex' to 'Sex_male' already
    age = int(entry_age.get())
    siblings_spouses = int(entry_siblings_spouses.get())
    parents_children = int(entry_parents_children.get())
    fare = float(entry_fare.get())

    # Create example data for prediction
    example_data = {
        'Pclass': [pclass],
        'Sex_male': [sex_male],
        'Age': [age],
        'Siblings/Spouses Aboard': [siblings_spouses],
        'Parents/Children Aboard': [parents_children],
        'Fare': [fare]
    }
    example_df = pd.DataFrame(example_data)

    # Handle missing values in the prediction data (if necessary)
    example_df['Age'].fillna(example_df['Age'].median(), inplace=True)
    example_df['Fare'].fillna(example_df['Fare'].median(), inplace=True)

    # Make prediction using the trained model
    prediction = model.predict(example_df)

    # Display prediction result in a message box
    if prediction[0] == 1:
        messagebox.showinfo("Prediction Result", "The model predicts that the passenger survived.")
    else:
        messagebox.showinfo("Prediction Result", "The model predicts that the passenger did not survive.")


# center window
def center_window(window):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the position for the window
    x_coordinate = (screen_width - window.winfo_reqwidth()) / 2
    y_coordinate = (screen_height - window.winfo_reqheight()) / 2

    # Set the window's position
    window.geometry("+%d+%d" % (x_coordinate, y_coordinate))


# Create Tkinter window
root = tk.Tk()
root.title("Titanic Survival Prediction")

# Create labels and entry fields for input
tk.Label(root, text="Pclass (1, 2, or 3):").grid(row=0, column=0)
entry_pclass = tk.Entry(root)
entry_pclass.grid(row=0, column=1)

tk.Label(root, text="Sex (male or female):").grid(row=1, column=0)
entry_sex = tk.Entry(root)
entry_sex.grid(row=1, column=1)

tk.Label(root, text="Age:").grid(row=2, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1)

tk.Label(root, text="Siblings/Spouses Aboard:").grid(row=3, column=0)
entry_siblings_spouses = tk.Entry(root)
entry_siblings_spouses.grid(row=3, column=1)

tk.Label(root, text="Parents/Children Aboard:").grid(row=4, column=0)
entry_parents_children = tk.Entry(root)
entry_parents_children.grid(row=4, column=1)

tk.Label(root, text="Fare:").grid(row=5, column=0)
entry_fare = tk.Entry(root)
entry_fare.grid(row=5, column=1)

# Create a button to trigger the prediction
predict_button = tk.Button(root, text="Predict Survival", command=predict_survival)
predict_button.grid(row=6, columnspan=2)

# Set the window size (width x height)
root.geometry("400x300")

# Center the window on the screen
center_window(root)

# Start the Tkinter main loop
root.mainloop()
