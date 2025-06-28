import pyautogui
import pyperclip
import time
import google.generativeai as genai

# Step 0: Configure Gemini API
genai.configure(api_key="git ")
model = genai.GenerativeModel('gemini-1.5-flash')

last_reply_sent = ""  # Used to avoid replying to self

while True:

    # Step 1: Give user time to switch to the correct screen
    time.sleep(2)

    # Step 2: Click on the app/icon to activate window
    pyautogui.click(706, 1056)
    time.sleep(1)

    # Step 3: Click and drag to select the text
    pyautogui.moveTo(632, 200)
    pyautogui.mouseDown()
    pyautogui.moveTo(1858, 958, duration=1)
    pyautogui.mouseUp()
    time.sleep(0.5)

    # Step 4: Copy the selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)

    # Step 5: Save copied text into a variable
    copied_text = pyperclip.paste().strip()
    print("----- Copied Text -----")
    print(copied_text)
    print("------------------------")

    # Step 6: Check if copied text is same as last reply
    if copied_text == last_reply_sent or copied_text == "":
        print("Last message is from you or empty. Skipping...\n")
        time.sleep(5)
        continue

    # Step 7: Get AI-generated response from Gemini
    response = model.generate_content([
        "You are a real person whose name is UMAIR. "
        "You analyze the chat and talk like real umair. "
        "Give ME SHORT AND interesting responses please. You can speak Urdu as well when asked.",
        "output should be next chat response as Umair",
        "Do not specially mention my name and time to response",
        copied_text,
    ])

    # Step 8: Store and print the AI response
    ai_reply = response.text.strip()
    print("----- AI Response -----")
    print(ai_reply)
    print("------------------------")

    # Step 9: Paste the AI response in chatbox and press Enter
    pyperclip.copy(ai_reply)
    time.sleep(0.5)
    pyautogui.click(889, 1007)      # Focus chatbox
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'v')   # Paste response
    time.sleep(0.2)
    pyautogui.press('enter')        # Send message

    # Step 10: Save this reply to avoid self-replies
    last_reply_sent = ai_reply

    # Step 11: Optional wait before next check
    time.sleep(5)

