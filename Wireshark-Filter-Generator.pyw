import tkinter as tk
from tkinter import ttk, messagebox

def generate_filter(call_ids, root, exclude):
    # Generate the filter string, either including or excluding the Call-IDs
    if exclude:
        filter_string = ' && '.join(f'sip.Call-ID != "{call_id}"' for call_id in call_ids)
    else:
        filter_string = ' || '.join(f'sip.Call-ID == "{call_id}"' for call_id in call_ids)

    # Copy the filter to the clipboard
    root.clipboard_clear()
    root.clipboard_append(filter_string)

    # Notify user that the filter has been copied
    messagebox.showinfo("Success", "Filter copied to clipboard!")

def create_display_filter(contact_uris, exclude):
    # Create the display filter, either including or excluding the Contact URIs
    if exclude:
        contact_filters = [f'sip.contact.uri != "{uri}"' for uri in contact_uris]
    else:
        contact_filters = [f'sip.contact.uri == "{uri}"' for uri in contact_uris]
    
    combined_filter = ' or '.join(contact_filters)
    return combined_filter

def uri_filter(contact_uris, root, exclude):
    # Create the display filter
    display_filter = create_display_filter(contact_uris, exclude)

    # Copy the filter to the clipboard
    root.clipboard_clear()
    root.clipboard_append(display_filter)

    # Notify user that the filter has been copied
    messagebox.showinfo("Success", "Filter copied to clipboard!")

def process_input(root):
    filter_type = filter_type_var.get()
    data = input_text.get("1.0", tk.END).strip().splitlines()

    if not data:
        messagebox.showerror("Error", "Please paste data into the text area.")
        return

    exclude = exclude_var.get()  # Check if the exclude checkbox is selected

    if filter_type == "Call-ID Filter":
        generate_filter(data, root, exclude)
    elif filter_type == "Contact URI Filter":
        uri_filter(data, root, exclude)
    else:
        messagebox.showerror("Error", "Please select a valid filter type.")

def create_gui():
    root = tk.Tk()
    root.title("Wireshark Filter Generator")

    # Set window icon
    # root.iconbitmap('path_to_icon.ico')  # Uncomment this line and set your icon file path if needed

    # Dropdown for filter type
    global filter_type_var
    filter_type_var = tk.StringVar()
    filter_type_label = tk.Label(root, text="Select Filter Type:")
    filter_type_label.pack(padx=10, pady=5)

    filter_type_dropdown = ttk.Combobox(root, textvariable=filter_type_var, state="readonly")
    filter_type_dropdown['values'] = ("Call-ID Filter", "Contact URI Filter")
    filter_type_dropdown.pack(padx=10, pady=5)

    # Text area to paste the data
    input_label = tk.Label(root, text="Paste Data Here (one per line):")
    input_label.pack(padx=10, pady=5)

    global input_text
    input_text = tk.Text(root, height=10, width=50)
    input_text.pack(padx=10, pady=5)

    # Checkbox for excluding
    global exclude_var
    exclude_var = tk.BooleanVar()
    exclude_checkbox = tk.Checkbutton(root, text="Exclude these items", variable=exclude_var)
    exclude_checkbox.pack(padx=10, pady=5)

    # Generate button
    generate_button = tk.Button(root, text="Generate Filter", command=lambda: process_input(root))
    generate_button.pack(padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
