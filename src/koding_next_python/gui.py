import customtkinter as ctk
from .pricing import calculate


def run_gui():
    app = ctk.CTk()
    app.title("Price Calculator")
    app.geometry("500x600")


    frame = ctk.CTkFrame(app, fg_color="transparent")
    frame.pack(expand=True)


    quantity_label = ctk.CTkLabel(frame, text="Quantity")
    quantity_label.pack()
    quantity_input = ctk.CTkEntry(
        frame,
        placeholder_text="Quantity",
        width=380,
        height=50,
    )
    quantity_input.pack(pady=10)


    quantity_label = ctk.CTkLabel(frame, text="Discount (%)")
    quantity_label.pack()
    discount_input = ctk.CTkEntry(
        frame,
        placeholder_text="Discount (%)",
        width=380,
        height=50,
    )
    discount_input.pack(pady=10)


    quantity_label = ctk.CTkLabel(frame, text="Price")
    quantity_label.pack()
    price_input = ctk.CTkEntry(
        frame,
        placeholder_text="Price",
        width=380,
        height=50,
    )
    price_input.pack(pady=10)


    result_label = ctk.CTkLabel(
        frame,
        text="Final Price: Rp. 0",
    )
    result_label.pack(pady=(30, 25))

    def calculate_price():
        quantity = int(quantity_input.get())
        discount = float(discount_input.get())
        price = float(price_input.get())

        result = calculate(price, discount, quantity)

        result_label.configure(
            text=f"Final Price: Rp. {result}"
        )

    button = ctk.CTkButton(
        frame,
        text="Calculate",
        width=380,
        height=55,
        command=calculate_price,
    )
    button.pack(pady=15)

    app.mainloop()
