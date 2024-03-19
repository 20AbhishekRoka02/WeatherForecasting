# A GUI application to get Weather Forecast using an API.
from tkinter import *
import tkinter.messagebox as mbox
import requests as req

class Weather():
    """Weather class has required methods to utilise API to get Current Weather Forecast."""


    def __init__(self):
        """storing API key as private class variable."""
        self.__api_key = "<API-KEY>"
    
    def get_private_key(self):
        """Method to get private key (here, API key)"""
        return self.__api_key
    
    def getCurrentWeather(self, city, resultframe,location,temperature,feelslike,description,humidity, status, icon):
        """This method has logic to get Weather Forecast using API """

        def labelManage():
            pass

        if city in ["","Enter your city here"]:
            mbox.showwarning("Warning","Please provide City name.")
        else:
            response = req.get(f"http://api.weatherstack.com/current?access_key={self.get_private_key()}&query={city}")            
            data = response.json()
            

            if "error" in data.keys():                
                # show error message to user
                mbox.showerror("Error", "An Error Occurred.")

            else:
                
                image_url = data['current']['weather_icons'][0] 
                response = req.get(image_url) #getting image from icons  url stored in CDN (Content Delivery Network)


                if response.status_code == 200:                  
                    # Adding image to Label
                    image_data = response.content
                    image = PhotoImage(data=image_data)
                    icon.config(image=image)
                    icon.image = image
                    
                
                # Updating Location 
                location.set(f"{data['location']['name']}")
                
                # Updating Temperature 
                temperature.set(f"{data['current']['temperature']}\u00b0C")
                
                # Updating Feels like Temperature 
                feelslike.set(f"Feels like {data['current']['feelslike']}\u00b0C")
                

                # Updating Weather Description 
                description.set(f"{data['current']['weather_descriptions'][0]}")
                

                # Updating Humidity 
                humidity.set(f"Humidity {data['current']['humidity']}%")
                
                
                # Updating status bar
                status.set(f"Last recorded at: {data['current']['observation_time']}")

                

        
    

class MainApp():   

    def __init__(self): 
        
        def onFocusIn(event):
            if cityname.get() == placeholder:
                cityname.delete(0,"end")
                cityname.config(fg="black")
        def onFocusOut(event):
            if cityname.get()=="":
                cityname.insert(0, placeholder)
                cityname.config(fg="gray")
            


        root = Tk()

        # root window title and dimension
        root.title("Weather Forecast")        
        root.geometry('500x400')
        root.resizable(width=False, height=False) #Disabling Resize


        # This is our UI frame, containing Title, Input bar and Search Button.        
        uiframe = Frame(root, width=500, height=400)   

        # Frame will display result to user.
        resultframe = Frame(root)

        # Adding title label.
        titlefontstyle = ("Montserrat", 18, "bold")
        titleLable = Label(uiframe, text="Weather GUI", anchor="center", fg="#003153", font=titlefontstyle)

        #City Input bar
        placeholder="Enter your city here"
        fontstyle = ("Segoe UI Light", 18)
        cityname=Entry(uiframe,fg="gray",font=fontstyle)
        cityname.insert(0, placeholder)
        cityname.bind("<FocusIn>", onFocusIn) #On Right Click in by mouse.
        cityname.bind("<FocusOut>", onFocusOut) #On Focus Out from Input bar.
        

        # Search Button
        weatherForcast= Weather() #Creating Object of Class Weather()


        searchbuttonfontstyle = ("Roboto Bold", 15, "bold")
        search = Button(uiframe, text="Search", font=searchbuttonfontstyle, bg="red", fg="white", command= lambda: weatherForcast.getCurrentWeather(cityname.get(), resultframe,location,temperature,feelslike,description,humidity,statusvariable, icon))

        # Placing things on Screen.
        titleLable.grid(column=1, row=0, columnspan=2)
        cityname.grid(column=1, row=1)
        search.grid(column=2,row=1)

        #Placing Result in resultframe

        resultfont = ("Open Sans", 14)
        # Location Label
        location = StringVar()
        Label(resultframe,textvariable=location, font=resultfont).grid(column=0, row=0)

        #weather icon
        icon = Label(resultframe) #defining label that will display weather icon
        icon.grid(column=0, row=1)

        # Temperature Label
        temperature = StringVar()
        Label(resultframe,textvariable=temperature, font=resultfont).grid(column=0, row=2)

                
        # Feels like Temperature Label
        feelslike = StringVar()
        Label(resultframe,textvariable=feelslike, font=resultfont).grid(column=0, row=3)

        # Weather Description Label
        description = StringVar()
        Label(resultframe,textvariable=description, font=resultfont).grid(column=0, row=4)

        # Humidity Label
        humidity = StringVar()
        Label(resultframe,textvariable=humidity, font=resultfont).grid(column=0, row=5)

        # Status bar
        statusbar=Frame(root,width=500, height=20, bg="white")
        statusvariable = StringVar()        
        statusLabel = Label(statusbar, textvariable=statusvariable, relief=SUNKEN, anchor=W, bg="white", font=("Lato Light", 12))
        statusLabel.pack(fill=X)
        
        # Packing all Frames to GUI
        uiframe.pack(pady=20)
        resultframe.pack()
        statusbar.pack(side=BOTTOM, fill=X)
        root.mainloop()

if __name__=="__main__":
    app = MainApp()
    
