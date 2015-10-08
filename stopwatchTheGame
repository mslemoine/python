# template for "Stopwatch: The Game"
import simplegui

# define global variables
interval = 100
dec_secs = 0
win = 0
total = 0
status = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    #0:00.0
    secs = t / 10
    str_secs =str(secs)
    
    minute = secs / 60
    if secs >= 60:
        secs = secs % 60
        str_secs =str(secs)
    if secs < 10:
        str_secs = "0"+str(secs)

    dec_secs = t%10
    message = str(minute) + ":" + str_secs + "."+str(dec_secs)
    return message
    

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    global status
    status = True
    timer.start()
    

def stop_timer():
    global total
    global win
    global status
    if status:
        timer.stop()
        total += 1
        if dec_secs % 10 == 0:
            win += 1
        status = False
        

def restart_timer():
    global total
    global win
    global dec_secs
    global status
    dec_secs = 0
    win = 0
    total = 0
    if status:
        timer.stop()
        status = False


# define event handler for timer with 0.1 sec interval
def time():
    global dec_secs
    dec_secs += 1

# define draw handler
def draw(canvas):
    """Draw message."""
    canvas.draw_text(format(dec_secs), [90,140], 50, "Blue")
    canvas.draw_text(str(win) + "/" + str(total), 
                     [130,50], 35, "Green")

    
# create frame
frame = simplegui.create_frame(format(dec_secs), 300, 200)
frame.set_draw_handler(draw)
frame.add_button("Start", start_timer, 100)
frame.add_button("Stop", stop_timer, 100)
frame.add_button("Reset", restart_timer, 100)




# register event handlers
timer = simplegui.create_timer(interval, time)



# start frame
frame.start()

# You can test this code at: http://www.codeskulptor.org/#user40_dWANAbLx6mXLxhf.py
