import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import customtkinter as ctk

# Resize splash logo image
image_path = 'D:/logo/motologo5.png'
img = Image.open(image_path)
resized_img = img.resize((430, 750))
resized_img.save("temp_logo.png", "PNG")

# Splash screen
splash_root = tk.Tk()
splash_root.geometry("430x750")
splash_root.title("Motivation Quotes")
splash_root.iconbitmap('logo2.ico')

splash_label = Label(splash_root, text="Empower your journey with the right mindset", font=("Raleway", 10))
splash_label.place(x=130, y=50)

# Splash logo
logo_image = ImageTk.PhotoImage(resized_img)
lbl = Label(splash_root, image=logo_image)
lbl.image = logo_image  # keep a reference to avoid garbage collection
lbl.pack()

# Main window
def main_window():
    root = tk.Tk()
    root.title('Main')
    root.iconbitmap('logo2.ico')
    root.geometry("430x750")
    root.config(bg='#001F3F')
    root.resizable(width=False, height=True)

    # Load and display main window logo
    main_image_path = 'khakilogo.png'
    main_img = Image.open(main_image_path)
    resized_main_img = main_img.resize((44, 44), Image.LANCZOS)
    main_logo_image = ImageTk.PhotoImage(resized_main_img)
    main_label = Label(root, image=main_logo_image, bg='#001F3F')
    main_label.image = main_logo_image
    main_label.place(rely=0.02, relx=0.02)

    line_img = ImageTk.PhotoImage(Image.open('line.png'))
    bgline = Label(root, image=line_img, bg='#001f3f', width= 440)
    bgline.image = line_img
    bgline.place(x=0, y=590)


    # Logo title
    title_label = Label(root, text="MOTIVATION QUOTES", font=("Raleway", 12, 'bold'), bg="#001F3F", fg="white")
    title_label.place(x=60, y=25)

    # Add button
    add_photo = Image.open('addbutton.png').resize((43, 36))
    photo_img = ImageTk.PhotoImage(add_photo)
    add_button = Label(root, image=photo_img, bg='#001F3F')
    add_button.image = photo_img
    add_button.place(x=360, y=16)

    # Image Slider
    images = ['m1.jpg', 'm2.png', 'm3.jpg', 'm4.png', 'm5.png', 'm6.jpg', 'm7.png', 'm8.jpg', 'm9.png', 'm10.png']
    current_image = 0
    slider_width = 430
    slider_height = 220
    
    slider_label = Label(root, bg='#001F3F')
    slider_label.place(x=-2, y=75)
    
    def update_image():
        nonlocal current_image
        image = Image.open(images[current_image]).resize((slider_width, slider_height))
        photo = ImageTk.PhotoImage(image)
        slider_label.config(image=photo)
        slider_label.image = photo
        current_image = (current_image + 1) % len(images)
        root.after(8000, update_image)

    # Start slideshow
    update_image()
    
    # Buttons
    life_button_img = ImageTk.PhotoImage(Image.open('rounded.png').resize((140, 38)))
    life_button = tk.Button(root, image=life_button_img, text='Life', font=('Raleway', 14, 'bold'),
    compound="center", fg="#001F3F", bg='#001F3F', borderwidth=0,
    activebackground='#001F3F', cursor='hand2')
    life_button.image = life_button_img
    life_button.place(x=15, y=320)

    edu_button_img = ImageTk.PhotoImage(Image.open('rounded2.png').resize((140, 38)))
    edu_button = tk.Button(root, image=edu_button_img, text='Education', font=('Raleway', 14, 'bold'),
    compound="center", fg="#201E43", bg='#001F3F', borderwidth=0,
    activebackground='#001F3F', activeforeground='#EAD8B1', cursor='hand2')
    edu_button.image = edu_button_img
    edu_button.place(x=162, y=320) 

    success_button_img = ImageTk.PhotoImage(Image.open('rounded2.png').resize((140, 38)))
    success_button = tk.Button(root, image=success_button_img, text='Success', font=('Raleway', 14, 'bold'),
    compound="center", fg="#201E43", bg='#001F3F', borderwidth=0,
    activebackground='#001F3F', activeforeground='#EAD8B1', cursor='hand2')
    success_button.image = success_button_img
    success_button.place(x=309, y=320)

    # Content
    scrollable_frame = ctk.CTkScrollableFrame(root, width=365, height=250, corner_radius=25, fg_color='#EAD8B1')
    scrollable_frame.place(x=15, y=375) 

    home_label1 = ctk.CTkLabel(
    scrollable_frame, 
    text="Each day you must choose the pain of discipline, or the pain of regret.",
    font=('Raleway', 16, 'bold'),
    text_color='#EAD8B1',
    fg_color='#634345', 
    width=360,
    height=160,
    corner_radius=20,
    wraplength=280
    )
    home_label1.pack(pady=(0, 0)) 
    home_label2 = ctk.CTkLabel(
    scrollable_frame, 
    text="Be the reason someone feels welcomed, seen, heard, valued, loved and supported.",
    font=('Raleway', 16, 'bold'),
    text_color='#EAD8B1',
    fg_color='#634345', 
    width=360,
    height=160,
    corner_radius=20,
    wraplength=280
    )
    home_label2.pack(pady=(20, 0))

    home_label3 = ctk.CTkLabel(
    scrollable_frame, 
    text="One day, you'll beliving the life you once prayed for.",
    font=('Raleway', 16, 'bold'),
    text_color='#EAD8B1',
    fg_color='#634345', 
    width=360,
    height=160,
    corner_radius=20,
    wraplength=280
    )
    home_label3.pack(pady=(20, 0))
    home_label4 = ctk.CTkLabel(
    scrollable_frame, 
    text="Accept both compliments and criticism. It takes both sun and rain for a flower to grow.",
    font=('Raleway', 16, 'bold'),
    text_color='#EAD8B1',
    fg_color='#634345', 
    width=360,
    height=160,
    corner_radius=20,
    wraplength=280
    )
    home_label4.pack(pady=(20, 0))

    home_label5 = ctk.CTkLabel(
    scrollable_frame, 
    text="Psychology says 'You ll never live a happy life if you always care about what others think about you.'",
    font=('Raleway', 16, 'bold'),
    text_color='#EAD8B1',
    fg_color='#634345', 
    width=360,
    height=160,
    corner_radius=20,
    wraplength=280
    )
    home_label5.pack(pady=(20, 0))

    home_label6 = ctk.CTkLabel(
    scrollable_frame, 
    text="Psychology says 'Ships don't sink because of the water around them. Ships sink because of the water that gets in them.' Don't let what's happening around you get inside you and weigh you down.",
    font=('Raleway', 16, 'bold'),
    text_color='#EAD8B1',
    fg_color='#634345', 
    width=360,
    height=160,
    corner_radius=20,
    wraplength=280
    )
    home_label6.pack(pady=(20, 0))

    home_label7 = ctk.CTkLabel(
    scrollable_frame, 
    text="Life isn't about finding yourself. It's about creating yourself.",
    font=('Raleway', 16, 'bold'),
    text_color='#EAD8B1',
    fg_color='#634345', 
    width=360,
    height=160,
    corner_radius=20,
    wraplength=280
    )
    home_label7.pack(pady=(20, 0))

    home_label8 = ctk.CTkLabel(
    scrollable_frame, 
    text="You cannot live when are you untouchable. Life vulnerability.",
    font=('Raleway', 16, 'bold'),
    text_color='#EAD8B1',
    fg_color='#634345', 
    width=360,
    height=160,
    corner_radius=20,
    wraplength=280
    )
    home_label8.pack(pady=(20, 0))

    home_label9 = ctk.CTkLabel(
    scrollable_frame, 
    text="Use the weekend to build the life you want instead of trying to escape the life you have.",
    font=('Raleway', 16, 'bold'),
    text_color='#EAD8B1',
    fg_color='#634345', 
    width=360,
    height=160,
    corner_radius=20,
    wraplength=280
    )
    home_label9.pack(pady=(20, 0))

    home_label10 = ctk.CTkLabel(
    scrollable_frame, 
    text="an inch of MOVEMENT will bring you closer to your goals than a mile of INTENTION.",
    font=('Raleway', 16, 'bold'),
    text_color='#EAD8B1',
    fg_color='#634345', 
    width=360,
    height=160,
    corner_radius=20,
    wraplength=280
    )
    home_label10.pack(pady=(20, 0))

    # navigation content
    custom_frame2 = ctk.CTkFrame(root, width=200, height=55, corner_radius=50, fg_color='#EAD8B1')
    custom_frame2.place(x=110, y=686)
    
    home_frame2 = ImageTk.PhotoImage(Image.open('home.png').resize((40,34)))
    home_frame = tk.Button( root,image=home_frame2,bg='#ead8b1',cursor='hand2', borderwidth=0,activebackground='#ead8b1')
    home_frame.image = home_frame2
    home_frame.place(x=118, y=696)

    favorite_frame2 = ImageTk.PhotoImage(Image.open('favorite.png').resize((40,34)))
    favorite_frame = tk.Button( root,image=favorite_frame2,bg='#ead8b1',cursor='hand2', borderwidth=0,activebackground='#ead8b1')
    favorite_frame.image = favorite_frame2
    favorite_frame.place(x=185, y=696)

    bookmark_frame2 = ImageTk.PhotoImage(Image.open('bookmark.png').resize((40,34)))
    bookmark_frame = tk.Button( root,image=bookmark_frame2,bg='#ead8b1',cursor='hand2', borderwidth=0,activebackground='#ead8b1')
    bookmark_frame.image = bookmark_frame2
    bookmark_frame.place(x=255, y=696)

    
# Screen delay
splash_root.after(3000, lambda: [splash_root.destroy(), main_window()])

# Splash screen mainloop
splash_root.mainloop()
