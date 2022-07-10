from flask import Flask, redirect, render_template, request, session, flash

app = Flask(__name__)

app.secret_key = "It's a secret" # used to prevent Cross Site Request Forgery-allows a CSRF token to be generated and stored in the user's session data


# Route Security: Although a small application, I chose to keep the GET and POST routes separate 
# as a good practice to reduce the chance of template injection. Routes in Flask are mapped to the Python route function.

todos = [] # list variable where the task names are saved. this serves as a mock database

@app.route('/') # home page route that displays the task entry form
def home():
    return render_template("index.html") # home page html

@app.route('/create/task', methods=['POST']) # not visible to the user-this route collects info from the form for data handling
def create_task():
    if len(request.form["task_name"]) > 0: # if check for form validation to prevent empty strings being saved into the  list variable 
        todos.append(request.form["task_name"].title()) # adds the string name to the todos list from <input type="text" name="task_name"> as the list element.
        print(todos) # using print to verify that the form validation is working correctly and that the element has been stored in the list variable "todos"
        return redirect('/show/list') # if validation is True, the form string is passed to the list as a list element to be displayed to the user
    else:
        flash("Task Must Be At Least 1 Character", "task_entry") # if validation failed then flash the message to inform the user
        return redirect('/') # redirects back to home for the user to retry the task entry

@app.route('/show/list') # task list route where the tasks are displayed for the user to see
def show_list():
    if todos == []: # form validation to trigger flash message
        flash(None, "empty_list") # "empty list" is the filter variable used to identify the HTML location where the message will display
    return render_template("show_list.html", todos=todos) # template variable to display the list[element] on line 27 in show_list.html

@app.route('/destroy/task/<todo>') # imports todo list element as a template variable from the template to be passed as an identifier for deletion in the list method .remove().
def destroy_task(todo):
    todos.remove(todo) # .remove(): Element to be deleted is mentioned using list name and element.
    print(todos) # using print to verify that the element has been removed the list variable "todos"
    return redirect('/show/list') # redirects back to the task list page with a current list.





if __name__=="__main__":
    app.run(debug=True)