from datetime import datetime
import os

folder_name="attendance_logs"
os.makedirs(folder_name, exist_ok=True)

def get_today_file():
    date_today=datetime.now().strftime("%d-%m-%Y")
    return f"{folder_name}/{date_today}.txt"

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")




def attendance_input(name, status):
    file_path=get_today_file()  
    time_now=get_current_time()

    with open(file_path, 'a') as file:
        file.write(f"{name}, {time_now}, {status}")
        print(f"✅ Saved: {name} marked {status} at {time_now}\n")


def main():
    print("Welcome to the Attendance System")

    while True:
        name=input("📍Enter Employee name: (or type 'exit' to quit)").strip()
        status=input("📍Mark attendance as 'IN' or 'OUT':").strip().upper()

        if name.lower()=='exit':
            print("Exiting.....")
            break
        if name=='':
            print("Name Cannot be empty. Please Enter Your name")
            continue

        
        if status not in ['IN', 'OUT']:
            print("Only 'IN' or 'OUT' is allowed")
            continue

        attendance_input(name, status)
main()