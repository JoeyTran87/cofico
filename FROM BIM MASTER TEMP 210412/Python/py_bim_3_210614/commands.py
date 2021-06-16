# import the time module
import time
  
# define the countdown func.
def countdown(t,str_count,str_done):    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(str_count,timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print(f"--------{str_done}-------------")
  
  
# # input time in seconds
# t = input("Enter the time in seconds: ")
  
# function call
# countdown(int(3),"Thao tác đang diễn ra , còn ","Thao tác hoàn tất")
def spinWaiting():
    spin = "|/-\\" 
    t = 1
    while t:
        for s in spin:
            print(s, s, s ,s,s,s,s,s,s,s,s,s,s,end="\r")
            time.sleep(1/len(spin))
        t -= 1

    print("------------------------------------------------------------------")

# spin(3)

def coficoLoading ():
    cofico = "COFICO BIM MANAGER LOADING . . ."    
    t = 4
    step = t/len(cofico)
    while t:
        for s in cofico:
            print(s,end="\r")
            time.sleep(step)
        t -= step

    print("Done---------------------------------------------------")

# coficoLoading ()