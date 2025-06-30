
import pyautogui
import pyperclip
import time
import google.generativeai as genai
import sys

# Step 0: Configure Gemini API
genai.configure(api_key="")
model = genai.GenerativeModel('gemini-1.5-flash')

last_reply_sent = ""  # Used to avoid replying to self

# Step 1: Click to focus the chat app once at the start
pyautogui.click(706, 1056)
time.sleep(1)

while True:
    time.sleep(2)

    # Step 2: Select the latest message area
    pyautogui.moveTo(632, 200)
    pyautogui.mouseDown()
    pyautogui.moveTo(1858, 958, duration=1)
    pyautogui.mouseUp()
    time.sleep(0.5)

    # Step 3: Copy selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    copied_text = pyperclip.paste().strip()

    print("----- Copied Text -----")
    print(copied_text)
    print("------------------------")

    # Step 4: Skip if text is empty or same as last reply
    if copied_text == last_reply_sent or copied_text == "":
        print("Last message is from you or empty. Skipping...\n")
        time.sleep(5)
        continue

    # Step 5: Get the last line only (most recent message)
    last_line = copied_text.split('\n')[-1].strip()

    # Step 6: Skip if the last message is from yourself (UMAعR💫)
    if "umaعr💫:" in last_line.lower():
        print("Last message is from UMAعR💫 (you). Skipping...\n")
        time.sleep(5)
        continue

    # Step 7: Generate AI response
    response = model.generate_content([
        "You are a real person whose name is UMAIR. "
        "You analyze the chat and talk like real umair. "
        "Give ME SHORT AND interesting responses please. You can speak Urdu as well when asked.",
        "output should be next chat response as Umair",
        "Do not specially mention my name and time to response",
        copied_text,
    ])

    ai_reply = response.text.strip()

    print("----- AI Response -----")
    print(ai_reply)
    print("------------------------")

    # Step 8: Paste and send the reply
    pyperclip.copy(ai_reply)
    time.sleep(0.5)
    pyautogui.click(889, 1007)  # Focus chat input box
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.2)
    pyautogui.press('enter')

    # Step 9: Save the reply to prevent echoing
    last_reply_sent = ai_reply

    # Step 10: Wait before next check
    time.sleep(5)
