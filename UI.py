import tkinter as tk


def show_popup():
	popup = tk.Tk()
	popup.title("Popup Window")
	popup.geometry("300x300")
	popup.resizable(True, True)

	tk.Label(popup, text="Hello! This is a popup window.").pack(expand=True)
	tk.Button(popup, text="Close", command=popup.destroy).pack(pady=(0, 15))

	popup.mainloop()


if __name__ == "__main__":
	show_popup()
