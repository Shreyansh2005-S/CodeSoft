import tkinter as tk
from tkinter import messagebox

# Store contacts in a list of dictionaries
contacts = []

def add_contact():
    name_val = name_var.get().strip()
    phone_val = phone_var.get().strip()
    email_val = email_var.get().strip()
    address_val = address_var.get().strip()

    if not name_val or not phone_val:
        messagebox.showerror("Error", "Store Name and Phone are required.")
        return

    contacts.append({
        "name": name_val,
        "phone": phone_val,
        "email": email_val,
        "address": address_val
    })
    clear_inputs()
    refresh_listbox()
    messagebox.showinfo("Success", "Contact added!")

def refresh_listbox():
    listbox.delete(0, tk.END)
    for i, c in enumerate(contacts):
        listbox.insert(tk.END, f"{i+1}. {c['name']} - {c['phone']}")

def clear_inputs():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    address_var.set("")

def on_select(event):
    if not listbox.curselection():
        return
    index = listbox.curselection()[0]
    contact = contacts[index]
    name_var.set(contact["name"])
    phone_var.set(contact["phone"])
    email_var.set(contact["email"])
    address_var.set(contact["address"])

def update_contact():
    if not listbox.curselection():
        messagebox.showwarning("Warning", "Select a contact to update.")
        return
    index = listbox.curselection()[0]

    name_val = name_var.get().strip()
    phone_val = phone_var.get().strip()
    email_val = email_var.get().strip()
    address_val = address_var.get().strip()

    if not name_val or not phone_val:
        messagebox.showerror("Error", "Store Name and Phone are required.")
        return

    contacts[index] = {
        "name": name_val,
        "phone": phone_val,
        "email": email_val,
        "address": address_val
    }
    clear_inputs()
    refresh_listbox()
    messagebox.showinfo("Success", "Contact updated!")

def delete_contact():
    if not listbox.curselection():
        messagebox.showwarning("Warning", "Select a contact to delete.")
        return
    index = listbox.curselection()[0]
    contact = contacts.pop(index)
    clear_inputs()
    refresh_listbox()
    messagebox.showinfo("Deleted", f"Deleted contact: {contact['name']}")

def search_contact():
    query = search_var.get().strip().lower()
    listbox.delete(0, tk.END)
    for i, c in enumerate(contacts):
        if query in c["name"].lower() or query in c["phone"]:
            listbox.insert(tk.END, f"{i+1}. {c['name']} - {c['phone']}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Contact Manager")

name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
address_var = tk.StringVar()
search_var = tk.StringVar()

# Input fields
tk.Label(root, text="Store Name").grid(row=0, column=0, sticky="w")
tk.Entry(root, textvariable=name_var).grid(row=0, column=1)

tk.Label(root, text="Phone").grid(row=1, column=0, sticky="w")
tk.Entry(root, textvariable=phone_var).grid(row=1, column=1)

tk.Label(root, text="Email").grid(row=2, column=0, sticky="w")
tk.Entry(root, textvariable=email_var).grid(row=2, column=1)

tk.Label(root, text="Address").grid(row=3, column=0, sticky="w")
tk.Entry(root, textvariable=address_var).grid(row=3, column=1)

# Buttons
tk.Button(root, text="Add", command=add_contact).grid(row=0, column=2, padx=5)
tk.Button(root, text="Update", command=update_contact).grid(row=1, column=2, padx=5)
tk.Button(root, text="Delete", command=delete_contact).grid(row=2, column=2, padx=5)

# Search field
tk.Label(root, text="Search").grid(row=4, column=0, sticky="w")
tk.Entry(root, textvariable=search_var).grid(row=4, column=1)
tk.Button(root, text="Search", command=search_contact).grid(row=4, column=2, padx=5)

# Contact listbox
listbox = tk.Listbox(root, width=50)
listbox.grid(row=5, column=0, columnspan=3, pady=10)
listbox.bind("<<ListboxSelect>>", on_select)

root.mainloop()
