import customtkinter as tk
import datetime
import os

button_info = []
button_instances = []
debug = False

root = tk.CTk()
root.title("MyNewt Minutes")
root.geometry("800x600")
root.configure(bg="gray")


def change_debug(_):
    global debug
    debug = not debug
    print(f"Debug mode has been" + (" enabled." if debug else " disabled."))
    if debug:
        debug_button.pack(side=tk.LEFT, padx=10, pady=10)
    else:
        debug_button.pack_forget()


# Bind ctrl+d to debug mode
root.bind("<Control-d>", change_debug)

top_frame = tk.CTkFrame(root, width=800, height=110, fg_color="white")
top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

# Create a frame for the bottom left of the window
bottom_left_frame = tk.CTkFrame(root, width=400, height=690)
bottom_left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

# Create a frame for the bottom right of the window
bottom_right_frame = tk.CTkFrame(root, width=400, height=690)
bottom_right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False)


def add_button(name, description, time, type):
    button_info.append({
        "name": name,
        "description": description,
        "time": time,
        "type": type
    })
    button = tk.CTkButton(bottom_right_frame, text=name, fg_color="darkgray", hover_color="lightgray", width=50,
                          height=30, command=lambda name=name: edit_event(name))
    button.pack(side=tk.TOP, padx=10, pady=10)
    button_instances.append(button)


def remove_button(name):
    if name is None:
        return
    for event in button_info:
        if event["name"] == name:
            button_info.remove(event)
    for button in button_instances:
        if button.cget("text") == name:
            button_instances.remove(button)
            button.destroy()


def organize_buttons():
    global button_instances
    global button_info
    print(str(button_instances) + "\n\n" + str(button_info))
    for button in button_info:
        remove_button(button["name"])
    button_instances = []
    for event in button_info:
        add_button(event["name"], event["description"], event["time"], event["type"])


# Add event button callback
def add_event():
    if event_name_box.get() == "":
        event_name_box.delete(0, tk.END)
        event_name_box.insert(0, "Event Name Required")
        return
    if event_name_box.get() == "Event Name Required" or event_name_box.get() == "Event Name Already Exists":
        return
    if button_info != []:
        for event in button_info:
            if event_name_box.get() == event["name"]:
                event_name_box.delete(0, tk.END)
                event_name_box.insert(0, "Event Name Already Exists")
                return
    if event_description_box.get(1.0, tk.END) == "\n" or event_description_box.get(1.0,
                                                                                   tk.END) == "Event Description Required\n" or event_description_box.get(
            1.0, tk.END) == "Event Description Required" or event_description_box.get(1.0, tk.END) == "":
        event_description_box.delete(1.0, tk.END)
        event_description_box.insert(1.0, "Event Description Required")
        return
    if event_type_dropdown.get() == "Event Type" or event_type_dropdown.get() == "Event Type Required":
        event_type_dropdown.set("Event Type Required")
        return
    if event_time_override_box.get() == "":
        eventTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Using current time: {eventTime}")
    else:
        try:
            if len(event_time_override_box.get()) == 8 and event_time_override_box.get()[2] == ":" and \
                    event_time_override_box.get()[5] == ":" and int(event_time_override_box.get()[0:2]) < 24 and int(
                    event_time_override_box.get()[3:5]) < 60 and int(event_time_override_box.get()[6:8]) < 60 and int(
                    event_time_override_box.get()[0:2]) >= 0 and int(event_time_override_box.get()[3:5]) >= 0 and int(
                    event_time_override_box.get()[6:8]) >= 0:
                eventTime = event_time_override_box.get()
                print(f"Using user defined time: {eventTime}")
            else:
                event_time_override_box.delete(0, tk.END)
                event_time_override_box.insert(0, "Invalid time format. Use 24hr format (HH:MM:SS)")
                return
        except ValueError:
            event_time_override_box.delete(0, tk.END)
            event_time_override_box.insert(0, "Invalid time format. Use 24hr format (HH:MM:SS)")
            return
        except TypeError:
            event_time_override_box.delete(0, tk.END)
            event_time_override_box.insert(0, "Invalid time format. Use 24hr format (HH:MM:SS)")
            return

    print(
        f"New Event button pressed\nEvent: {event_name_box.get()}\nDescription: {event_description_box.get(1.0, tk.END)}\nTime: {eventTime}")
    add_button(event_name_box.get(), event_description_box.get(1.0, tk.END), eventTime, event_type_dropdown.get())

    event_name_box.delete(0, tk.END)
    event_description_box.delete(1.0, tk.END)
    event_type_dropdown.set("Event Type")
    event_time_override_box.delete(0, tk.END)
    event_time_override_box.configure(placeholder_text="Event Time Override (Optional. 24hr format)")

    event_name_box.grid_forget()
    event_type_dropdown.grid_forget()
    event_description_label.grid_forget()
    event_description_box.grid_forget()
    event_time_override_box.grid_forget()
    add_event_button.grid_forget()
    new_event_button.grid(row=0, column=0, padx=10, pady=10)

    organize_buttons()


title_box = tk.CTkEntry(top_frame, placeholder_text="Doc Title")


def debug_button_callback():
    # Add 4 numbered events
    for i in range(4):
        add_button(f"Event {i + 1}", f"Event {i + 1} description", datetime.datetime.now().strftime("%H:%M:%S"),
                   "Debug")
    print(f"button_info: {button_info}\nbutton_instances: {button_instances}")


debug_button = tk.CTkButton(top_frame, text="Debug", fg_color="darkgray", hover_color="lightgray",
                            command=debug_button_callback)

# Create an Add Event button
add_event_button = tk.CTkButton(bottom_left_frame, text="Add Event", fg_color="darkgray", hover_color="lightgray",
                                command=add_event, width=50, height=30)

# Create an Event Name box
event_name_box = tk.CTkEntry(bottom_left_frame, width=300, height=30, placeholder_text="Event Name")

# Event Type dropdown menu
event_type_options = ["Attendence", "Discussion", "Question", "Decision", "Action Item", "Other"]
event_type_dropdown = tk.CTkOptionMenu(bottom_left_frame, values=event_type_options)
event_type_dropdown.configure(width=300, height=30)
event_type_dropdown.set("Event Type")

# Create an Event Description label
event_description_label = tk.CTkLabel(bottom_left_frame, text="Event Description")

# Create an Event Description box
event_description_box = tk.CTkTextbox(bottom_left_frame, width=300, height=100)

# Create an optional time override box
event_time_override_box = tk.CTkEntry(bottom_left_frame, width=300, height=30,
                                      placeholder_text="Event Time Override (Optional. 24hr format)")


def edit_event(name):
    event_info = {}
    for event in button_info:
        if event["name"] == name:
            event_info = event
    new_event_button.grid_forget()
    event_name_box.grid(row=0, column=0, padx=10, pady=10)
    event_type_dropdown.grid(row=1, column=0, padx=10, pady=10)
    event_description_label.grid(row=2, column=0, padx=10, pady=10)
    event_description_box.grid(row=3, column=0, padx=10, pady=0)
    event_time_override_box.grid(row=4, column=0, padx=10, pady=10)

    print("Inserting event info into boxes")
    event_name_box.delete(0, tk.END)  # Clear the contents of the event_name_box
    event_name_box.insert(0, event_info["name"])
    event_description_box.delete(1.0, tk.END)  # Clear the contents of the event_description_box
    event_description_box.insert(tk.END, event_info["description"])
    event_type_dropdown.set(event_info["type"])
    event_time_override_box.delete(0, tk.END)  # Clear the contents of the event_time_override_box
    event_time_override_box.insert(0, event_info["time"])
    add_event_button.grid(row=3, column=5, padx=10, pady=10)
    print("Edit window created.")
    remove_button(name)


def new_event():
    # Add event entry to the grid

    eventTime = datetime.datetime.now().strftime("%H:%M")

    # Remove the New Event button
    new_event_button.grid_forget()

    event_name_box.grid(row=0, column=0, padx=10, pady=10)
    event_type_dropdown.grid(row=1, column=0, padx=10, pady=10)
    event_description_label.grid(row=2, column=0, padx=10, pady=10)
    event_description_box.grid(row=3, column=0, padx=10, pady=0)
    event_time_override_box.grid(row=4, column=0, padx=10, pady=10)
    add_event_button.grid(row=3, column=5, padx=10, pady=10)

    event_name_box.delete(0, tk.END)  # Clear the contents of the event_name_box
    event_description_box.delete(1.0, tk.END)  # Clear the contents of the event_description_box
    event_type_dropdown.set("Event Type")
    event_time_override_box.delete(0, tk.END)  # Clear the contents of the event_time_override_box
    event_time_override_box.configure(placeholder_text="Event Time Override (Optional. 24hr format)")


# Create a New Event button
new_event_button = tk.CTkButton(bottom_left_frame, text="New Event", fg_color="darkgray", hover_color="lightgray",
                                command=new_event, width=50, height=30)


# New Doc button callback
def new_doc():
    title_box.pack(side=tk.LEFT, padx=10, pady=10)
    publish_button.pack(side=tk.LEFT, padx=10, pady=10)
    new_event_button.grid(row=0, column=0, padx=10, pady=10)


# Exit button callback
def exit(event=None, type=None):
    try:
        root.destroy()
        print("Exiting with code 0, no errors.")
        os._exit(0)
        print("Exiting has encountered an unknown error. Exiting with code 1.")
        os._exit(1)
    except KeyboardInterrupt:
        print("Exiting with code 0, no errors. (Ctrl+C)")
        os._exit(0)
    except SystemExit:
        print("Exiting with code 0, no errors. (SystemExit)")
        os._exit(0)
    except Exception as e:
        print(f"Exiting has encountered an unknown error. Exiting with code 1.\nError: {e}")
        os._exit(1)


# Publish button callback
def publish():
    if title_box.get() == "":
        title_box.delete(0, tk.END)
        title_box.insert(0, "Title Required")
        return
    if title_box.get() == "Title Required" or title_box.get() == "No Events":
        return
    if not button_info:
        title_box.delete(0, tk.END)
        title_box.insert(0, "No Events")
    # Create an embed with all the events
    webhook = ""
    import requests
    # Create the embed data
    embed = {
        "title": title_box.get(),
        "description": "MyNewt Minutes, manual entry",
        "color": 0x0000ff,  # Blue
        # Generate fields from the button_info list
        "fields": [
            {
                "name": event["time"] + " - " + event["type"],
                "value": "Name: " + event["name"] + "\n" + event["description"],
                "inline": False
            } for event in button_info
        ],
        "footer": {
            "text": "MyNewt Minutes"
        }
    }

    # Create the payload data
    payload = {
        "embeds": [embed]
    }

    # Make the POST request to the webhook URL with the payload data
    webhook = input("Webhook URL: ")
    response = requests.post(webhook, json=payload)

    # Check the response status code
    if response.status_code == 204:
        print("Webhook sent successfully.")
    else:
        print(f"Webhook failed with status code {response.status_code}.")


# Create a "New" button in the top frame
new_button = tk.CTkButton(top_frame, text="New Doc", fg_color="darkgray", hover_color="lightgray", command=new_doc)
new_button.pack(side=tk.LEFT, padx=10, pady=10)

# Create a "Publish" button in the top frame
publish_button = tk.CTkButton(top_frame, text="Publish", fg_color="darkgreen", hover_color="green", command=publish)

# Create an "Exit" button in the top frame
exit_button = tk.CTkButton(top_frame, text="Exit", fg_color="darkred", hover_color="red", command=exit)
exit_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Main loop
root.mainloop()
